from cryptography.fernet import Fernet, InvalidToken  # Модули для ключа и ошибки ключа
from tkinter import *  # Модуль GUI
import tkinter.ttk as ttk  # Модуль виджетов GUI
from PIL import ImageTk  # Модуль для связи GUI и изображений
from PIL import Image as Img  # Модуль для  изображений
from pyperclip import copy  # Модуль для копирования текста в буфер обмена
from random import sample  # Модуль рандом для генерации пароля


login = ''
password = '123456'


# Класс для проверки пароля и запуска основного окна
class Start:
    def __init__(self):
        self.start = Tk()
        self.start.geometry('240x450')
        self.start.title('Verification')
        self.start.attributes("-topmost", True)
        self.start.resizable(False, False)
        self.start.configure(background='#FFFFFF')
        self.start.bind('<Return>', lambda event: self.check())

        self.flag_wrong, self.flag_add, self.flag_show, self.new_login, self.new_password = 0, False, True, 0, 0
        self.img_lock1 = ImageTk.PhotoImage(Img.open('textures.png').crop((1, 35, 49, 83)))
        self.img_touch1 = ImageTk.PhotoImage(Img.open('textures.png').crop((50, 35, 114, 99)))
        self.img_lock2 = ImageTk.PhotoImage(Img.open('textures.png').crop((1, 84, 49, 132)))
        self.img_touch2 = ImageTk.PhotoImage(Img.open('textures.png').crop((115, 35, 179, 99)))
        self.img_enter = ImageTk.PhotoImage(Img.open('textures.png').crop((103, 1, 119, 17)))
        self.img_voice = ImageTk.PhotoImage(Img.open('textures.png').crop((18, 18, 34, 34)))
        self.img_visible0 = ImageTk.PhotoImage(Img.open('textures.png').crop((120, 1, 136, 27)))
        self.img_visible1 = ImageTk.PhotoImage(Img.open('textures.png').crop((137, 1, 153, 27)))

        self.lock_image = Label(self.start, bg='#FFFFFF', image=self.img_lock1)
        self.touch_image = Label(self.start, bg='#FFFFFF', image=self.img_touch1)
        self.status = Label(self.start, text='Place your index finger on the scanner.', bg='#FFFFFF')
        self.entry_login = ttk.Entry(self.start)
        self.frame_password = Frame(self.start, bg='#000000')
        self.entry_password = Entry(self.frame_password, fg='#000000', bg='#FFFFFF', relief=FLAT, show='*')
        self.entry_password.focus_force()
        self.visible_button = Button(self.frame_password, relief='flat', border='0', bg='#FFFFFF', activebackground="#ffffff", image=self.img_visible0, command=self.show)
        self.register_button = Button(self.start, relief='flat', border='0', bg='#FFFFFF', activebackground='#FFFFFF', text='Зарегистрироваться', command=self.register)
        self.check_button = Button(self.start, relief='flat', border='0', bg='#2f3035', activebackground='#202020', fg='#FFFFFF', activeforeground='#FFFFFF', text='Proceed', command=self.check)
        self.voice_button = Button(self.start, relief='flat', border='0', bg='#FFFFFF', activebackground="#ffffff", text=' Voice Assistance', image=self.img_voice, compound="left")

        self.lock_image.place(x=96, y=20)
        Label(self.start, bg='#FFFFFF', text='Verification', font=('tKDefaultFont', 15, 'bold')).place(x=0, y=80, width=240)
        self.touch_image.place(x=88, y=112)
        self.status.place(x=0, y=185, width=240)
        Label(self.start, bg='#FFFFFF', text='Enter Social Security Number').place(x=20, y=274)
        self.frame_password.place(x=20, y=295, width=200, height=30)
        self.entry_password.place(x=1, y=1, width=180, height=28)
        self.visible_button.place(x=181, y=1)
        self.check_button.place(x=20, y=345, width=200, height=30)
        self.voice_button.place(x=65, y=415)

        self.start.mainloop()

    #  Метод кнопки
    def check(self):
        global login
        if self.flag_add:
            login = self.entry_login.get()
            self.new_password = self.entry_password.get()
            if self.entry_login.get() == '' or self.entry_password.get() == '':
                self.status['text'] = 'Один или несколько пустых вводов.'
            else:
                self.entry_login.delete(0, END)
                self.entry_password.delete(0, END)
                print(f'login: <{login}>\npassword: <{self.new_password}>')
                self.lock_image.config(image=self.img_lock2)
                self.touch_image.config(image=self.img_touch2)
                self.status.config(fg='#3cd184')
                self.status['text'] = 'Успешная регистрация'
                self.start.after(2000, self.leave)
        else:
            if self.entry_password.get() == password:
                self.lock_image.config(image=self.img_lock2)
                self.touch_image.config(image=self.img_touch2)
                self.status.config(fg='#3cd184')
                self.status['text'] = 'Verified!'
                self.start.after(2000, self.leave)
                # _2 = Ma1n()  # Присваиваем окну класс для изменения
            elif self.entry_password.get() == '':
                self.status['text'] = 'Пустой ввод.'
            else:
                self.status['text'] = 'Повторите ввод.'
                self.entry_password.delete(0, END)
                self.flag_wrong += 1
                if self.flag_wrong == 3:
                    self.register_button.place(x=20, y=325)
                    self.flag_wrong = 0
                else:
                    pass

    #  Метод регистрации аккаунта (доделать)
    def register(self):
        self.status['text'] = 'Введите логин и пароль.'
        Label(self.start, bg='#FFFFFF', text='Enter Login').place(x=20, y=214)
        self.entry_login.place(x=20, y=235, width=200)
        self.register_button.place_forget()
        self.flag_add = True

    #  Метод видимости пароля
    def show(self):
        if self.flag_show:
            self.visible_button.config(image=self.img_visible1)
            self.entry_password.config(show='')
            self.flag_show = False
        else:
            self.visible_button.config(image=self.img_visible0)
            self.entry_password.config(show='*')
            self.flag_show = True

    #  Метод выхода из "стартового" и запуск главного окна
    def leave(self):
        self.start.destroy()
        _2 = Ma1n()


# Класс для основного окна.
class Ma1n:
    # Инициализация переменных.
    def __init__(self):
        global login
        self.A = []  # Обозначаем пустой список
        self.flag = False  # Флаг для нажатия на столбец базы данных
        self.filepath = r'bd'  # Путь к файлу
        self.texture = r'textures.png'  # Путь к иконкам
        try:
            self.key = open('key.key', 'rb').read()  # Открытие файла ключа
        except FileNotFoundError:
            with open(f'{login}.key', 'wb') as key_file:
                key_file.write(Fernet.generate_key())
            self.key = open(f'{login}.key', 'rb').read()
        self.f = Fernet(self.key)  # Обозначаем бинарный ключ шифрования
        self.columns = ('название', 'вебсайт', 'логин', 'пароль', 'заметки')  # Колонки таблицы
        self.style = ['#FFFFFF', '#000000', '#FF0000']  # Стиль (тема)
        # self.style = ['#202020', '#FFFFFF', '#6A8759']  # Резервный стиль (стандартная тема)
        self.ma1n = Tk()  # Переменная ma1n это GUI окно
        self.img_add = ImageTk.PhotoImage(Img.open(self.texture).crop((1, 1, 17, 17)))
        self.img_chng = ImageTk.PhotoImage(Img.open(self.texture).crop((18, 1, 34, 17)))
        self.img_del = ImageTk.PhotoImage(Img.open(self.texture).crop((35, 1, 51, 17)))
        self.img_gnrt = ImageTk.PhotoImage(Img.open(self.texture).crop((52, 1, 68, 17)))
        self.img_sett = ImageTk.PhotoImage(Img.open(self.texture).crop((69, 1, 85, 17)))
        self.img_exit = ImageTk.PhotoImage(Img.open(self.texture).crop((86, 1, 102, 17)))
        self.img_ent = ImageTk.PhotoImage(Img.open(self.texture).crop((103, 1, 119, 17)))
        self.img_debug = ImageTk.PhotoImage(Img.open(self.texture).crop((1, 18, 17, 34)))
        self.taskbar()
        self.data()
        self.ma1n.geometry('930x250')
        self.ma1n.title('Password Manager')  # Меняем имя главного окна
        self.ma1n.attributes("-topmost", True)
        self.ma1n.configure(bg=self.style[0])  # Меняем главному окну стиль
        self.ma1n.bind('<Return>', lambda event: self.variable.set(1))
        self.load()
        self.ma1n.mainloop()  # Запуск главного окна

    # Функция нажатия на столбец по выбору.
    def select(self, _event):
        if not self.flag:  # Если флажок по умолчанию = False
            for selection in self.tree.selection():
                pwd = self.tree.item(selection)['values'][3]
                self.status['text'] = f'Скопировано: <{str(pwd)}>'
                copy(pwd)
        elif self.flag == 'delete':
            for selection in self.tree.selection():
                self.line = self.tree.item(selection)['values']
                self.status['text'] = f'Удалить [{self.line[0]}]?'
        elif self.flag == 'edit':
            for selection in self.tree.selection():
                self.line = self.tree.item(selection)['values']
                self.status['text'] = f'Редактировать [{self.line[0]}]?'

    # Функция, постоянно выполняющаяся после каждой команды.
    def every(self):
        self.flag = False
        self.status['text'] = ''
        self.entry.delete(0, END)
        for i in self.tree.get_children():
            self.tree.delete(i)
        self.A = sorted(self.A)
        for i in self.A:
            self.tree.insert('', END, values=i)
        self.ma1n.update()

    # Функция раскодирования и загрузки базы из файла.
    def load(self):
        try:
            with open(self.filepath, 'rb') as file:
                decrypted_data = self.f.decrypt(file.read())
            with open(self.filepath, 'wb') as file:
                file.write(decrypted_data)
        except FileNotFoundError:
            self.status['text'] = 'Ошибка. Не могу найти файл. Запуск.'
            with open(self.filepath, 'w') as file:
                file.close()
        except (InvalidToken, TypeError):
            self.save()
            self.load()
        finally:
            with open(self.filepath, 'r', encoding='UTF-8') as file:
                self.A = sorted([i.replace('\n', '').replace('▓▓', '▓').split('▓') for i in file.readlines()])
            self.every()

    # Функция добавления аккаунта в таблицу.
    def add(self):
        B = []
        self.flag = 'add'
        for i in range(5):
            self.status['text'] = f'[Добавление] Введите {self.columns[i]}: '
            self.entry.delete(0, END)
            self.ma1n.wait_variable(self.variable)
            if self.entry.get() == '':
                B.append(' ')
            else:
                B.append(str(self.entry.get()))
                self.entry.delete(0, END)
        self.A.append(B)
        self.every()

    # Функция изменения аккаунта в таблице.
    def edit(self):
        B = []
        self.flag = 'edit'
        self.status['text'] = '[Изменение] Выберите имя и нажмите клавишу.'
        self.entry.delete(0, END)
        self.ma1n.wait_variable(self.variable)
        try:
            if self.line in self.A:
                for i in range(5):
                    self.status['text'] = f'[Изменение] Введите {self.columns[i]}. Старое: {self.line[i]} '
                    self.entry.delete(0, END)
                    self.ma1n.wait_variable(self.variable)
                    if self.entry.get() == '':
                        B.append(str(self.line[i]))
                    else:
                        B.append(str(self.entry.get()))
                        self.entry.delete(0, END)
                self.A.append(B)
                self.A.remove(self.line)
            else:
                self.status['text'] = '[Изменение] Что-то пошло не так.'
        except AttributeError:
            self.status['text'] = '[Изменение] Строчка не существует.'
        self.every()

    # Функция удаления аккаунта из таблицы.
    def delete(self):
        self.flag = 'delete'
        self.status['text'] = '[Удаление] Выберите имя и нажмите клавишу.'
        self.entry.delete(0, END)
        self.ma1n.wait_variable(self.variable)
        try:
            if self.line in self.A:
                self.A.remove(self.line)
            else:
                self.status['text'] = '[Удаление] Что-то пошло не так.'
        except NameError:
            pass
        except AttributeError:
            self.status['text'] = '[Удаление] Строчка не существует.'
        self.every()

    # Функция генерации случайного пароля.
    @staticmethod
    def generate():
        _3 = Generator()

    # Функция вывода окна с настройками приложения.
    def settings(self):
        pass

    # Функция отладки (с консолью).
    def debug(self):
        try:
            self.every()
            print('len(A) = ', len(self.A))
            print(f'len(A[i]) = {len(self.A[0])}')
            for i in self.tree.get_children():
                print(self.tree.item(i)['values'])
            print('\n')
            for i in range(len(self.A)):
                print(self.A[i])
        except IndexError:
            pass

    # Функция шифрования и сохранения базы в файл.
    def save(self):
        with open(self.filepath, 'w', encoding='UTF-8') as file:
            for i in range(len(self.A)):
                for j in range(len(self.A[i])):
                    file.write(str(self.A[i][j]) + '▓')
                file.write('\n')
        with open(self.filepath, 'rb') as file:
            encrypted_data = self.f.encrypt(file.read())
        with open(self.filepath, 'wb') as file:
            file.write(encrypted_data)

    # Функция закрытия приложения.
    def close(self):
        self.save()  # Функция сохранения
        raise SystemExit  # Выход

    # Дизайн боковой панели
    def taskbar(self):
        taskbar = Frame(bg=self.style[0])
        taskbar.pack(side=LEFT, fill=Y)
        Button(taskbar, image=self.img_add, compound='left', relief=FLAT, bg=self.style[0], command=self.add).pack(expand=1, anchor=NW)
        Button(taskbar, image=self.img_chng, compound='left', relief=FLAT, bg=self.style[0], command=self.edit).pack(expand=1, anchor=NW)
        Button(taskbar, image=self.img_del, compound='left', relief=FLAT, bg=self.style[0], command=self.delete).pack(expand=1, anchor=NW)
        Button(taskbar, image=self.img_gnrt, compound='left', relief=FLAT, bg=self.style[0], command=self.generate).pack(expand=1, anchor=NW)
        Button(taskbar, image=self.img_sett, compound='left', relief=FLAT, bg=self.style[0], command=self.settings).pack(expand=1, anchor=NW)
        Button(taskbar, image=self.img_exit, compound='left', relief=FLAT, bg=self.style[0], command=self.close).pack(expand=1, anchor=NW)
        Button(taskbar, image=self.img_debug, compound='left', relief=FLAT, bg=self.style[0], command=self.debug).pack(expand=1, anchor=NW)

    # Дизайн основного окна
    def data(self):
        self.toolbar = Frame(bg=self.style[0])
        self.toolbar.pack(side=TOP, fill=X)
        self.top_frame = Frame(self.toolbar, bg=self.style[0])
        self.top_frame.pack(side=TOP, fill=X)
        self.status = Label(self.top_frame, fg=self.style[2], width=63, height=1, bg=self.style[0])
        self.status.pack(side=LEFT, fill=X)
        self.variable = IntVar()
        self.send_btn = Button(self.top_frame, image=self.img_ent, relief=FLAT, bg=self.style[0], command=lambda: self.variable.set(1))
        self.send_btn.pack(side=RIGHT)
        self.entry = Entry(self.top_frame, fg=self.style[1], bg=self.style[0], relief=FLAT)
        self.entry.pack(side=RIGHT)
        self.bottom_frame = Frame(self.toolbar, bg=self.style[0])
        self.bottom_frame.pack(fill=BOTH, expand=1)
        self.stylei = ttk.Style()
        self.stylei.configure(".", font=('Consolas', 10))
        self.stylei.configure("Treeview.Heading", font=('Arial', 10, 'bold'), foreground='black')
        self.tree = ttk.Treeview(self.bottom_frame, show='headings', columns=self.columns)
        self.tree.heading('название', text='Название')
        self.tree.column('название', width=95)
        self.tree.heading('вебсайт', text='Вебсайт')
        self.tree.column('вебсайт', width=185)
        self.tree.heading('логин', text='Логин')
        self.tree.column('логин', width=172)
        self.tree.heading('пароль', text='Пароль')
        self.tree.column('пароль', width=250)
        self.tree.heading('заметки', text='Заметки')
        self.tree.bind('<<TreeviewSelect>>', self.select)
        self.bar = ttk.Scrollbar(self.bottom_frame, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.bar.set)
        self.tree.pack(side=LEFT, fill=BOTH, expand=1)
        self.bar.pack(side=RIGHT, fill=Y)


# Класс для окна генерации пароля.
class Generator:
    def __init__(self):
        self.symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        self.values = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 62]
        self.generated_password = ''
        self.generator = Tk()
        self.generator.title("Password Generator")
        self.generator.attributes("-topmost", True)
        self.password_label = Label(self.generator, text='')
        self.password_label.grid(row=0, column=0, columnspan=3)
        self.combo = ttk.Combobox(self.generator, values=self.values, state="readonly")
        self.combo.current(8)
        self.combo.grid(row=1, column=0, columnspan=3)
        self.status_generator = Label(self.generator, text='Выберите длину:')
        self.status_generator.grid(row=3, column=0, columnspan=3)
        Button(self.generator, text="Generate", command=self.generate_output).grid(row=2, column=0)
        Button(self.generator, text="Copy", command=self.generate_copy).grid(row=2, column=1)
        Button(self.generator, text="Close", command=self.generator.destroy).grid(row=2, column=2)
        self.generator.mainloop()

    # Функция вывода сгенерированного пароля в окне генерации.
    def generate_output(self):
        self.generated_password = str(
            ''.join(sample(self.symbols, int(self.combo.get()))))  # Создаём пароль из случайных символов
        self.password_label['text'] = self.generated_password  # Выводим пароль в Label

    # Функция копирования сгенерированного пароля в окне генерации.
    def generate_copy(self):
        try:
            copy(self.generated_password)  # Пытаемся скопировать пароль
            self.status_generator['text'] = 'Скопировано'  # Выводим статус в окно для статуса
        except NameError:  # Если нет пароля
            self.status_generator['text'] = 'Ничего нет.'  # Выводим ошибку в окно для статуса


if __name__ == '__main__':
    _1 = Start()
