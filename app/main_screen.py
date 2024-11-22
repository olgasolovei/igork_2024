import tkinter as tk
from tkinter import messagebox


class MainScreen:
    def __init__(self, master, callback_profile):
        self.master = master
        self.master.title("Головний екран")
        self.master.geometry("400x400")

        # Інформаційна панель про погодні умови та ризик
        self.info_panel = tk.Label(
            master, text="Поточні умови на майданчику:\nВітер: 15 км/год\nТемпература: 25°C", font=("Arial", 12))
        self.info_panel.pack(pady=20)

        # Індикатор ризику (зелений/жовтий/червоний)
        self.risk_level = "Низький"  # Це може змінюватись в залежності від даних
        self.risk_indicator = tk.Label(
            master, text=f"Ризик ураження струмом: {self.risk_level}", font=("Arial", 12), fg="green")
        self.risk_indicator.pack(pady=10)

        # Кнопка для перегляду прогнозу погоди та стану ліній електропередач
        self.forecast_button = tk.Button(
            master, text="Переглянути прогноз", command=self.view_forecast)
        self.forecast_button.pack(pady=10)

        # Кнопка для перегляду сповіщень
        self.notifications_button = tk.Button(
            master, text="Переглянути сповіщення", command=self.view_notifications)
        self.notifications_button.pack(pady=10)

        # Кнопка для переходу до профілю користувача
        self.profile_button = tk.Button(
            master, text="Профіль", command=callback_profile)
        self.profile_button.pack(pady=10)

    def view_forecast(self):
        # Створення нового вікна для показу прогнозу
        forecast_window = tk.Toplevel(self.master)
        forecast_window.title("Прогноз погоди та стан ліній електропередач")
        forecast_window.geometry("400x300")

        # Інформація про прогноз
        forecast_label = tk.Label(
            forecast_window, text="Прогноз на сьогодні:\n- Швидкість вітру: 20 км/год\n- Температура: 18°C\n- Можливі небезпечні умови: сильний вітер.", font=("Arial", 12))
        forecast_label.pack(pady=20)

        # Кнопка для закриття вікна
        close_button = tk.Button(
            forecast_window, text="Закрити", command=forecast_window.destroy)
        close_button.pack(pady=10)

    def view_notifications(self):
        # Створення нового вікна для перегляду сповіщень
        notifications_window = tk.Toplevel(self.master)
        notifications_window.title("Сповіщення")
        notifications_window.geometry("400x300")

        # Список сповіщень
        notifications_text = "1. Небезпека ураження струмом через контакт з лінією.\n2. Сильний вітер на майданчику.\n3. Перевищення допустимого рівня вологи."
        notifications_label = tk.Label(
            notifications_window, text=notifications_text, font=("Arial", 12), justify=tk.LEFT)
        notifications_label.pack(pady=20)

        # Кнопка для закриття вікна
        close_button = tk.Button(
            notifications_window, text="Закрити", command=notifications_window.destroy)
        close_button.pack(pady=10)

    def update_risk_level(self, new_risk_level):
        # Оновлення рівня ризику в залежності від умов
        self.risk_level = new_risk_level
        self.risk_indicator.config(
            text=f"Ризик ураження струмом: {self.risk_level}")
        if self.risk_level == "Низький":
            self.risk_indicator.config(fg="green")
        elif self.risk_level == "Середній":
            self.risk_indicator.config(fg="yellow")
        elif self.risk_level == "Високий":
            self.risk_indicator.config(fg="red")

    def update_weather_info(self, new_weather_info):
        # Оновлення погодних умов
        self.info_panel.config(
            text=f"Поточні умови на майданчику:\n{new_weather_info}")
