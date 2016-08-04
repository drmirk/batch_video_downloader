def startDownload():
    ## Imported selenium webdriver

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys as keys
    import time

    ## used chrome as primary browser
    ## store the chrome app in a place and show the path

    ##driver = webdriver.Chrome("/home/ibrahim/Downloads/chromedriver")
    driver = webdriver.Chrome()
    
    ## visit videoblocks login site and select both email and passwor field

    driver.get('http://www.videoblocks.com/login/')
    email = driver.find_element_by_id('login-email')
    #print(email)
    passwd = driver.find_element_by_id('login-password')
    #print(passwd)

    ## entered both email and password from GUI
    ## and then changed to the final download folder

    email.send_keys("mukimscreation@gmail.com")
    #print("email.send_keys(emailAddress)\n")
    passwd.send_keys("abidbari")
    #print("passwd.send_keys(password)\n")
    passwd.send_keys(keys.RETURN)
    #print("passwd.send_keys(keys.RETURN)\n")
    driver.get("https://www.videoblocks.com/member/bin/view/lneAbH6P3QuOHMutEBd0HJNhk")
    #print("driver.get(folderAddress)\n")
    '''
    check_login = True
    while(check_login):
        if('Folder - VideoBlocks' in driver.title):
            check_login = False
            print("Check login false")
        else:
            driver.get(folderAddress)
            print("now redirecting")
    '''

    ########################################################
    ########################################################
    ########################################################
    ########################################################
    ########################################################

    ## find all the videos download links

    download_links = driver.find_elements_by_xpath("//*[@id='cool-new-btn']")
    print("download links complete")
    print(len(download_links))
    print("\n \n \n")
    trNo = 0
    for links in download_links:
        trNo = trNo + 1
        links.click()
        time.sleep(2)
        myXpath = "//*[@id='ssw-table']/tbody/tr[" + str(trNo) + "]/td[6]/div/div/ul/li[1]"
        download_btn = driver.find_element_by_xpath(myXpath)
        download_btn.click()
        


startDownload()
