import tkinter as tk
from tkinter import messagebox


class LoginScreen:
    def __init__(self, master, callback):
        self.master = master
        self.master.title("Авторизація")
        self.master.geometry("300x250")

        self.callback = callback

        # Логін
        self.login_label = tk.Label(master, text="Логін")
        self.login_label.pack(pady=10)
        self.login_entry = tk.Entry(master)
        self.login_entry.pack(pady=5)

        # Пароль
        self.password_label = tk.Label(master, text="Пароль")
        self.password_label.pack(pady=10)
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack(pady=5)

        # Кнопка увійти
        self.login_button = tk.Button(
            master, text="Увійти", command=self.check_credentials)
        self.login_button.pack(pady=10)

        # Кнопка відновлення пароля
        self.forgot_button = tk.Button(
            master, text="Забули пароль?", command=self.forgot_password)
        self.forgot_button.pack(pady=5)

    def check_credentials(self):
        login = self.login_entry.get()
        password = self.password_entry.get()

        if login == "admin" and password == "1234":
            self.callback()
        else:
            messagebox.showerror("Помилка", "Невірний логін або пароль")

    def forgot_password(self):
        messagebox.showinfo("Відновлення пароля", "Інструкції на вашу пошту.")
