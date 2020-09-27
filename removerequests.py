from time import sleep
from selenium import webdriver
import getpass 
import csv

def Login():	
	print("Username:", end="")
	username = str(input())
	pas = getpass.getpass() 
	browser = webdriver.Firefox(executable_path=r'C:\Users\HP\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\selenium\webdriver\firefox\geckodriver.exe')
	browser.get('https://www.linkedin.com/login')
	sleep(4)

	name = browser.find_element_by_xpath('//*[@id="username"]')
	name.send_keys(username)

	password = browser.find_element_by_xpath('//*[@id="password"]')
	password.send_keys(pas)

	sleep(3)
	try:
		signin = browser.find_element_by_xpath('/html/body/div/main/div[2]/form/div[3]/button') 
	except:
		signin = browser.find_element_by_xpath('/html/body/div/main/div[2]/form/div[4]/button') 
	signin.click()
	if not signin:
		return 
	print('signin Complete')
	sleep(5)	
	Total = 0
	page = 'https://www.linkedin.com/mynetwork/invitation-manager/sent/?invitationType=&page=1'
	browser.get(page)
	sleep(2)
	for i in range(1,100):
		sleep(1)
		try:
			browser.find_element_by_xpath('/html/body/div[8]/div[3]/div/div/div/div/div/div/section/div[2]/div[2]/ul/li['+str(i)+']/div/div[2]/button').click()
			sleep(1)
			browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
			print('pass - '+str(i))
			Total += 1
			sleep(2)
		except:
			print('Fail - '+str(i))
			# fail += 1
			pass
		browser.execute_script("window.scrollTo(0, 150)")
	print('Total Success: '+str(Total))
Login()
