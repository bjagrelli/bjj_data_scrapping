import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import os
from datetime import datetime

# This function uses the requests library to make a request to the specified URL and then writes the response (the HTML of the page) to a file with the specified filename.
def get_page_html(url):
    data = requests.get(url)

    return data.text

# This function takes in a filename as an argument. The function opens the file and reads the contents. It then creates a BeautifulSoup object from the page using html.parser and returns the soup object. This function can be used to scrape data from webpages for further processing.
def main_page_scraper(html):
    soup = BeautifulSoup(html, "html.parser")

    return soup


def get_fighters_page_link(soup, url):
    fighters_links = []

    for link in soup.find_all('a'):
        if "p=" in str(link.get('href')):
            fighters_links.append(link.get('href'))

    fighters_links = list(set(fighters_links))
    for idx, link in enumerate(fighters_links):
        fighters_links[idx] = url.format(link)
            
    return fighters_links

def fighters_page_scraper_html(scraper_dict, fighters_links):
    fighters_list = []
    for link in fighters_links:
        id = link.replace('https://www.bjjheroes.com/bjj-fighters/?p=', '')

        raw_html = scraper_dict[link]['Raw Html']

        soup = BeautifulSoup(raw_html, "html.parser")   

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
        try:
            fight_record = soup.find("table", {"class": "table table-striped sort_table"})
        except:
            fight_record = []

        fighters_list.append((id, fighter_name, fighter_weight_class, fighter_team, fight_record))

    return fighters_list        