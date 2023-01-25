from view import MainWindow
from tkinter import *


def main():

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

    root.mainloop()

if __name__ == "__main__":
    main()