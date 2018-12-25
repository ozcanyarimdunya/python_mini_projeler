import records
import requests
from bs4 import BeautifulSoup


class RealPython(object):
    db = records.Database('sqlite:///database.db')

    def __init__(self):
        self.db.query(
            """DROP TABLE IF EXISTS TUTORIAL"""
        )
        self.db.query(
            """CREATE TABLE IF NOT EXISTS TUTORIAL (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT
                    , IMAGE TEXT
                    , URL TEXT
                    , TITLE TEXT
                )"""
        )

    def insert(self, image, url, title):
        self.db.query(
            """INSERT INTO TUTORIAL (IMAGE, URL, TITLE) VALUES (:image, :url, :title)"""
            , image=image
            , url=url
            , title=title
        )

    def scrap(self):
        base_url = "https://realpython.com"
        html = requests.get(base_url).content
        soup = BeautifulSoup(html, 'html.parser')

        main_content = soup.find("div", {"class": "main-content"})
        tutorials = main_content.find_all("div", {"class": "col-12 col-md-6 col-lg-4 mb-5"})

        for tut in tutorials:
            image = tut.find('img').attrs.get('src')
            url = base_url + tut.find('a').attrs.get('href')
            title = tut.find('h2', {"class": "card-title"}).text

            self.insert(image=image, url=url, title=title)

    def print(self):
        all_data = self.db.query(
            """SELECT * FROM TUTORIAL"""
        )

        for row in all_data:
            print(row)


r = RealPython()
r.scrap()
r.print()
