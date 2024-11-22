import tkinter as tk
from login import LoginScreen
from main_screen import MainScreen
from profile_users import ProfileScreen
from change_password import ChangePasswordScreen


def open_main_screen():
    root.withdraw()
    main_screen = tk.Tk()
    MainScreen(main_screen, open_profile_screen)
    main_screen.mainloop()


def open_profile_screen():
    root.withdraw()
    profile_screen = tk.Tk()
    ProfileScreen(profile_screen, open_change_password_screen,
                  open_login_screen)
    profile_screen.mainloop()


def open_change_password_screen():
    root.withdraw()
    change_password_screen = tk.Tk()
    ChangePasswordScreen(change_password_screen, open_profile_screen)
    change_password_screen.mainloop()


def open_login_screen():
    root.deiconify()
    login_screen = tk.Tk()
    LoginScreen(login_screen, open_main_screen)
    login_screen.mainloop()


root = tk.Tk()
open_login_screen()
root.mainloop()
