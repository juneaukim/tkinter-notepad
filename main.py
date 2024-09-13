from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.title("Notepad")
window.resizable(False,False)

menu = Menu(window)
menu_1 = Menu(menu, tearoff=0)
menu_1.add_command(label="New File")
menu_1.add_command(label="save")
menu_1.add_separator()
menu_1.add_command(label="exit", command=window.destroy)
menu.add_cascade(label="File", menu=menu_1)

menu_2 = Menu(menu, tearoff=0)
menu_2.add_command(label="founder")
menu.add_cascade(label="founder", menu=menu_2)

window.config(menu=menu)