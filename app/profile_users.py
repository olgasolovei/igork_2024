import tkinter as tk
from tkinter import messagebox


class ProfileScreen:
    def __init__(self, master, callback_change_password, callback_logout):
        self.master = master
        self.master.title("Профіль користувача")
        self.master.geometry("300x250")

        # Інформація про користувача
        self.user_info_label = tk.Label(
            master, text="Ім'я: Admin\nРоль: Оператор крана", font=("Arial", 12))
        self.user_info_label.pack(pady=20)

        # Кнопка зміни пароля
        self.change_password_button = tk.Button(
            master, text="Змінити пароль", command=callback_change_password)
        self.change_password_button.pack(pady=10)

        # Кнопка виходу
        self.logout_button = tk.Button(
            master, text="Вийти", command=callback_logout)
        self.logout_button.pack(pady=10)
