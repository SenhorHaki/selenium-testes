from selenium import webdriver	
from time import sleep

def login():	
	login_input = navegador.find_element_by_xpath('//html/body/div/div/main/div/div[1]/div/div/div/div/div/div/form/div[1]/input')
	login_input.send_keys('tester@geniantis.com')
	pass_input = navegador.find_element_by_xpath('/html/body/div/div/main/div/div[1]/div/div/div/div/div/div/form/div[2]/input')
	pass_input.send_keys('tester123ricardo')
	bl= navegador.find_element_by_xpath('/html/body/div/div/main/div/div[1]/div/div/div/div/div/div/form/div[3]/div[1]/button')
	bl.click()

navegador = webdriver.Chrome()
navegador.get('http://homolog.geniants.com') 
sleep(1)
login()
login()
sleep(2.9)
navegador.get('https://homolog.geniants.com/#/conteudos')
sleep(2)
C_c = navegador.find_element_by_xpath('/html/body/div/div/main/div/div[1]/div[5]/a')
C_c.click()
sleep(3)
C_x =navegador.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/header/button')
C_x.click()
sleep(2)
navegador.quit()