from bjj_data_scrapping import *

main_page_url = 'https://www.bjjheroes.com/a-z-bjj-fighters-list'
fighter_page_url = 'https://www.bjjheroes.com/bjj-fighters{}'
fighters_folder = 'fighters'
filename = 'bjj_fighters.html'

def main():
    get_page_html(main_page_url, filename)

    print('>>> Processo iniciado\n\n')

    soup = main_page_scrapper(filename)

    print('>>> Extraindo dados das páginas dos atletas\n')
    
    fighters_links = get_fighters_page(soup)

    check_folder(fighters_folder)

    print('>>> Ínicio da carga de dados dos atletas\n')

    fighters_page_scrapper(fighters_links, fighter_page_url, fighters_folder)


if __name__ == '__main__':
    main()