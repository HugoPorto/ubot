from bs4 import BeautifulSoup

import requests

import urllib.request

import scrapy

import pymysql

import datetime

from urllib.request import urlopen

from load import Load

class BrickSetSpider(scrapy.Spider):
    database = False
    
    method = 1
    
    def __init__(self, name, database, method):
        self.datetimenow = datetime.datetime.now()
        
        self.datenow = datetime.date.today()
        
        if(database):
            self.connection = pymysql.connect(
                                host='',
                                user='',
                                password='',
                                db='',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
            
        self.name = name
        
        self.method = method

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
        
        posicao = int(content.index(find) + len(find))
        
        dolar = content[posicao: posicao + 4]
        
        return dolar

    def getEuroValue(self):
        content = urllib.request.urlopen("https://www.melhorcambio.com/euro-hoje").read()
        
        content = str(content)
        
        find = '<input type="text" id="nacional" value="'
        
        posicao = int(content.index(find) + len(find))
        
        euro = content[posicao: posicao + 4]
        
        return euro

    def run(self):
        if(self.method == 1):
            valor_dolar = self.getDolarValue()
            
            print("Dolar: " + valor_dolar)
            
        elif(self.method == 2):
            valor_euro = self.getEuroValue()
            
            print("Euro: " + valor_euro)
            
        elif(self.method == 3):
            self.getSimpleTitle()
            
        elif(self.method == 4):
            self.getDolarTwo()

    def getTimeNow():
        content = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/88/goiania-go").text
        
        content = str(content)
        
        find = 'xima">'
        
        posicao = int(content.index(find) + len(find))
        
        maxima = content[posicao: posicao + 2]
        
        find = 'nima">'
        
        posicao = int(content.index(find) + len(find))
        
        minima = content[posicao: posicao + 2]
        
        print("Temp. Maxima: " + maxima)

    def saveDolarData(self, dolarQuote):
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `core_dolar` (`quote`, `now`) VALUES (%s ,%s)"
                
                cursor.execute(sql, (str(dolarQuote), self.datenow))
                
                self.connection.commit()
        finally:
            self.connection.close()

    def searchSimple(self):
        html = urlopen('http://pythonscraping.com/pages/page1.html')
        
        bs = BeautifulSoup(html.read(), 'html.parser')
        
        print(bs.body)
        
    def getSimpleTitle(self):
        html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
        
        bs = BeautifulSoup(html, "html.parser")
        
        nameList = bs.findAll('span', {'class': 'green'})
        
        for name in nameList:
            print(name.get_text())
            
    def getDolarTwo(self):
        html = urlopen('https://dolarhoje.com/')
        
        bs = BeautifulSoup(html, "html.parser")
        
        dolar = bs.find('input', {'id':'nacional'})
        
        print(dolar['value'])