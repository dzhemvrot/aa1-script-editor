import tkinter
import tkinter.filedialog
from tkinter import *

root = Tk()
root.option_add("*Font", "Verdana 10")

#########################################################################

def scan():
    start = "1.0"
    end = "end"
    mycount = IntVar()

    regex_patterns = [r'".*"', r'#.*']

    for pattern in regex_patterns:
        Text.mark_set("start", start)
        Text.mark_set("end", end)

        num = int(regex_patterns.index(pattern))

        while True:
            index = Text.search(pattern, "start", "end", count=mycount, regexp = True)

            if index == "": break

            Text.mark_set("start", "%s+%sc" % (index, mycount.get()))

def cypher():
    alll = Text.get("1.0",END)
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    i = 64
    for j in range(len(alphabet)):
        char = alphabet[j]
        alll = alll.replace(char, "{"+str(i)+"}")
        i = i+1
    alll = alll.replace('№', "{130}")
    alll = alll.replace('-', "{132}")
    #alll = alll.replace('—', "{132}")
    alll = alll.replace('«', "{<<}")
    alll = alll.replace('»', "{>>}")
    alll=alll[:-1]
    Text.delete("0.0", "end")
    Text.insert("0.0", alll)

def decypher():
    alll = Text.get("0.0",END)
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    i = 64
    for j in range(len(alphabet)):
        char = alphabet[j]
        alll = alll.replace("{"+str(i)+"}", char)
        i = i+1
    alll = alll.replace("{130}", '№')
    alll = alll.replace("{131}", '-')
    alll = alll.replace("{132}", '—')
    alll = alll.replace("{<<}", '«')
    alll = alll.replace("{>>}", '»')
    alll=alll[:-1]
    Text.delete("0.0", "end")
    Text.insert("0.0", alll)

def update():
    scan()

def clear():
    Text.delete("1.0", "end")

def load():
    ftypes = [('Расшифрованный txt файл скрипта', '*.txt'), ('Все файлы', '*')] 
    fn = tkinter.filedialog.Open(root, filetypes = ftypes).show()
    if fn == '':
        return 
    Text.delete('1.0', 'end')
    Text.insert('1.0', open(fn).read())   

def save():
    fn = tkinter.filedialog.SaveAs(root, filetypes = [('Расшифрованный txt файл скрипта', '*.txt'), ('Все файлы', '*')]).show()
    if fn == '':
        return
    open(fn, 'wt').write(Text.get('1.0', 'end'))

#########################################################################

menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(menubar,tearoff=0)

file_menu.add_command(label='Open', command = load)
file_menu.add_command(label='Save', command = save)
file_menu.add_separator()

file_menu.add_command(
    label='Exit',
    command=root.destroy
)

menubar.add_cascade(
    label="File",
    menu=file_menu
)

menubar.add_command(label='About')

#########################################################################

Label = Label(root, text = "Ace Attorney Script Editor")
Label.grid(row=0, column=0, columnspan=5)

Text = Text(root)
Text.grid(row = 1, column = 0, columnspan = 5)

ClearB = Button(root, text = "Clear", width = 8, command = clear)
ClearB.grid(row = 2, column = 1, padx=20, pady=10)
CB = Button(root, text = "Cypher", width = 8, command = cypher)
CB.grid(row = 2, column = 2, padx=20, pady=10)
DCB = Button(root, text = "Decypher", width = 8, command = decypher)
DCB.grid(row = 2, column = 3, padx=20, pady=10)

scrollbar = Scrollbar(root, orient='vertical', command=Text.yview)
scrollbar.grid(row=1, column=5, sticky=NS)

Text['yscrollcommand'] = scrollbar.set

try:
    root.iconbitmap('icon.ico')
except:
    pass
root.title(u'Ace Attorney Script Editor')
root.resizable(False, False)
root.bind("<Key>", lambda event: update())
root.mainloop()
