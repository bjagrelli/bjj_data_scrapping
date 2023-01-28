from bjj_data_scrapping import *

main_page_url = 'https://www.bjjheroes.com/a-z-bjj-fighters-list'
fighter_page_url = 'https://www.bjjheroes.com/bjj-fighters{}'
fighters_folder = 'fighters'
filename = 'bjj_fighters.html'

def main():
    
    get_page_html(main_page_url, filename)

    print('>>> Beginning of process\n')

    soup = main_page_scrapper(filename)

    print('>>> Getting page links for each athlete\n')
    
    fighters_links = get_fighters_page_link(soup)

    check_folder(fighters_folder)

    print('>>> Starting data scrapping for each athlete \n')

    fighters_page_scrapper_html(fighters_links, fighter_page_url, fighters_folder)


if __name__ == '__main__':
    main()