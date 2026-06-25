import cloudscraper

scraper = cloudscraper.create_scraper()

page = scraper.get("https://steamrip.com/ace-attorney-investigations-collection-free-download/").text

with open("templates/index.html", "w") as file:
    file.write(page)