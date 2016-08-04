## This version takes username, email and folder link
## then downloads video one by one from that page only
## so if that folder had more than one page, it wont go
## to other pages.
## Also, this works with by checking ".crdownload" in
## the pc download folder only
########################################################
########################################################

## import tkinter widgets

from tkinter import *
from tkinter import ttk

## the root widget with a fixed size

root = Tk()
root.geometry('720x200+200+200')

##------------------------------------------------------
##------------------------------------------------------
## Labels

userName = ttk.Label(root, text = "Email Address")
userName.grid(row = 0, column = 0)

passwdLabel = ttk.Label(root, text = "Password")
passwdLabel.grid(row = 1, column = 0)

folderLabel = ttk.Label(root, text = "Folder Link")
folderLabel.grid(row = 2, column = 0)



##-----------------------------------------------------
##-----------------------------------------------------
## Entry fields

email = ttk.Entry(root, width = 100)
email.grid(row = 0, column = 1)

passwd = ttk.Entry(root, width = 100)
passwd.grid(row = 1, column = 1)
passwd.config(show = "*")

folderLink = Text(root, width = 75, height = 5)
folderLink.grid(row = 2, column = 1)
folderLink.config(wrap = "char")



##-----------------------------------------------------
##-----------------------------------------------------
## Button command and variables

emailAddress = ""
password = ""
folderAddress = ""
def getInfo():
    global emailAddress
    global password
    global folderAddress
    emailAddress = email.get()
    password = passwd.get()
    folderAddress = folderLink.get("1.0", "end")
    folderAddress = folderAddress[:-1]
    startDownload()




##-----------------------------------------------------
##-----------------------------------------------------
## Button
downloadButton = ttk.Button(root, text = "Download")
downloadButton.grid(row = 3, column = 1)
downloadButton.config(command = getInfo)



########################################################
########################################################
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
    driver = webdriver.Chrome()                                                     ## for windows
    
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


    ## redirect to the final download folder
    check = True
    while(check):
        if(driver.title == "Members Dashboard - VideoBlocks"):
            driver.get(folderAddress)
            check = False
        else:
            time.sleep(2)


    ## check to page load and find all the videos download links
    check = True
    time.sleep(5)
    while(check):
        if(driver.title == "My Folder - VideoBlocks"):
            download_links = driver.find_elements_by_xpath("//*[@id='cool-new-btn']")
            print(len(download_links))
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
            if((driver.title == "My Folder - VideoBlocks") and (crDownload < 3)):
                links.click()
                time.sleep(3)
                check = False
            else:
                time.sleep(5)
        topXPATH = "//*[@id='ssw-table']/tbody/tr[" + str(tableRow) + "]/td[6]/div/div/ul/li[1]"
        download_btn = driver.find_element_by_xpath(topXPATH)
        download_btn.click()
        time.sleep(10)
