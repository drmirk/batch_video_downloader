'''
This script logs into videoblocks account and then redirects to all folders

'''
def login():
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys as keys
	driver = webdriver.Chrome()
	driver.get('http://www.videoblocks.com/login/')
	email = driver.find_element_by_id('login-email')
	passwd = driver.find_element_by_id('login-password')
	##before login just insert email and passowrd
	email.send_keys()
	passwd.send_keys()
	passwd.send_keys(keys.RETURN)
	check_login = True
	while(check_login):
	    if('Folder - VideoBlocks' in driver.title):
	        check_login = False
	    else:
	        driver.get('http://www.videoblocks.com/member/bins/')
