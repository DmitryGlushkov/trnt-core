import urllib.request
import pgdb

main_url = 'https://rutracker.org/forum/viewforum.php?f='


def scrap_topic(id):
    pass


def scrap_forum(id):
    print('start scrap_forum')
    _sc = ForumScraper()
    _sc.start(id)


class ForumScraper:

    def __init__(self):
        print('TScraper init')
        self.connection = pgdb.connect(host='localhost', user='sg', password='sg', database='t_data')

    def do_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        for d in cursor.fetchall():
            print('result: ' + str(d))

    def start(self, forum_id):
        url = main_url + forum_id
        with urllib.request.urlopen(url) as response:
            data = response.read()
