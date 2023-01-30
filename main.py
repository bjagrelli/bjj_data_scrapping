from functions import *
from WebScrapper import WebScraper

# Variables
main_page_url = 'https://www.bjjheroes.com/a-z-bjj-fighters-list'
fighter_page_url = 'https://www.bjjheroes.com/bjj-fighters{}'

def main():
    
    main_page_html = get_page_html(main_page_url)

    print('>>> Beginning of process\n')

    soup = main_page_scrapper(main_page_html)

    print('>>> Getting page links for each athlete\n')
    
    fighters_links = get_fighters_page_link(soup, fighter_page_url)

    t1 = datetime.now()
    scrapper = WebScraper(urls = fighters_links)

    print(f'>>> Downloaded completed')
    print(f'>>> Data scrapping started')

    fighters_list = fighters_page_scrapper_html(scrapper.master_dict, fighters_links)

    t2 = datetime.now()
    scrapping_time = t2 - t1
    print(f'>>> Data scrapping took {scrapping_time.seconds} seconds')

if __name__ == '__main__':
    main()