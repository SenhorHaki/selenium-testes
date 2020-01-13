from selenium import webdriver
from time import sleep
#------------#

navegador = webdriver.Chrome()
navegador.get('http://www.infordu.com')
sleep(1)
#sleep(3)
login_input = navegador.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/label/input')
login_input.send_keys('admin')
pass_input = navegador.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/label/input')
pass_input.send_keys('admin')
bl= navegador.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div[1]/button')
bl.click()
while (True):
	sleep(1)
	#print(navegador.current_url)
	if navegador.current_url == 'http://www.infordu.com/#/home':
		sleep(1)
		bk = navegador.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div[3]/button')			
		bk.click()
		sleep(1)
		login_input = navegador.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/label/input')
		login_input.send_keys('admin')
		pass_input = navegador.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/label/input')
		pass_input.send_keys('admin')
		sleep(1)
		bl= navegador.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div[1]/button')
		bl.click()

			#navegador.quit()
			#break