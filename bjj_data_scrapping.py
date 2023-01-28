import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import os

def principal_period(s):
    i = (s+s).find(s, 1, -1)
    return None if i == -1 else s[:i]


def get_page_html(url, filename):
    data = requests.get(url)

    with open(filename, 'w+') as f:
        f.write(data.text)


def main_page_scrapper(filename):
    with open(filename) as f:
        page = f.read()

    soup = BeautifulSoup(page, "html.parser")

    return soup


def get_fighters_page(soup):
    fighters_links = []

    for link in soup.find_all('a'):
        if "p=" in str(link.get('href')):
            fighters_links.append(link.get('href'))

    fighters_links = list(set(fighters_links))
            
    return fighters_links

def check_folder(folder):
    if not os.path.isdir(folder):
        os.makedirs(folder)

def fighters_page_scrapper(fighters_links, url, folder):
    fighters_links_count = len(fighters_links)
    i = 0

    for link in fighters_links:
        request_url = url.format(link)
        data = requests.get(url)
        
        with open("{}/{}.html".format(folder, link[4:]), "w+", encoding='utf-8') as f:
            f.write(data.text)
        
        i += 1
        print(f'>>> Baixando dados do lutador: {i}/{fighters_links_count}', end='\r')