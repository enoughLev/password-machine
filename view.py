from tkinter import *
import model as m
class MainWindow:
    def __init__(self, root):
        self.root = root
        self.back = Frame(root, background='white')
        self.back.pack(expand=True, fill='both')

        for r in range(1, 6): self.back.rowconfigure(index=r, weight=10)
        self.back.rowconfigure(0, weight=2)
        self.back.rowconfigure(6, weight=2)
        for r in range(1, 4): self.back.columnconfigure(index=r, weight=15)
        self.back.columnconfigure(index=0, weight=2)
        self.back.columnconfigure(index=4, weight=2)

        for r in range(0, 7, 6): 
            for c in range(5):
                Frame(self.back, background='grey').grid(row=r, column=c, sticky='nsew')
        for r in range(1, 6):
            for c in range(0, 5, 4):
                Frame(self.back, background='grey').grid(row=r, column=c, sticky='nsew')

        welcome = Frame(self.back, background='white')
        welcome.grid(row=1, column=2, sticky='nsew')

        Label(welcome, text='Выберите действие:', foreground='black', background='white', font=('Calibri', 14)).pack(side=BOTTOM, anchor=CENTER)
        Label(welcome, text='Начало работы', foreground='black', background='white', font=('Calibri', 20)).pack(side=BOTTOM, anchor=CENTER)

        buttons = Frame(self.back, background='white')
        buttons.grid(row=2, column=2, sticky='nsew')
        for r in range(2): buttons.rowconfigure(index=r, weight=1)
        for r in range(3): buttons.columnconfigure(index=r, weight=1)
        
        Button(buttons, text='Создать новый пароль', font=('Calibri', 14), command=lambda: self.new_window('create')).grid(row=0, column=1)
        Button(buttons, text='Найти сохранённый пароль', font=('Calibri', 14), command=lambda: self.new_window('find')).grid(row=1, column=1, sticky=N)

    def new_window(self, command):
        if command == 'create':
            self.back.pack_forget()
            CreateWindow(self.root)
        elif command == 'find':
            self.back.pack_forget()
            FindWindow(self.root)
        elif command == 'return_back':
            self.back.pack_forget()
            MainWindow(self.root)

class CreateWindow:
    def __init__(self, root):
        self.root = root
        self.back = Frame(root, background='lightgrey')
        self.back.pack(expand=True, fill=BOTH)
        
        self.back.rowconfigure(index=0, weight=1)
        self.back.rowconfigure(index=1, weight=40)
        self.back.rowconfigure(index=2, weight=1)

        self.back.columnconfigure(index=0, weight=1)
        self.back.columnconfigure(index=1, weight=40)
        self.back.columnconfigure(index=2, weight=1)


        for r in range(0, 3, 2): 
            for c in range(3):
                Frame(self.back, background='grey').grid(row=r, column=c, sticky='nsew')
        for r in range(3):
            for c in range(0, 3, 2):
                Frame(self.back, background='grey').grid(row=r, column=c, sticky='nsew')

        self.widg = Frame(self.back, background='lightgrey')
        self.widg.grid(column=1, row=1, sticky=NSEW)

        services = StringVar()
        login = StringVar()
        len_password = StringVar()
        new_pas = StringVar()
        old_pas = StringVar()
        lab_old_pas = StringVar()
        services_text = StringVar()
        flag = False
        def back_to_main(command):
            if command == 'return_back':
                self.back.pack_forget()
                MainWindow(root)
            pass
        
        Label(self.widg, background='lightgrey', text='Генерация', font=('Calibri', 20), justify=CENTER).place(anchor=CENTER, relx=0.5, rely=0.05)

        Label(self.widg, background='lightgrey', text='Введите название сервиса:', font=('Calibri', 13), justify=CENTER).place(anchor=NW, relx=0.015, rely=0.1) # relwidth=0.4, relheight=0.1
        ser = Entry(self.widg, font=('Calibri', 14), textvariable=services)
        ser.place(anchor=NW, relx=0.38, rely=0.1)
        Label(self.widg, background='lightgrey', text='Логин', font=('Calibri', 13), justify=CENTER).place(anchor=NW, relx=0.015, rely=0.2)
        Label(self.widg, background='lightgrey', text='(при необходимости)', font=('Calibri', 8), justify=CENTER).place(anchor=NW, relx=0.015, rely=0.25)
        Entry(self.widg, font=('Calibri', 14), textvariable=login).place(anchor=NW, relx=0.38, rely=0.2)
        Label(self.widg, background='lightgrey', text='Длина пароля', font=('Calibri', 13), justify=CENTER).place(anchor=NW, relx=0.015, rely=0.3)
        Label(self.widg, background='lightgrey', text='(рекомендованная длина 12 символов)', font=('Calibri', 8), justify=CENTER).place(anchor=NW, relx=0.015, rely=0.35)
        Entry(self.widg, font=('Calibri', 14), textvariable=len_password).place(anchor=NW, relx=0.38, rely=0.3)

        #Button(self.widg, text='Сгенерировать', font=('Calibri', 14), command=lambda: self.gener(services, len_password, pas)).place(anchor=CENTER, relx=0.4, rely=0.4)
        Button(self.widg, text='Сгенерировать', font=('Calibri', 14), command=lambda: self.verify(services, len_password, new_pas, old_pas)).place(anchor=CENTER, relx=0.4, rely=0.5)

        Button(self.widg, text='Вернуться назад', font=('Calibri', 10), command=lambda: back_to_main('return_back')).place(relx=0.01, rely=0.94)

        Label(self.widg, textvariable=new_pas, background='lightgrey', font=('Calibri', 12, 'italic'), justify=LEFT).place(relx=0.15, rely=0.65)
        Label(self.widg, textvariable=old_pas, background='lightgrey').place(relx=0.6 , rely=0.6)
        
        txt_warning = "У вас уже имеется пароль \nот данного сервиса! \nЕсли вы хотите создать новый \nпароль для данного сервиса, то \nподтвердите выбор. \nВ случае, если вам необходимо \nузнать существющий пароль \nот сервиса, то проведите \nпоиск пароля по сервису из \nглавного меню.\n{}".format(services.get())
        
        global label_warning
        global label_services
        label_warning = Label(self.widg, text=txt_warning, foreground='red', background='lightgrey', font=('Calibri', 12, 'italic'), justify=LEFT, width=29, height=11, relief=GROOVE, border=2)
        label_services = Label(self.widg, textvariable=services, foreground='black', background='lightgrey', font=('Calibri', 12, 'italic'), justify=LEFT)

        
        """def callback_function_1(*args) :
            txt_1 = ''
            return txt_1"""
        def callback_function(*args) :
            label_warning.place_forget()
            
        def enter_press(*args):
            self.verify(services, len_password, new_pas, old_pas)

        meters = StringVar()
        Label(self.widg, textvariable=meters, background='#E9D66B').grid(column=2, row=2, sticky=(W, E))
        num = '123'
        #ser.bind('<KeyPress>', callback_function)
        root.bind('<Return>', enter_press)

        
        """root.bind('<KeyPress>', callback_function_1)"""
        
    
    def place(self):
        if self.flag:
            label_warning.place(relx=0.665, rely=0.1)
        elif self.flag == False:
            label_warning.place_forget()
            label_services.place(relx=0.15, rely=0.6)
            Label(self.widg, text='Ваш сервис:', background='lightgrey', font=('Calibri', 13), justify=CENTER).place(relx=0.015, rely=0.6)
            Label(self.widg, text='Ваш пароль:', background='lightgrey', font=('Calibri', 13), justify=CENTER).place(relx=0.015, rely=0.65)

    def gener(self, len_password, l_new_pas):
        l_new_pas.set(m.generator_pas(len_password.get()))
    
    def verify(self, l_services, l_len_password, l_pas, l_old_pas):
        if (m.search_password(m.get_spis(), l_services.get())):             #если сервис существует
            l_old_pas.set(m.get_spis()[m.search_password(m.get_spis(), l_services.get())])
            self.flag = True
            self.place()
            #label_warning.place(relx=0.665, rely=0.1)
            print([m.search_password(m.get_spis(), l_services.get())])            
        else:                                                               #если сервис НЕ существует
            self.gener(l_len_password, l_pas)
            self.place()
            





"""     for r in range(1, 6): self.back.rowconfigure(index=r, weight=15)
        self.back.rowconfigure(0, weight=2)
        self.back.rowconfigure(6, weight=2)
        for r in range(1, 6): self.back.columnconfigure(index=r, weight=15)
        self.back.columnconfigure(index=0, weight=2)
        self.back.columnconfigure(index=6, weight=2)

        for r in range(0, 7, 6): 
            for c in range(7):
                Frame(self.back, background='grey').grid(row=r, column=c, sticky='nsew')
        for r in range(1, 7):
            for c in range(0, 7, 6):
                Frame(self.back, background='grey').grid(row=r, column=c, sticky='nsew')

        Label(self.back, background='lightgrey', text='Генерация', font=('Calibri', 20), justify=CENTER).grid(row=1, column=2, sticky=NSEW)
        
        Frame(self.back, background='black').grid(row=1, column=1, sticky=NSEW)
        forms = Frame(self.back, background='blue')
        forms.grid(row=3, column=1, sticky=NSEW, columnspan=4)
        serv = Frame(forms, background='lightgrey')
        serv.grid(row=0, column=0)
        log = Frame(forms, background='white')
        log.grid(row=1, column=0, sticky=NSEW)
        pas = Frame(forms, background='white')
        pas.grid(row=2, column=0, sticky=NSEW)
        services = StringVar()
        login = StringVar()
        len_password = StringVar()
        
        Label(serv, background='lightgrey', text='Введите название сервиса:', font=('Calibri', 14), justify=CENTER).grid(row=0, column=0, sticky=NW, pady=20)
        Entry(serv, font=('Calibri', 14), textvariable=services).grid(row=0, column=1, sticky=NW, pady=20)
        Label(log, background='lightgrey', text='Логин', font=('Calibri', 14), justify=CENTER).grid(row=0, column=0, sticky=NW)
        #Label(forms, background='lightgrey', text='(при необходимости)', font=('Calibri', 8), justify=CENTER).grid(row=3, column=0, sticky=NW)
        Entry(log, font=('Calibri', 14), textvariable=login).grid(row=0, column=1, sticky=NW)
        Label(pas, background='lightgrey', text='Длина пароля', font=('Calibri', 14), justify=CENTER).grid(row=4, column=0, sticky=NW)
        #Label(forms, background='lightgrey', text='(рекомендованная длина 12 символов)', font=('Calibri', 8), justify=CENTER).grid(row=5, column=0, sticky=NW)
        Entry(pas, font=('Calibri', 14), textvariable=len_password).grid(row=4, column=1, sticky=NW)








        Button(self.back, text='Вернуться назад', font=('Calibri', 10), command=lambda: self.new_window('return_back')).grid(row=5, column=1, sticky=SW, padx=10, pady=10)
"""

class FindWindow:
    def __init__(self, root):
        self.root = root
        self.back = Frame(root, background='lightgrey')
        self.back.pack(expand=True, fill=BOTH)
        
        for r in range(1, 6): self.back.rowconfigure(index=r, weight=15)
        self.back.rowconfigure(0, weight=2)
        self.back.rowconfigure(6, weight=2)
        for r in range(1, 6): self.back.columnconfigure(index=r, weight=15)
        self.back.columnconfigure(index=0, weight=2)
        self.back.columnconfigure(index=6, weight=2)

        for r in range(1, 6, 4):
            for c in range(1, 6):
                LabelFrame(self.back, background='grey', text='%d:%d' % (r, c)).grid(row=r, column=c, sticky='nsew')
        for r in range(1, 6):
            for c in range(1, 6, 4):
                LabelFrame(self.back, background='grey', text='%d:%d' % (r, c)).grid(row=r, column=c, sticky='nsew')
        
        """LabelFrame(self.back, background='grey', text='1:3').grid(row=1, column=3, sticky='nsew')
        LabelFrame(self.back, background='grey', text='1:5').grid(row=1, column=5, sticky='nsew')
        LabelFrame(self.back, background='grey', text='3:1').grid(row=3, column=1, sticky='nsew')
        LabelFrame(self.back, background='grey', text='5:1').grid(row=5, column=1, sticky='nsew')"""

        for r in range(0, 7, 6): 
            for c in range(7):
                Frame(self.back, background='grey').grid(row=r, column=c, sticky='nsew')
        for r in range(1, 7):
            for c in range(0, 7, 6):
                Frame(self.back, background='grey').grid(row=r, column=c, sticky='nsew')

        Label(self.back, background='lightgrey', text='Поиск пароля', font=('Calibri', 20), justify=CENTER).grid(row=1, column=1, columnspan=5, rowspan=1)

        """entry = Frame(self.back, background='red') #lightgrey
        entry.grid(row=2, column=1, sticky=NSEW, padx=7, columnspan=2)
        Label(entry, background='lightgrey', text='Введите название сервиса:', font=('Calibri', 16), justify=LEFT).pack(anchor=W)
        pas = StringVar()
        Entry(entry, textvariable=pas, font=('Calibri', 14)).pack(anchor=SW)
        Button(entry, text='Искать', font=('Calibri', 14), command=lambda: self.find(pas)).pack(anchor=SE)

        Button(self.back, text='Вернуться назад', font=('Calibri', 10), command=lambda: self.new_window('return_back')).grid(row=5, column=1, sticky=SW, padx=10, pady=10)
"""
    def find(self, pas):
        result = Frame(self.back, background='lightgrey')
        result.grid(row=3, column=1, sticky=NSEW, padx=5)
        Label(result, text=m.get_spis()[m.search_password(m.get_spis(), pas.get())]).pack()
        #print(pas)
        
    def new_window(self, command):
        if command == 'return_back':
            self.back.pack_forget()
            MainWindow(self.root)

        pass

