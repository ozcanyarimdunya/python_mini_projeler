"""
In this project we trying to use
    - records   (https://github.com/kennethreitz/records)
    - requests  (https://github.com/requests/requests)
    - bs4       (https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html)
modules.

records : Records is a very simple, but powerful, library for making raw SQL queries to most relational databases.
requests: Requests is the only Non-GMO HTTP library for Python, safe for human consumption.
bs4     : Beautiful Soup is a Python library for pulling data out of HTML and XML files.


We will scrap the image, url and title from 'https://realpython.com' then save it to database.db

To scrap required data from website we will download 'https://realpython.com' home page html file. We will user
records in this case. After downloading html page then we will scrap data from html file with bs4. And finally we will
save it to database. We will use records in here to create a database and insert data.
"""

import records
import requests
from bs4 import BeautifulSoup


class RealPython:
    # create a main database object, a live connection
    db = records.Database('sqlite:///database.db')
    base_url = "https://realpython.com"

    def __init__(self):
        """
        Initialise method RealPython class
        :return: None
        """
        # check if table already exists, if yes then delete it
        self.db.query(
            """DROP TABLE IF EXISTS TUTORIAL"""
        )

        # check if table exists. if not then create new one
        self.db.query(
            """CREATE TABLE IF NOT EXISTS TUTORIAL (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT
                    , IMAGE TEXT
                    , URL TEXT
                    , TITLE TEXT
                )"""
        )

    def insert(self, image, url, title):
        """
        Insert data into database
        :param image: Each item's thumbnail
        :param url: Each item's url link
        :param title: Each item's title
        :return: None
        """
        self.db.query(
            """INSERT INTO TUTORIAL (IMAGE, URL, TITLE) VALUES (:image, :url, :title)"""
            , image=image
            , url=url
            , title=title
        )

    def scrap(self):
        """
        Scrap data from website and insert it to database
        :return: None
        """
        html = requests.get(self.base_url).content
        soup = BeautifulSoup(html, 'html.parser')

        main_content = soup.find("div", {"class": "main-content"})
        tutorials = main_content.find_all("div", {"class": "col-12 col-md-6 col-lg-4 mb-5"})

        for tut in tutorials:
            image = tut.find('img').attrs.get('src')
            url = self.base_url + tut.find('a').attrs.get('href')
            title = tut.find('h2', {"class": "card-title"}).text

            self.insert(image=image, url=url, title=title)

    def print(self):
        """
        Select all data from database then print it row by row
        :return: None
        """
        all_data = self.db.query(
            """SELECT * FROM TUTORIAL"""
        )

        for row in all_data:
            print(
                """
                ID      : {id},
                IMAGE   : {image},
                URL     : {url},
                TITLE   : {title}  
                """.format(
                    id=row["ID"],
                    image=row["IMAGE"],
                    url=row["URL"],
                    title=row["TITLE"]
                )
            )


# create an instance of RealPython class
rp = RealPython()

# run scrap method
rp.scrap()

# print method
rp.print()

# Output
"""

ID      : 1,
IMAGE   : https://files.realpython.com/media/PEP-8-Tutorial-Python-Code-Formatting-Guide_Watermarked.9103cf7be328.jpg,
URL     : https://realpython.com/python-pep8/,
TITLE   : How to Write Beautiful Python Code With PEP 8  


ID      : 2,
IMAGE   : https://files.realpython.com/media/A-Pythonistas-Holiday-Wish-List_Watermarked.bdc9b573f669.jpg,
URL     : https://realpython.com/python-holiday-wish-list/,
TITLE   : A Pythonista's Holiday Wish List  


ID      : 3,
IMAGE   : https://files.realpython.com/media/Python-Development-in-Thonny---In-Depth_Watermarked.411337d5c6ec.jpg,
URL     : https://realpython.com/python-thonny/,
TITLE   : Thonny: The Beginner-Friendly Python Editor  


ID      : 4,
IMAGE   : https://files.realpython.com/media/A-Community-Interview_Blue.4a0c9c3f9e33.jpg,
URL     : https://realpython.com/interview-brian-peterson/,
TITLE   : Python Community Interview With Brian Peterson  


ID      : 5,
IMAGE   : https://files.realpython.com/media/Sending-Emails-With-Python_Watermarked.6fee62c5f3b9.jpg,
URL     : https://realpython.com/python-send-email/,
TITLE   : Sending Emails With Python  

...
...
...

"""
