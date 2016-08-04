emailAddress = ""
password = ""
folderAddress = "https://www.videoblocks.com/member/bin/view/sm6ixOhPr0CYQlV4qRyaC9Iey"
pageNumber = "2"


########################################################
########################################################
########################################################

def startDownload():
    ## Imported selenium webdriver and time module
    ## and OS module

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys as keys
    import time
    import os

    ## used chrome as primary browser
    ## store the chrome app in a place and show the path

    ##driver = webdriver.Chrome("/home/ibrahim/Downloads/chromedriver")             ## for linux
    driver = webdriver.Chrome()
    ## driver.maximize_window()                                                     ## for windows
    
    ## visit videoblocks login site and select both email and passwor field
    check = True
    while(check):
        if(driver.title == "Login - VideoBlocks"):
            email = driver.find_element_by_id('login-email')
            passwd = driver.find_element_by_id('login-password')
            ## entered both email and password from GUI
            email.send_keys(emailAddress)
            passwd.send_keys(password)
            passwd.send_keys(keys.RETURN)
            check = False
        else:
            driver.get('http://www.videoblocks.com/login/')


    ## redirect to the download folder
    check = True
    while(check):
        if(driver.title == "Members Dashboard - VideoBlocks"):
            driver.get(folderAddress)
            check = False
        else:
            time.sleep(2)
            
    
    ## redirects to the final donwload page
    check = True
    time.sleep(5)
    while(check):
        if(driver.title == "My Folder - VideoBlocks"):
            page_btn = driver.find_element_by_link_text(pageNumber)
            page_btn.click()
            check = False
        else:
            time.sleep(2)


    ## check to page load and find all the videos download links
    check = True
    time.sleep(5)
    go_up = driver.find_element_by_xpath("/html/body")
    go_up.send_keys(keys.HOME)
    time.sleep(1)
    while(check):
        if(driver.title == "My Folder - VideoBlocks"):
            download_links = driver.find_elements_by_xpath("//*[@id='cool-new-btn']")
            ## i_dont_know = len(download_links)
            check = False
        else:
            time.sleep(2)

    ## iterate through each links and create a xpath
    ## then press the first link
    tableRow = 0
    for links in download_links:        
        tableRow = tableRow + 1
        ## completely load a page
        check = True
        while(check):
            ## check if there is any unfinished chrome download in the download directory
            ## if there are less than 4 unfinished chrome download, only then clicks the download button
            crDownload = 0
            allDir = os.listdir("C:\\Users\\mdibr\\Downloads")
            for files in allDir:
                if(files[-11:] == ".crdownload"):
                    crDownload = crDownload + 1

            ## checks the page is loaded and also number of active download is less than 4
            if((driver.title == "My Folder - VideoBlocks") and (crDownload < 6)):
                links.click()
                time.sleep(3)
                check = False
            else:
                time.sleep(5)
        topXPATH = "//*[@id='ssw-table']/tbody/tr[" + str(tableRow) + "]/td[6]/div/div/ul/li[1]"
        download_btn = driver.find_element_by_xpath(topXPATH)
        download_btn.click()
        time.sleep(10)




startDownload()
