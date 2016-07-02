#import selenium webdriver
from selenium import webdriver

#created
driver = webdriver.Chrome()
page = "file:///F:/python/videoblocks/My%20Folder%20-%20VideoBlocks.html"

driver.get(page)

download_links = driver.find_elements_by_xpath(".//*[@id='cool-new-btn']")

download_links.click()

download_btn = driver.find_element_by_xpath(".//*[@id='ssw-table']/tbody/tr[1]/td[6]/div/div/ul/li[1]")

    
download_btn.click()