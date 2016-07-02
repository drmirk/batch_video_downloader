from tkinter import *
from tkinter import ttk


def buttonCommand():
    emailAddress = email.get()
    password = passwd.get()
    folder = folderLink.get("1.0", "end")
    
def theGui():
    root = Tk()
    root.geometry('720x200+200+200')

    userName = ttk.Label(root, text = "Email Address")
    userName.grid(row = 0, column = 0)

    email = ttk.Entry(root, width = 100)
    email.grid(row = 0, column = 1)

    passwdLabel = ttk.Label(root, text = "Password")
    passwdLabel.grid(row = 1, column = 0)

    passwd = ttk.Entry(root, width = 100)
    passwd.grid(row = 1, column = 1)

    folderLabel = ttk.Label(root, text = "Folder Link")
    folderLabel.grid(row = 2, column = 0)

    folderLink = Text(root, width = 75, height = 5)
    folderLink.grid(row = 2, column = 1)
    folderLink.config(wrap = "char")

    downloadButton = ttk.Button(root, text = "Download")
    downloadButton.grid(row = 3, column = 1)


    def buttonCommand():
        emailAddress = email.get()
        password = passwd.get()
        folder = folderLink.get("1.0", "end")

    downloadButton.config(command = buttonCommand)






    
    
