import tkinter
import tkinter.filedialog
import os
import webbrowser
import re
from tkinter import *
from tkinter import ttk, messagebox
from os import getcwd
from datetime import datetime, timedelta
from ScrollableNotebook import *

root = Tk()
root.option_add("*Font", "Verdana 10")
tabslist = []
tabControl = ScrollableNotebook(root,wheelscroll=True)
style = ttk.Style(root)
style.configure('lefttab.TNotebook', tabposition='wn')

#########################################################################

def helpweb():
    webbrowser.open('https://github.com/dzhemvrot/latviadebate_app/blob/main/README.md', new=2)

def helps():
    win = Toplevel()
    win.title('About')
    message = """This is a program for redacting Ace Attorney NDS Scripts.

Program author: dzhemvrot
Program version: 3.0
Program restributed using GPL-3.0 license"""
    HelpLab = Label(win, text=message)
    HelpLab.grid(row=0, column=1)
    HelpBut = Button(win, text='Help', command=helpweb)
    HelpBut.grid(row=1, column=0)
    ClBut = Button(win, text='Close', command=win.destroy)
    ClBut.grid(row=1, column=2)
    win.resizable(False, False)

def load():
    ftypes = [('Txt file', '*.txt'), ('All files', '*')] 
    fn = tkinter.filedialog.Open(root, filetypes = ftypes).show()
    if fn == '':
        return
    filetext = open(fn).read()
    result = filetext.split('[')
    #print(result)
    tab = {}
    for i in range(len(result)):
        #print('"' + result[i] + '"')
        if result[i] != result[0]:
            tab[i] = ttk.Frame(tabControl)
            tabControl.add(tab[i], text=f"{i-1}")
            #print(f'Added tab {i}!')
    tabControl.pack(fill='both', expand=True)
    #tabScroll = Scrollbar(tab[i], orient='horizontal', command=tabControl.yview)
    #tabScroll.pack(fill='both', expand=True, sticky=NS)
    # this is not working so i just commented this
    for i in range(len(result)):
        if result[i] != result[0]:
            globals()["textwrite_"+str(i)] = Text(tab[i])
            globals()["textwrite_"+str(i)].pack(fill='both', expand=True)
            #globals()["scrollbar_fortext_"+str(i)] = Scrollbar(tab[i], orient='vertical', command=globals()["textwrite_"+str(i)].yview)
            #globals()["scrollbar_fortext_"+str(i)].pack(fill='both', expand=True, sticky=NS)
            # i dont have any clue how to make this stuff work ^^^
            globals()["textwrite_"+str(i)].insert('1.0', "[" + result[i])
    global length
    length = len(result)
    
def save():
    fn = tkinter.filedialog.SaveAs(root, filetypes = [('Txt file', '*.txt'), ('All files', '*')]).show()
    if fn == '':
        return
    wholetext = "\n"
    for i in range(length):
        if i != 0:
            wholetext += globals()["textwrite_"+str(i)].get('1.0', 'end')
    open(fn, 'wt').write(wholetext)
    tkinter.messagebox.showinfo(title='Success!', message='''File saved successfully!''')

#########################################################################

#########################################################################

menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(menubar,tearoff=0)

file_menu.add_command(label='Load', command = load)
file_menu.add_command(label='Save', command = save)
file_menu.add_separator()

file_menu.add_command(
    label='Exit',
    #command=on_closing
)

menubar.add_cascade(
    label="File",
    menu=file_menu
)

menubar.add_command(label='About', command = helps)


#########################################################################

try:
    root.iconbitmap('icon.ico')
except:
    pass
root.title(u'AA1SE')
root.geometry("1280x720")
root.resizable(False, False)
#root.protocol("WM_DELETE_WINDOW", on_closing)
root.bind("<Control-s>", lambda event: save())
root.bind("<Control-o>", lambda event: load())
root.mainloop()
