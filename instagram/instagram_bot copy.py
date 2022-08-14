from webbrowser import get
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint
import os

chromedrive_path = os.getcwd() + os.sep + 'chromedriver.exe'

webdriver = webdriver.Chrome(executable_path=chromedrive_path)

sleep(2)

webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

sleep(2)

webdriver.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys("ivanpadalecki005")

sleep(2)

webdriver.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys("thuh@R67Yuj")

sleep(2)

botao_de_login = webdriver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

sleep(10)

webdriver.find_element(By.XPATH, "//button[contains(text(), 'Agora não')]").click()

sleep(5)

webdriver.find_element(By.XPATH, "//button[contains(text(), 'Agora não')]").click()

hashtag_lista = ['python', 'setups', 'nba']

novos_usuarios_seguidos = []

tag = -1

seguindo = 0

likes = 0

comentarios = 0
    
sleep(3)

for hashtag in hashtag_lista:
    
    tag = tag + 1
    
    webdriver.get('https://www.instagram.com/explore/tags/' + hashtag_lista[tag] + '/')

    sleep(10)

    primeira_thumb = webdriver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a")
    
    primeira_thumb.click()
    
    sleep(randint(2, 3))
    
    try:
        for _ in range(1, 3):
            
            usuario = webdriver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/span/a").text
            
            if usuario not in novos_usuarios_seguidos:
                
                if webdriver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button").text == 'Seguir':
                    
                    webdriver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button").click()
                    
                    novos_usuarios_seguidos.append(usuario)
                    
                    seguindo = seguindo + 1
                    
                    like = webdriver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button").click()
                    
                    likes = likes + 1
                    
                    sleep(randint(2, 3))
                    
                    comentario = webdriver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[3]/div/div/section[1]/span[2]/button").click()
                    
                    comment_box = webdriver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[3]/div/div/section[3]/div/form/textarea").click()
                    
                    sleep(randint(2, 3))
                    
                    com = randint(1,10)
                    
                    if com < 6:
                        
                        comment_box.send_keys('Muito Legal!')
                        
                        sleep(2)
                        
                    elif com > 5 and com < 9:
                        
                        comment_box.send_keys('Bom Trabalho!')
                        
                        sleep(2)
                        
                    elif com  == 9:
                        
                        comment_box.send_keys('Irado!')
                        
                        sleep(2)
                        
                    elif com  == 10:
                        
                        comment_box.send_keys('Irado!')
                        
                        sleep(2)
            
                    comment_box.send_keys(Keys.ENTER)
                    
                    comentarios = comentarios + 1
                    
                    sleep(randint(5))
                    
                webdriver.find_element(By.LINK_TEXT, 'Próximo').click()
                
                sleep(randint(2,3))
                
            else:
                
                webdriver.find_element(By.LINK_TEXT, 'Próximo').click()
                
                sleep(randint(2,3))
    except:
        
        continue

print('Liked {} fotos.'.format(likes))

print('Comentários {} fotos.'.format(comentarios))

print('Seguindo {} pessoas novas.'.format(seguindo))