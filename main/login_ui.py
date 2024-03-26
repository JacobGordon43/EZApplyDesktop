import requests
import aws
import json
import tkinter as tk
from tkinter import Label
import tkinter.messagebox as mBox
# import interface
def login():
    # mBox.showinfo("Credentials", ("Credentials are ", username_entry.get(), "and ", password_entry.get()))
    url = aws.login_url
    headers = {"Content-Type": "application/json"}
    params = {}
    data = json.dumps({"email": username_entry.get(), "password": password_entry.get()})
    print(data)
    response = requests.post(url=url, headers=headers, data=data)
    print(json.loads(response.text))
    print(response.status_code)
    if(response.status_code == 200):
        import interface
        root.destroy()

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

login_btn = tk.Button(text="Login", command=login)
login_btn.place(relx=.5, rely=.7, anchor="center", width=70, height=30)
root.mainloop()