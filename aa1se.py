from tkinter import *
import tkinter.filedialog   #модуль filedialog для диалогов открытия/закрытия файла
from collections import deque

class Window:
    def __init__(self, master):
        self.master = master
        self.master.option_add("*Font", "Verdana 12")
 
        self.Main = Frame(self.master)
 
        self.stack = deque(maxlen = 10)
        self.stackcursor = 0
 
        self.L1 = Label(self.Main, text = "This is my Code Editor")
        self.L1.pack(padx = 5, pady = 5)

def Mark(ev):
    Person(ev)

#def Person(ev):

def Quit(ev):
    global root
    root.destroy()
    
def LoadFile(ev):
    ftypes = [('Все файлы', '*'), ('txt файлы', '*.txt'), ('Файлы Python', '*.py'), ('Файлы html', '*.html')] # Фильтр файлов
    fn = tkinter.filedialog.Open(root, filetypes = ftypes).show()
    
    if fn == '':
        return
    #if person in fn:
        
    textbox.delete('1.0', 'end')    # Очищаем окно редактирования
    textbox.insert('1.0', open(fn).read())   # Вставляем текст в окно редактирования
    person
     
    global cur_path
    cur_path = fn # Храним путь к открытому файлу
   
def SaveFile(ev):
    fn = tkinter.filedialog.SaveAs(root, filetypes = [('Все файлы', '*'), ('txt файлы', '*.txt'), ('Файлы Python', '*.py'), ('Файлы html', '*.html')]).show()
    if fn == '':
        return
    open(fn, 'wt').write(textbox.get('1.0', 'end'))

root = Tk() # объект окна верхнего уровня создается от класса Tk модуля tkinter. 
#Переменную, связываемую с объектом, часто называют root (корень)
    
    
root.title(u'AA1 scripts redactor')


panelFrame = Frame(root, height = 60, bg = 'gray')
textFrame = Frame(root, height = 340, width = 600)

panelFrame.pack(side = 'top', fill = 'x')   #упакуем с привязкой к верху
textFrame.pack(side = 'bottom', fill = 'both', expand = 1)  

textbox = Text(textFrame, font='Arial 14', wrap='word')  #перенос по словам метод wrap
scrollbar = Scrollbar(textFrame)

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

textbox.pack(side = 'left', fill = 'both', expand = 1)  #текстбокс слева
scrollbar.pack(side = 'right', fill = 'y')    #расположим скролбар (лифт) справа

loadBtn = Button(panelFrame, text = 'Load')
saveBtn = Button(panelFrame, text = 'Save')
markBtn = Button(panelFrame, text = 'Mark')
quitBtn = Button(panelFrame, text = 'Quit', bg='#A9A9A9',fg='#FF0000')

markBtn.bind("<Button-1>", Mark)
loadBtn.bind("<Button-1>", LoadFile)
saveBtn.bind("<Button-1>", SaveFile)
quitBtn.bind("<Button-1>", Quit)

loadBtn.place(x = 10, y = 10, width = 130, height = 40)
saveBtn.place(x = 150, y = 10, width = 130, height = 40)
markBtn.place(x = 290, y = 10, width = 100, height = 40)
quitBtn.place(x = 400, y = 10, width = 100, height = 40)

self.T1 = Text(self.Main, width = 90, height = 25)
 
self.T1.tag_configure("orange", foreground = "orange", font = "Verdana 12")
self.T1.tag_configure("blue", foreground = "blue", font = "Verdana 12")
self.T1.tag_configure("purple", foreground = "purple", font = "Verdana 12")
self.T1.tag_configure("green", foreground = "green", font = "Verdana 12")
#self.T1.tag_configure("red", foreground = "red", font = "Verdana 12")
 
self.tags = ["red", "yellow", "orange", "green"]
 
self.wordlist = [ ["<p>"],
                  ["int", "string", "float", "bool", "__init__"],
                  ["pygame", "tkinter", "sys", "os", "mysql"],
                  ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] ]
 
self.T1.bind("<Return>", lambda event: self.indent(event.widget))
         
self.T1.pack(padx = 5, pady = 5)


#root.wm_attributes('-fullscreen','true')
root.iconbitmap('icon.ico')
root.mainloop()
