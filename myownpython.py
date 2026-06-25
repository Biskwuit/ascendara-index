import cloudscraper
from bs4 import BeautifulSoup
import time
from tqdm import tqdm

BASE_URL = "https://steamrip.com"

scraper = cloudscraper.create_scraper()

games_list_page = scraper.get(f"{BASE_URL}/games-list-page/").text
games_list_soup = BeautifulSoup(games_list_page, 'html.parser')

# games_list_urls = games_list_soup.find("li", {"class": "az-list-item"}).find("a").get('href')

# game_page = scraper.get(BASE_URL + games_urls).text
# game_soup = BeautifulSoup(game_page, 'html.parser')

# game_name = game_soup.title.get_text().split('Free Download', 1)[0]

# line = '-' * (len(game_name) + 2)

# print(f'\n{line}')
# print(f' {game_name}')
# print(f'{line}\n')

#for links in game_soup.find_all("a", string="DOWNLOAD HERE"):
#    print('https:' + links.get('href'))

itterations = 0
counter = 0

# for game_url in games_soup.find_all("li", {"class": "az-list-item"}):
#     # print(f'{BASE_URL}{game_url.find("a").get("href")}')
#     game_page = scraper.get(f'{BASE_URL}{game_url.find("a").get("href")}').text
#     counter = counter + 1
#     game_soup = BeautifulSoup(game_page, 'html.parser')

#     game_name = game_soup.title.get_text().split('Free Download', 1)[0]


#     line = '-' * (len(game_name) + 2)

#     print(f'\n{line}')
#     print(f' {game_name}')
#     print(f'{line}\n')

#     for links in game_soup.find_all("a", string="DOWNLOAD HERE"):
#        print('https:' + links.get('href'))

#     itterations = itterations + 1
#     if itterations == 20:
#         time.sleep(10)
#         itterations = 0

def games_pages():
    global counter
    global game_url
    for game_url in games_list_soup.find_all("li", {"class": "az-list-item"}):
        counter = counter + 1

games_pages()
print(counter)

for i in tqdm(range(counter)):
    for game_url in games_list_soup.find_all("li", {"class": "az-list-item"}):
        game_page_url = scraper.get(f'{BASE_URL}{game_url.find("a").get("href")}').text
        game_page_soup = BeautifulSoup(game_page_url, 'html.parser')
        game_name = game_page_soup.title.get_text().split('Free Download', 1)[0]
        line = '-' * (len(game_name) + 2)
        with open("game_list.txt", "a") as file:
            file.write(f'\n{line}')
            file.write(f' {game_name}')
            file.write(f'{line}\n')
        for links in game_page_soup.find_all("a", string="DOWNLOAD HERE"):
            with open("game_list.txt", "a") as file:
                file.write('https:'+str(links.get('href'))+' ')
        itterations = itterations + 1
        if itterations == 20:
            time.sleep(10)
            itterations = 0