import tkinter as tk
from tkinter import messagebox


class ChangePasswordScreen:
    def __init__(self, master, callback_profile):
        self.master = master
        self.master.title("Зміна пароля")
        self.master.geometry("300x250")

        # Поля для старого і нового пароля
        self.old_password_label = tk.Label(master, text="Старий пароль")
        self.old_password_label.pack(pady=10)
        self.old_password_entry = tk.Entry(master, show="*")
        self.old_password_entry.pack(pady=5)

        self.new_password_label = tk.Label(master, text="Новий пароль")
        self.new_password_label.pack(pady=10)
        self.new_password_entry = tk.Entry(master, show="*")
        self.new_password_entry.pack(pady=5)

        # Кнопки
        self.save_button = tk.Button(
            master, text="Зберегти", command=self.change_password)
        self.save_button.pack(pady=10)

        self.back_button = tk.Button(
            master, text="Назад", command=callback_profile)
        self.back_button.pack(pady=10)

    def change_password(self):
        old_password = self.old_password_entry.get()
        new_password = self.new_password_entry.get()

        if old_password == "1234" and new_password:
            messagebox.showinfo("Пароль змінено", "Пароль успішно змінено.")
        else:
            messagebox.showerror(
                "Помилка", "Невірний старий пароль або новий пароль порожній.")
