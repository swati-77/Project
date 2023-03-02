from tkinter import *
from tkinter.messagebox import  showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file 
    root.title("Untitled - Notepad")
    file=None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) +"- Notepad")
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None :
        file = asksaveasfilename(initalfile= 'Untitled.txt', defaultextension= ".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file== "":
            file = None
        else:
            #Save as a new File 
            f= open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file)+ "-Notepad")
            print("File Saved")
    else:
        #Save the file
        f= open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Take easy notes.")

if __name__ == '__main__':
    #Basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    #  root.wm_iconbitmap("1.ico")    karna h
    root.geometry("644x788")
    #add textArea
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand = True, fill=BOTH)


    #lets create a menubar
    MenuBar = Menu(root)
    #File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)

    #to open new file
    FileMenu.add_command(label="New", command= newFile)

    #To Open already Existing file
    FileMenu.add_command(label="Open", command= openFile)

    #to save the current file
    FileMenu.add_command(label ="Save", command= saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label= "Exit", command= quitApp)
    MenuBar.add_cascade(label= "File", menu=FileMenu)
    #File Menu Ends

    #Edit menu Starts
    EditMenu= Menu(MenuBar, tearoff=0)
    #To give A feature of Cut, copy and paste
    EditMenu.add_command(label= "Cut", command= cut)
    EditMenu.add_command(label= "Copy", command= copy)
    EditMenu.add_command(label= "Paste", command= paste)

    MenuBar.add_cascade(label="Edit", menu= EditMenu)

    #File Menu Ends

    #Help Menu starts
    HelpMenu= Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label= "About Nptepad", command = about) 
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    #help menu ends

    root.config(menu=MenuBar)
    #Adding Scrollbar using rules from Tkinter
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side= RIGHT, fill = Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand= Scroll.set)

    root.mainloop()
    