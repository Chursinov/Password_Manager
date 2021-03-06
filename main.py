from cryptography.fernet import Fernet, InvalidToken  # Модули для ключа и ошибки ключа
from tkinter import *  # Модуль GUI
import tkinter.ttk as ttk  # Модуль виджетов GUI
from PIL import ImageTk  # Модуль для связи GUI и изображений
from PIL import Image as Img  # Модуль для  изображений
from pyperclip import copy  # Модуль для копирования текста в буфер обмена
from random import sample  # Модуль рандом для генерации пароля


login = 'key'
password = '1'


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
        self.img_lock1 = ImageTk.PhotoImage(Img.open('textures.png').crop((83, 1, 130, 49)))
        self.img_touch1 = ImageTk.PhotoImage(Img.open('textures.png').crop((1, 1, 65, 65)))
        self.img_lock2 = ImageTk.PhotoImage(Img.open('textures.png').crop((83, 50, 130, 98)))
        self.img_touch2 = ImageTk.PhotoImage(Img.open('textures.png').crop((1, 66, 65, 130)))
        self.img_enter = ImageTk.PhotoImage(Img.open('textures.png').crop((103, 1, 119, 17)))
        self.img_voice = ImageTk.PhotoImage(Img.open('textures.png').crop((66, 55, 82, 71)))
        self.img_visible0 = ImageTk.PhotoImage(Img.open('textures.png').crop((66, 28, 82, 54)))
        self.img_visible1 = ImageTk.PhotoImage(Img.open('textures.png').crop((66, 1, 82, 27)))

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
        _ = Ma1n()


# Класс для основного окна.
class Ma1n:
    # Инициализация переменных.
    def __init__(self):
        self.A = []  # Обозначаем пустой список
        self.flag = False
        self.line = []  # Флаг  выделения строки для копирования
        self.symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        self.values = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 62]
        self.generated_password = ''
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
        self.style = {'bg': '#3C8080', 'fg': '#C38080', 'text': '#C38080'}  # Резервный стиль (стандартная тема)

        self.ma1n = Tk()  # Переменная ma1n это GUI окно
        self.ma1n.geometry('975x400+50+50')
        self.ma1n.title('Password Manager')  # Меняем имя главного окна
        self.ma1n.attributes("-topmost", True)
        self.ma1n.overrideredirect(True)
        self.ma1n.resizable(False, True)
        self.ma1n.configure(bg=self.style['bg'])  # Меняем главному окну стиль
        self.ma1n.bind('<Return>', lambda event: self.variable.set(1))
        self.img_add = ImageTk.PhotoImage(Img.open(self.texture).crop((131, 1, 179, 49)))
        self.img_chng = ImageTk.PhotoImage(Img.open(self.texture).crop((131, 50, 179, 98)))
        self.img_del = ImageTk.PhotoImage(Img.open(self.texture).crop((180, 1, 228, 49)))
        self.img_gnrt = ImageTk.PhotoImage(Img.open(self.texture).crop((180, 50, 228, 98)))
        self.img_2fa = ImageTk.PhotoImage(Img.open(self.texture).crop((278, 1, 326, 49)))
        self.img_card = ImageTk.PhotoImage(Img.open(self.texture).crop((278, 50, 326, 98)))
        self.img_sett = ImageTk.PhotoImage(Img.open(self.texture).crop((229, 1, 277, 49)))
        self.img_exit = ImageTk.PhotoImage(Img.open(self.texture).crop((229, 50, 277, 98)))
        self.img_ent = ImageTk.PhotoImage(Img.open(self.texture).crop((66, 89, 82, 105)))

        self.taskbar = Frame(self.ma1n, bg=self.style['bg'])
        Button(self.taskbar, image=self.img_add, relief=FLAT, border='0', bg=self.style['bg'], command=self.add).pack()
        Button(self.taskbar, image=self.img_chng, relief=FLAT, border='0', bg=self.style['bg'], command=self.edit).pack()
        Button(self.taskbar, image=self.img_del, relief=FLAT, border='0', bg=self.style['bg'], command=self.delete).pack()
        Button(self.taskbar, image=self.img_gnrt, relief=FLAT, border='0', bg=self.style['bg'], command=lambda: self.generate()).pack()
        Button(self.taskbar, image=self.img_2fa, relief=FLAT, border='0', bg=self.style['bg'], command=lambda: self.twofactor()).pack()
        Button(self.taskbar, image=self.img_card, relief=FLAT, border='0', bg=self.style['bg'], command=lambda: self.card()).pack()
        Button(self.taskbar, image=self.img_sett, relief=FLAT, border='0', bg=self.style['bg'], command=lambda: self.settings()).pack()
        Button(self.taskbar, image=self.img_exit, relief=FLAT, border='0', bg=self.style['bg'], command=self.close).pack()
        self.taskbar.place(x=0, y=0)
        self.toolbar = Frame(self.ma1n, bg=self.style['bg'])
        self.top_frame = Frame(self.toolbar, bg=self.style['bg'])
        self.variable = IntVar()
        self.status = Label(self.top_frame, fg=self.style['text'], width=63, height=1, bg=self.style['bg'])
        self.entry = Entry(self.top_frame, fg=self.style['fg'], bg=self.style['bg'], relief=FLAT)
        self.send_btn = Button(self.top_frame, image=self.img_ent, relief=FLAT, border='0', bg=self.style['bg'], command=lambda: self.variable.set(1))
        self.status.place(x=0, y=0, width=708, height=20)
        self.entry.place(x=708, y=0, width=200, height=20)
        self.send_btn.place(x=907, y=0)
        self.top_frame.place(x=0, y=0, width=925, height=22)
        self.bottom_frame = Frame(self.toolbar, bg=self.style['bg'])
        self.stylei = ttk.Style(self.bottom_frame)
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
        self.tree.place(x=0, y=0, width=905, height=480)
        self.bar.place(x=906, y=0, width=20, height=480)
        self.bottom_frame.place(x=0, y=23, width=925, height=478)

        self.generator_frame = Frame(self.toolbar)
        self.password_label = Label(self.generator_frame, text='', font=('Consolas', 10))
        self.combo = ttk.Combobox(self.generator_frame, values=self.values, state="readonly")
        self.combo.current(8)
        self.status_generator = Label(self.generator_frame, text='Выберите длину:')
        self.toolbar.place(x=50, y=0, width=925, height=400)

        self.twofactor_frame = Frame(self.toolbar)
        self.twofactor_label = Label(self.twofactor_frame, text='Коды 2 факторной аутентификации', font=('Consolas', 10))

        self.card_frame = Frame(self.toolbar)
        self.card_label = Label(self.card_frame, text='Кредитные карты', font=('Consolas', 10))

        self.settings_frame = Frame(self.toolbar)
        self.tip_label = Label(self.settings_frame, text='Введите цвет фона и цвет текста приложения', font=('Consolas', 10))
        self.preview_label = Label(self.settings_frame, text='Так будет выглядеть текст', font=('Consolas', 10))
        self.bg_color_entry = Entry(self.settings_frame, font=('Consolas', 10))
        self.fg_color_entry = Entry(self.settings_frame, font=('Consolas', 10))
        self.preview_button = Button(self.settings_frame, text='Предпросмотр', relief=FLAT, border='0', command=lambda: self.change_preview())
        self.change_button = Button(self.settings_frame, text='Изменить', relief=FLAT, border='0', command=lambda: self.change_theme())
        self.settings_label = Label(self.settings_frame, text='Настройки', font=('Consolas', 10))

        self.load()
        self.ma1n.mainloop()  # Запуск главного окна

    # Функция нажатия на столбец по выбору.
    def select(self, _event):
        if not self.flag:  # Если флажок по умолчанию = True
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

    # Функция декодирования и загрузки базы из файла.
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
        if not self.flag:
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
        else:
            pass

    # Функция изменения аккаунта в таблице.
    def edit(self):
        if not self.flag:
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
        else:
            pass

    # Функция удаления аккаунта из таблицы.
    def delete(self):
        if not self.flag:
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
        else:
            pass

    # Функция генерации случайного пароля.
    def generate(self):
        if not self.flag:
            self.flag = 'generate'
            self.bottom_frame.place_forget()
            self.password_label.grid(row=0, column=0, columnspan=3)
            self.combo.grid(row=1, column=0, columnspan=3)
            Button(self.generator_frame, text="Генерировать", command=self.generate_output).grid(row=2, column=0)
            Button(self.generator_frame, text="Скопировать", command=self.generate_copy).grid(row=3, column=0)
            self.status_generator.grid(row=5, column=0, columnspan=3)
            self.generator_frame.place(x=0, y=23, width=925, height=278)
        else:
            if self.flag == 'generate':
                self.flag = False
                self.generator_frame.place_forget()
                self.bottom_frame.place(x=0, y=23, width=925, height=278)

    # Функция вывода окна с кодами 2FA.
    def twofactor(self):
        if not self.flag:
            self.flag = '2fa'
            self.bottom_frame.place_forget()
            self.twofactor_label.place(x=0, y=0)
            self.twofactor_frame.place(x=0, y=23, width=925, height=278)
        else:
            if self.flag == '2fa':
                self.flag = False
                self.twofactor_frame.place_forget()
                self.bottom_frame.place(x=0, y=23, width=925, height=278)

    # Функция вывода окна с кредитными картами.
    def card(self):
        if not self.flag:
            self.flag = 'card'
            self.bottom_frame.place_forget()
            self.card_label.place(x=0, y=0)
            self.card_frame.place(x=0, y=23, width=925, height=278)
        else:
            if self.flag == 'card':
                self.flag = False
                self.card_frame.place_forget()
                self.bottom_frame.place(x=0, y=23, width=925, height=278)

    # Функция вывода окна с настройками приложения.
    def settings(self):
        if not self.flag:
            self.flag = 'settings'
            self.bottom_frame.place_forget()

            self.settings_label.place(x=50, y=50, height=25)
            self.tip_label.place(x=50, y=100, height=25)
            self.bg_color_entry.place(x=50, y=125, width=100, height=25)
            self.fg_color_entry.place(x=150, y=125, width=100, height=25)
            self.preview_button.place(x=250, y=125, width=100, height=25)
            self.preview_label.place(x=50, y=150, width=200, height=25)
            self.change_button.place(x=250, y=150, width=100, height=25)
            self.settings_frame.place(x=0, y=23, width=925, height=278)
        else:
            if self.flag == 'settings':
                self.flag = False
                self.settings_frame.place_forget()
                self.bottom_frame.place(x=0, y=23, width=925, height=278)

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
        if not self.flag:
            self.save()  # Функция сохранения
            raise SystemExit  # Выход
        else:
            pass

    # Метод вывода сгенерированного пароля в окне генерации.
    def generate_output(self):
        self.generated_password = str(
            ''.join(sample(self.symbols, int(self.combo.get()))))  # Создаём пароль из случайных символов
        self.password_label['text'] = self.generated_password  # Выводим пароль в Label

    # Метод копирования сгенерированного пароля в окне генерации.
    def generate_copy(self):
        try:
            copy(self.generated_password)  # Пытаемся скопировать пароль
            self.status_generator['text'] = 'Скопировано'  # Выводим статус в окно для статуса
        except NameError:  # Если нет пароля
            self.status_generator['text'] = 'Ничего нет.'  # Выводим ошибку в окно для статуса

    # Метод изменения темы для ознакомления
    def change_preview(self):
        try:
            self.preview_label.config(bg=self.bg_color_entry.get(), fg=self.fg_color_entry.get())
        except Exception as e:
            self.tip_label.config(text=e)

    # Метод изменения темы для всего приложения
    def change_theme(self):
        try:
            self.style['bg'] = self.bg_color_entry.get()
            self.style['fg'] = self.fg_color_entry.get()
            self.taskbar.config(bg=self.style['bg'])
            self.toolbar.config(bg=self.style['bg'])
            self.top_frame.config(bg=self.style['bg'])
            self.status.config(bg=self.style['bg'])
            self.entry.config(bg=self.style['bg'], fg=self.style['fg'])
            self.send_btn.config(bg=self.style['bg'])
            self.bottom_frame.config(bg=self.style['bg'])

            self.ma1n.configure(bg=self.style['bg'])
        except Exception as e:
            self.tip_label.config(text=e)


if __name__ == '__main__':
    _ = Start()
