from webbrowser import get
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
from selenium.common.exceptions import NoSuchElementException

class Test:
    def test_companys(self):
        chrome_options = self.set_options_webdriver()
        
        chromedrive_path = os.getcwd() + os.sep + 'libs' + os.sep + 'chromedriver.exe'

        self.webdriver = webdriver.Chrome(executable_path=chromedrive_path, options=chrome_options)
        
        self.webdriver.set_window_size(1024, 800)

        sleep(2)

        self.webdriver.get('http://localhost:8765/')

        sleep(2)

        self.webdriver.find_element(By.ID, "login").click()

        sleep(2)

        try:
            self.webdriver.find_element(By.ID, "email-login").send_keys("victor@email.com")
            print('Obtendo id do campo e-mail...')
        except NoSuchElementException :
            print('Erro ao obter id do campo login...')
            exit()
            
        sleep(2)

        try:
            self.webdriver.find_element(By.ID, "password-login").send_keys("123")
            print('Obtendo id do campo password...')
        except NoSuchElementException :
            print('Erro ao obter id do campo password...')
            exit()

        sleep(2)

        try:
            self.webdriver.find_element(By.ID, "signin").click()
            print('Obtendo id do botão signin...')
        except NoSuchElementException :
            print('Erro ao obter id do botão de login...')
            exit()

        sleep(2)

        try: 
            self.webdriver.find_element(By.XPATH, "/html/body/div/aside[1]/div/nav/ul/li[1]/a").click()
            print('Obtendo caminho para o botão que abre a lista de links de empresas...')
        except NoSuchElementException :
            print('Erro ao obter caminho para o botão que abre a lista de links do item empresas...')
            exit()
            
        sleep(2)

        try:
            self.webdriver.find_element(By.XPATH, "/html/body/div/aside[1]/div/nav/ul/li[1]/ul").click()
            print('Obtendo caminho para o link empresas...')
        except NoSuchElementException :
            print('Erro ao obter o caminho para o botão que lista as empresas...')
            exit()

        sleep(2)

        try:
            self.webdriver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div/a").click()
            print('Obtendo caminho para o botão adicionar...')
        except NoSuchElementException :
            print('Erro ao obter caminho para o botão de adicionar nova empresa...')
            exit()
            
        sleep(2)

        try :
            self.webdriver.find_element(By.ID, "company").send_keys("Selenium")
            print('Obtendo caminho para o input do nome da empresa...')
        except NoSuchElementException :
            print('Erro ao obter caminho para o input company no form de empresas...')
            exit()
            
        sleep(2)

        try :
            self.webdriver.find_element(By.ID, "photo").send_keys("C://Users/Hugo/Documents/Focux/Logo.png")
            print('Setando a logomarca da empresa no input da foto (logomarca) da empresa...')
        except NoSuchElementException :
            print('Erro ao obter caminho para o input photo no form de empresas...')
            exit()
            
        sleep(2)

        try :
            self.webdriver.find_element(By.ID, "email").send_keys("victor.porto7@gmail.com")
            print('Obtendo id para o campo e-mail...')
        except NoSuchElementException :
            print('Erro ao obter caminho para o input email no form de empresas...')
            exit()
            
        sleep(2)

        try :
            self.webdriver.find_element(By.ID, "phone").send_keys("91984744021")
            print('Obtendo id para o campo telefone...')
        except NoSuchElementException :
            print('Erro ao obter caminho para o input phone no form de empresas...')
            exit()
            
        sleep(2)

        try :
            self.webdriver.find_element(By.ID, "fiscal-number").send_keys("123")
            print('Obtendo id para o campo npumero e fiscal e setando o mesmo...')
        except NoSuchElementException :
            print('Erro ao obter caminho para o input fiscal-number no form de empresas...')
            exit()
            
        sleep(2)

        try :
            self.webdriver.find_element(By.ID, "address").send_keys("Teste")
            print('Obtendo id e setando o campo endereço...')
        except NoSuchElementException :
            print('Erro ao obter caminho para o input address no form de empresas...')
            exit()
            
        sleep(2)

        try :
            self.webdriver.find_element(By.ID, "cep").send_keys("68600000")
            print('Obtendo id e setando o campo cep...')
        except NoSuchElementException :
            print('Erro ao obter caminho para o input cep no form de empresas...')
            exit()
            
        sleep(2)

        try :
            self.webdriver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[2]/div[2]/div[3]/span/span[1]/span/span[2]/b").click()
            print('Clicando no botão que abre o select2...')
        except NoSuchElementException :
            print('Erro ao obter caminho para o caminho do botão que abre o slect2 para o item cidadeno form de empresas...')
            exit()
            
        sleep(2)

        try :
            self.webdriver.find_element(By.CLASS_NAME, "select2-search__field").click()
            print('Clicando no search do campo que usa o select2...')
        except NoSuchElementException :
            print('Erro ao obter caminho para o search input do select de cidade no form de empresas...')
            exit()
            
        sleep(2)

        try :
            self.webdriver.find_element(By.CLASS_NAME, "select2-search__field").send_keys("Alegre")
            print('Setando uma opção no campo que usa o select2...')
        except NoSuchElementException :
            print('Erro ao obter caminho para o search input do select de cidade no form de empresas...')
            exit()
            
        sleep(2)

        try :
            self.webdriver.find_element(By.XPATH, "/html/body/span/span/span[2]/ul/li[1]").click()
            print('Clicando na cidade escolhida...')
        except NoSuchElementException :
            print('Erro ao obter caminho para o item onde é possível selecionar a cidade escolhida no select cidade do form de empresas...')
            exit()
            
        sleep(3)

        try :
            self.webdriver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/form/button").click()
            print('Adicionando empresa...')
        except NoSuchElementException :
            print('Erro ao obter caminho para o botão adicionar no form de empresas...')
            exit()
            
        print('Empresa adicionada com sucesso...')

    def set_options_webdriver(self):
        chrome_options = Options()
        
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        chrome_options.add_argument('--lang=pt-BR')
        
        chrome_options.add_argument('--disable-notifications')
        
        chrome_options.add_argument("headless")
        
        return chrome_options
    
run_test = Test()
run_test.test_companys()