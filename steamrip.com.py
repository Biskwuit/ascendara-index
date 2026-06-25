import cloudscraper
from bs4 import BeautifulSoup
import json

BASE_URL = "https://steamrip.com"

scraper = cloudscraper.create_scraper()

def scrap(url):
    return BeautifulSoup(scraper.get(url).text, 'html.parser')

games_list_page = scrap(f'{BASE_URL}/games-list-page/')

games = []

for game_page_url in games_list_page.find_all("li", {"class": "az-list-item"}):
    print(f'{game_page_url.find("a").string}')
    print(f'{BASE_URL}{game_page_url.find("a").get("href")}')

    games.append({
        "game": game_page_url.find("a").string,
        "link": BASE_URL + game_page_url.find("a").get("href")
    })

    with open('data.json', 'w') as jfile:
        json.dump(games, jfile)