import os
import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class WebScraping : 
    def __init__(self) :
        chrome_options = Options()
        
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        chrome_options.add_argument('--lang=pt-BR')
        
        chrome_options.add_argument('--disable-notifications')
        
        chromedrive_path = os.getcwd() + os.sep + 'libs' + os.sep + 'chromedriver.exe'

        self.webdriver = webdriver.Chrome(executable_path=chromedrive_path, options=chrome_options)
        
    def iniciar(self):
        self.proxima_pagina = 1 