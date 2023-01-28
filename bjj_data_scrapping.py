import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import os

def principal_period(s):
    i = (s+s).find(s, 1, -1)
    return None if i == -1 else s[:i]

# This function uses the requests library to make a request to the specified URL and then writes the response (the HTML of the page) to a file with the specified filename.
def get_page_html(url, filename):
    data = requests.get(url)

    with open(filename, 'w+') as f:
        f.write(data.text)

# This function takes in a filename as an argument. The function opens the file and reads the contents. It then creates a BeautifulSoup object from the page using html.parser and returns the soup object. This function can be used to scrape data from webpages for further processing.
def main_page_scrapper(filename):
    with open(filename) as f:
        page = f.read()

    soup = BeautifulSoup(page, "html.parser")

    return soup


def get_fighters_page_link(soup):
    fighters_links = []

    for link in soup.find_all('a'):
        if "p=" in str(link.get('href')):
            fighters_links.append(link.get('href'))

    fighters_links = list(set(fighters_links))
            
    return fighters_links

# This code checks to see if a folder exists. If it does not, it creates the folder.
def check_folder(folder):
    if not os.path.isdir(folder):
        os.makedirs(folder)

def get_fighters_page_html(fighters_links, url, folder):
    fighters_links_count = len(fighters_links)
    i = 0

    for link in fighters_links:
        request_url = url.format(link)
        data = requests.get(url)
        
        with open("{}/{}.html".format(folder, link[4:]), "w+", encoding='utf-8') as f:
            f.write(data.text)
        
        i += 1
        print(f'>>> Downloading grappler data: {i}/{fighters_links_count}', end='\r')

def fighters_page_scrapper_html(fighters_links, folder):
    fighters_list = []
    df_list = []
    for id in fighters_links:
        with open("{}/{}.html".format(folder, id[4:]), encoding="utf-8") as f:
            page = f.read()

        soup = BeautifulSoup(page, "html.parser")   

        # GATHER FIGHTER DATA
        try:
            fighter_name = soup.find('strong', text=re.compile("Full Name")).parent.getText().split(": ",1)[1]
        except:
            fighter_name = ""
        try:
            fighter_weight_class = soup.find('strong', text=re.compile("Weight Division")).parent.getText().split(": ",1)[1]
        except:
            fighter_weight_class = ""  
        try:
            fighter_team = soup.find('strong', text=re.compile("Team/Association")).parent.getText().split(": ",1)[1]
        except:
            fighter_team = ""

        fighters_list.append([id[4:], fighter_name, fighter_weight_class, fighter_team])

        try:
            fighter_record = pd.read_html(str(soup.find("table", {"class": "table table-striped sort_table"})))[0]
        #     fighter_record['Opponent'] = principal_period(fighter_record['Opponent'])
            fighter_record['Fighter Id'] = id[4:]
            df_list.append(fighter_record)
        except:
            data = []
            fighter_record = pd.DataFrame(data)
        