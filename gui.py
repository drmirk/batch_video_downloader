from tkinter import *
from tkinter import ttk


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




##-----------------------------------------------------
##-----------------------------------------------------
## Entry fields

email = ttk.Entry(root, width = 100)
email.grid(row = 0, column = 1)

passwd = ttk.Entry(root, width = 100)
passwd.grid(row = 1, column = 1)

folderLink = Text(root, width = 75, height = 5)
folderLink.grid(row = 2, column = 1)
folderLink.config(wrap = "char")
##-----------------------------------------------------
##-----------------------------------------------------




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




##-----------------------------------------------------
##-----------------------------------------------------
## Button
downloadButton = ttk.Button(root, text = "Download")
downloadButton.grid(row = 3, column = 1)
downloadButton.config(command = getInfo)




