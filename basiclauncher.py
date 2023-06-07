# Quartz Dev.

import tkinter as tk
from tkinter import filedialog
import os

def save_file_path(file_path, app_name):
    with open('app_list.txt', 'a') as file:
        file.write(file_path + ',' + app_name + '\n')
    create_app_button(window, file_path, app_name)

def delete_file_path(app_path):
    with open('app_list.txt', 'r') as file:
        lines = file.readlines()
    with open('app_list.txt', 'w') as file:
        for line in lines:
            if line.split(',')[0].strip() != app_path:
                file.write(line)
    refresh_app_buttons()

def create_app_button(window, app_path, app_name):
    button_frame = tk.Frame(window)
    button_frame.pack()
    button = tk.Button(button_frame, text=app_name if app_name else app_path.split('/')[-1], command=lambda: launch_app(app_path))
    button.pack(side=tk.LEFT)
    delete_button = tk.Button(button_frame, text="Sil", command=lambda app=app_path: delete_file_path(app))
    delete_button.pack(side=tk.LEFT)
    app_buttons.append(button_frame)

def launch_app(path):
    os.startfile(path)

def open_file_dialog():
    app_path = filedialog.askopenfilename(filetypes=[("Executable Files", "*.exe")])
    if app_path:
        name_window = tk.Toplevel(window)
        name_window.title("Uygulama İsmi")
        name_entry = tk.Entry(name_window)
        name_entry.pack(padx=10, pady=10)

        def save_name():
            app_name = name_entry.get()
            name_window.destroy()
            save_file_path(app_path, app_name)

        save_button = tk.Button(name_window, text="Kaydet", command=save_name)
        save_button.pack(pady=10)

def refresh_app_buttons():
    for button in app_buttons:
        button.pack_forget()  # Mevcut düğmeleri pencereden kaldır
    app_buttons.clear()

    with open('app_list.txt', 'r') as file:
        app_data = file.read().splitlines()
        for app_entry in app_data:
            app_path, app_name = app_entry.split(',')
            create_app_button(window, app_path, app_name)

window = tk.Tk()
window.title("Quartzz Launcher V1")

menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Dosya", menu=file_menu)
file_menu.add_command(label="Uygulama Ekle", command=open_file_dialog)
file_menu.add_separator()
file_menu.add_command(label="Hakkında", command=lambda: show_about_dialog())

def show_about_dialog():
    about_window = tk.Toplevel(window)
    about_window.title("Hakkında")
    about_label = tk.Label(about_window, text="Yapımcı: Quartzz#1535 - Qua Dev.")
    about_label.pack(padx=10, pady=10)

app_buttons = []
with open('app_list.txt', 'r') as file:
    app_data = file.read().splitlines()
    for app_entry in app_data:
        app_path, app_name = app_entry.split(',')
        create_app_button(window, app_path, app_name)

window.mainloop()
