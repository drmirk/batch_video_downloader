from selenium import webdriver
driver = webdriver.Chrome("/home/ibrahim/Downloads/chromedriver")
page = "file:///media/ibrahim/Primary/Users/mdibr/Desktop/tet/My%20Folder%20-%20VideoBlocks.html"

driver.get(page)

full_page = driver.page_source

links = ['test']

full_page.find()