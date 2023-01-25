from view import MainWindow
import model as m
from tkinter import *
import time
from threading import Thread, main_thread


spis = m.get_spis()

root = Tk()
root.title('Password manager')
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2 # середина экрана
h = h//2 
w = w - 400 # смещение от середины
h = h - 350
root.geometry('800x600+{}+{}'.format(w, h))
root.resizable(False, False)
root.iconphoto(True, PhotoImage(file='img\icon.png'))

main = MainWindow(root)

def finish():
    root.destroy()
root.protocol("WM_DELETE_WINDOW", finish)


root.mainloop()
