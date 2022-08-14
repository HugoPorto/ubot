"""
from urllib.request import urlopen
html = urlopen('http://pythonscraping.com/pages/page1.html')
print(html.read())
"""

"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)
"""

"""
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen("https://pythonscrapingthisurldoesnotexist.com")
except HTTPError as e:
    print("The server returned an HTTP error")
except URLError as e:
    print("The server could not be found!")
else:
    print(html.read())
"""


from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    except URLError as e:
        print("O servidor não pôde ser encontrado!")
        return None
    else:
        try:
            bsObj = BeautifulSoup(html.read(), "lxml")
            title = bsObj.body.h1
            
        except AttributeError as e:
            print("A tag não pôde ser encontrada")
            return None
        else:
            return title

title = getTitle("http://www.pythonscraping.com/pages/page1.html")

if title == None:
    print("Title could not be found")
else:
    print(title)