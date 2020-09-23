from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext as scrolltext
import time
def run():
    filename = "untitled"
    START = 0.0
    def new_file():
        global filename
        filename = "untitled"
        text.delete(START,END)
    def save_file():
        global filename
        t = text.get(START,END)
        with open(filename+'.txt', 'w') as file:
            file.write(t)
    def save_file_as():
        file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        t = text.get(START,END)
        try:file.write(t.rstrip())
        except :showerror(title='problem', message='there was a probleam saving the file')
    def open_file():
        global filename
        file = filedialog.askopenfile(mode='r')
        root.title(file)   
        t = file.read()
        text.delete(START, END)
        text.insert(START, t)
    def rename():
        global filename
        pass

    root = Tk()
    root.title("nunix's text editor")        
    root.minsize(width=300,height=300)
    root.maxsize(width=1200,height=900)
    text = scrolltext.ScrolledText(root, width=400, height=400)
    text.pack(side='left')
    menu_bar = Menu(root)
    file_menu = Menu(menu_bar)
    file_menu.add_command(label='new file', command=new_file)
    file_menu.add_command(label='open file', command=open_file)
    file_menu.add_command(label='save', command=save_file)
    file_menu.add_command(label='save as', command=save_file_as)
    file_menu.add_command(label='rename', command=rename)

    file_menu.add_separator()

    file_menu.add_command(label='quit',command=root.quit)
    menu_bar.add_cascade(label='file',menu=file_menu)
    root.config(menu=menu_bar)
    root.mainloop()
    new_file()
if __name__ == '__main__':
    try:
        run()
    except Exception:pass