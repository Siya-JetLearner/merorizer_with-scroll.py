from tkinter import *
from tkinter.filedialog import *

master = Tk()
master.title("Memorizer")


fopen = Button (master, text="OPEN", command=openFile, width=15) 
fDelete = Button (master, text="DELETE", command=deleteItem, width=15) 
fSave = Button (master, text="SAVE", command=saveFile, width=15)


fopen.pack(side=LEFT, padx=5, pady=5) 
fDelete.pack(side=RIGHT, padx=5, pady=5)
fSave.pack(padx=5, pady=5)

fAdd = Button (master, text="ADD", command=addItem, width=15)
item =Entry(master, width=35)
item.pack(padx=5, pady=5)
fAdd.pack(padx=5, pady=5)


frame = Frame (master)
scrollbar = Scrollbar (frame, orient="vertical")
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox (frame, width=70, yscrollcommand=scrollbar.set, bg='red')

for i in range(1,100):
    listbox.insert(END, "LIST" + str(i))

listbox.pack(side=LEFT, padx=5)
scrollbar.config(command=listbox.yview)
