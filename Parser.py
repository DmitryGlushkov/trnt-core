import urllib.request
import os
from bs4 import BeautifulSoup
from core import TScraper
import platform

print(platform.architecture()[0])

print('start')
print(os.environ['PATH'])
print(os.environ['Path'])


"""
with urllib.request.urlopen(url) as response:
    content_type = response.getheader('Content-Type')
    charset = content_type[content_type.find('charset=') + 8:]
    data = response.read().decode(charset)
    soup = BeautifulSoup(data)
    list = soup.find('tr', {'class': 'hl-tr'})
    #for item in list:

    print(1)
"""