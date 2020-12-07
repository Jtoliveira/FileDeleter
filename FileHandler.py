import os
from tkinter import *

mainWindow = Tk()

mainWindow.geometry("400x400")
mainWindow.title("File Deletus")

def fileFunction(path, file, instruction):
    for root, directories, files in os.walk(path, topdown=False): #walk() lists the files and the subdirectories
        for name in files:
            if name == file:
                if instruction == "open":
                    try:
                        os.system(os.path.join(root,name)) #open the file/launch the exec/ etc
                    except:
                        wrongLabel = Label(mainWindow, text="Something went wrong") 
                        wrongLabel.place(x = 60, y = 140)
                        wrongLabel.after(2000, lambda: wrongLabel.destroy()) 

                elif instruction == "delete":

                    try:
                        warning = "Deleted the file: " + os.path.join(root,file)

                        os.remove(os.path.join(root,name)) #delete the file

                        deletedLabel = Label(mainWindow, text=warning) 
                        deletedLabel.place(x = 60, y = 140)
                        deletedLabel.after(2000, lambda: deletedLabel.destroy()) #destroy the label after two seconds
                    except:
                        wrongLabel = Label(mainWindow, text="Something went wrong") 
                        wrongLabel.place(x = 60, y = 140)
                        wrongLabel.after(2000, lambda: wrongLabel.destroy()) 
                    
pathLabel = Label(mainWindow, text ="Path to folder") 
pathLabel.place(x = 120, y = 20) 
  
path = Entry(mainWindow, width = 35) 
path.place(x = 220, y = 20, width = 100) 

fileLabel = Label(mainWindow, text ="Filename") 
fileLabel.place(x = 120, y = 60)
  
file = Entry(mainWindow, width = 35) 
file.place(x = 220, y = 60, width = 100) 

deleteButton = Button(mainWindow, text= "Delete the file", command= lambda: fileFunction(path.get(), file.get(), "delete"))
deleteButton.place(x = 200, y = 100)

openButton = Button(mainWindow, text= "Open the file", command= lambda: fileFunction(path.get(), file.get(), "open"))
openButton.place(x = 100, y = 100)

mainWindow.mainloop()
            
