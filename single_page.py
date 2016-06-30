from selenium import webdriver
import re

driver = webdriver.Chrome()
page = "file:///F:/python/videoblocks/My%20Folder%20-%20VideoBlocks.html"

driver.get(page)

classes = driver.find_element_by_id("cool-new-btn")



from selenium.webdriver.common.keys import Keys as keys

classes.click()
