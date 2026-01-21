import os
import sys
from time import sleep
import tkinter as tk
from tkinter import messagebox
#-------------------------
root = tk.Tk()
root.geometry('600x400')
root.config(bg='black')
root.title('Python')
#-------------------------
main_label = tk.Label(root, text='System info.', fg='white', bg='black', font=('Cursive', 36))
main_label.pack(pady=20)
#-------------------------
def show_python_version():
    messagebox.showinfo('Python Version', sys.version)

def show_python_path():
    messagebox.showinfo('Python Path', sys.path)

def show_platform_information():
    messagebox.showinfo('Platform Info', sys.platform)

def list_current_directory():
    messagebox.showinfo('Current Directory', os.listdir())

def show_current_colder():
    messagebox.showinfo('Current folder', os.getcwd)

def os_cpu_count():
    messagebox.showinfo('Cpu count', os.cpu_count)

def get_login():
    messagebox.showinfo('Cpu count', os.getlogin)
#-------------------------
python_version_but = tk.Button(root, text='Python Version ', command=show_python_version)
python_version_but.pack(pady=20)

python_path_but = tk.Button(root, text='Python Path', command=show_python_path ,fg='cyan')
python_path_but.pack(pady=20)

platform_but = tk.Button(root, text='Platform', command=show_platform_information, fg='green')
platform_but.pack(pady=20)

os_but = tk.Button(root, text='LCMD', command=list_current_directory, fg='purple')
os_but.pack(pady=20)

ocurol_but = tk.Button(root, text='current folder', command=show_current_colder, fg='red')
ocurol_but.place(x=50, y=50)

ocurol_b2ut = tk.Button(root, text='CPU count', command=os_cpu_count, fg='blue')
ocurol_b2ut.place(x=50, y=100)

get_login_but = tk.Button(root, text='Login info', command=get_login, fg='magenta')
get_login_but.place(x=50, y=150)
#-------------------------


root.mainloop()