import cloudscraper
from bs4 import BeautifulSoup

BASE_URL = "https://steamrip.com"

scraper = cloudscraper.create_scraper()

games_page = scraper.get(f"{BASE_URL}/games-list-page/").text
games_soup = BeautifulSoup(games_page, 'html.parser')

games_urls = games_soup.find("li", {"class": "az-list-item"}).find("a").get('href')

game_page = scraper.get(BASE_URL + games_urls).text
game_soup = BeautifulSoup(game_page, 'html.parser')

game_name = game_soup.title.get_text().split('Free Download', 1)[0]

line = '-' * (len(game_name) + 2)

print(f'\n{line}')
print(f' {game_name}')
print(f'{line}\n')

#for links in game_soup.find_all("a", string="DOWNLOAD HERE"):
#    print('https:' + links.get('href'))
    
for game_url in games_soup.find_all("li", {"class": "az-list-item"}):
    print(f'{BASE_URL}{game_url.find("a").get("href")}')