from bs4 import BeautifulSoup
import requests
import urllib.request
import scrapy
import pymysql
import datetime

class BrickSetSpider(scrapy.Spider):
    def __init__(self):
        print('Rodando BrickSetSpider...')
        self.datetimenow = datetime.datetime.now()
        self.datenow = datetime.date.today()
        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='quotes',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    name = "ubot_spider"
    start_urls = ['http://brickset.com/sets/year-2016']

    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'h1 ::text'
            NAME_SELECTOR = 'h1 a ::text'
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            IMAGE_SELECTOR = 'img ::attr(src)'
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
                'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
                'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
                'image': brickset.css(IMAGE_SELECTOR).extract_first(),
            }

            NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
            next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
            if next_page:
                yield scrapy.Request( # Ei, rastreie esta página.
                    response.urljoin(next_page),
                    callback=self.parse # Uma vez que você tenha obtido o HTML desta página, retorne-o para este método para que possamos analisá-lo, extrair os dados e encontrar a próxima página.
                )

    def getDolarValue(self):
        content = requests.get("https://dolarhoje.com/").text
        content = str(content)
        find = '<input type="text" id="nacional" value="'
        posicao = int(content.index(find) + len(find)) # content.index retorna o índice onde ocorre pela primeira vez a string passada por parâmetro
        dolar = content[posicao: posicao + 4]
        return dolar

    def getEuroValue():
        content = urllib.request.urlopen("https://www.melhorcambio.com/euro-hoje").read()
        content = str(content)
        find = '<input type="text" id="nacional" value="'
        posicao = int(content.index(find) + len(find))
        euro = content[posicao: posicao + 4]
        print("Euro: " + euro)

    def run(self):
        print('Rodando metódo run...')
        dolar = self.getDolarValue()
        self.saveDolarData(dolar)
        print("Dolar: " + dolar)

    def getTimeNow():
    # content = urllib.request.urlopen("https://www.climatempo.com.br/previsao-do-tempo/cidade/88/goiania-go").read()
    content = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/88/goiania-go").text
    content = str(content)
    print(content)
    find = 'xima">'
    posicao = int(content.index(find) + len(find))
    maxima = content[posicao: posicao + 2]

    def saveDolarData(self, dolarQuote):
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `dolar` (`quote`, `now`) VALUES (%s ,%s)"
                cursor.execute(sql, (str(dolarQuote), self.datenow))
                self.connection.commit()

            # with connection.cursor() as cursor:
            #     sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            #     cursor.execute(sql, ('webmaster@python.org',))
            #     result = cursor.fetchone()
            #     print(result)
        finally:
            self.connection.close()


spider = BrickSetSpider()
# spider.saveDolarData()
spider.run()


#

#
#     find = 'nima">'
#     posicao = int(content.index(find) + len(find))
#     minima = content[posicao: posicao + 2]
#     print("Temp. Maxima: " + maxima)
#
#
# def extract_title(content):
#     soup = BeautifulSoup(content, "lxml")
#     tag = soup.find("title", text=True)
#
#     print(tag)
#
#     if not tag:
#         return None
#
#     return tag.string.strip()
#
# def extract_links(content):
#     soup = BeautifulSoup(content, "lxml")
#     links = set()
#
#     for tag in soup.find_all("a", href=True):
#         if tag["href"].startswith("http"):
#             links.add(tag["href"])
#
#     return links
#
# def showLinksTest():
#     page = requests.get("https://www.python.org/")
#     links = extract_links(page.text)
#
#     for link in links:
#         print(link)
#
# def crawl(start_url):
#     seen_urls = set([start_url])
#     available_urls = set([start_url])
#
#     while available_urls:
#         url = available_urls.pop()
#
#         try:
#             content = requests.get(url, timeout=3).text
#             # content = requests.get(url).text
#         except Exception:
#             continue
#
#         title = extract_title(content)
#
#         if title:
#             print(title)
#             print(url)
#             print()
#
#         for link in extract_links(content):
#             if link not in seen_urls:
#                 seen_urls.add(link)
#                 available_urls.add(link)
#
# def startCrawler():
#     try:
#         crawl("https://www.python.org")
#     except KeyboardInterrupt:
#         print()
#         print("Bye!")
#
# startCrawler()
# getDolarValue()
# getTimeNow()
# getEuroValue()