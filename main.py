'''
This script logs into videoblocks account and then redirects to all folders

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys

driver = webdriver.Chrome()

driver.get('http://www.videoblocks.com/login/')

email = driver.find_element_by_id('login-email')
passwd = driver.find_element_by_id('login-password')

#before testing just add the username and password
email.send_keys()
passwd.send_keys()

passwd.send_keys(keys.RETURN)



check_login = True

while(check_login):
    if('Folder - VideoBlocks' in driver.title):
        check_login = False
    else:
        driver.get('http://www.videoblocks.com/member/bins/')



'''gets all the folder names in a list '''

save_source = driver.page_source

links = []

count = 1

while(count > -1 ):
	count = save_source.find('<a href="/member/bin/view/')
	if(count != -1):
		ind = count + 9
		ind2 = save_source[ind:].find('"')
		ind2 = ind + ind2
		links.append(save_source[ind:ind2])
		save_source = save_source[ind2:]

for index, item in enumerate(links):
	item = "http://www.videoblocks.com" + item
	links.remove(links[index])
	links.insert(index, item)
