import requests
import aws
import json
import tkinter as tk
from tkinter import Label
import tkinter.messagebox as mBox
import backend
# import interface
def login(username, password):
    status_code = backend.login(username, password)
    print(status_code)
    if(status_code == 200):
        root.destroy()
        import interface

root = tk.Tk()
root.geometry("800x500")
root.title("EZApply Login")
root.resizable(width=False, height=False)

inputs = ["email", "password"]
fields = []
labels = []
i = 0
# for input in inputs:
#     e = tk.Entry(root)
#     e.grid(row=i, column=0)
#     lb = tk.Label(root, text=input + ":")
#     lb.grid(row=i, column=1)
username_label = tk.Label(root, text="Username")
username_label.place(relx=.423, rely = .43,)
username_entry = tk.Entry(root)
username_entry.place(relx=.5, rely=.5, anchor="center")

password_label = tk.Label(root, text="Password")
password_label.place(relx=.423, rely = .54)
password_entry = tk.Entry(root, show="*")
password_entry.place(relx=.5, rely=.6, anchor="center")

login_btn = tk.Button(text="Login", command=lambda : login(username_entry.get(),password_entry.get()))
login_btn.place(relx=.5, rely=.7, anchor="center", width=70, height=30)
root.mainloop()