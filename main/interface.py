import tkinter as tk;
import tkinter.messagebox as mBox;
import main_app;
from tkinter import filedialog
import os
# Setting up the window
root = tk.Tk()
root.geometry("800x500")
root.title("Automatic Job Application Applier")

# Browser Options
OPTIONS = [
    "Chrome",
    "Edge",
    "FireFox"
]

browser_value = tk.StringVar(root)
browser_value.set(OPTIONS[0])

username = os.environ.get('USERNAME')
browser_location = tk.StringVar(root)
browser_location.set("C:\Program Files\Google\Chrome\Application")
menu = tk.OptionMenu(root, browser_value, *OPTIONS)

def setBrowserLocation():
    filename = filedialog.askopenfilename()
    browser_location.set(filename)
    print("Selected: ", filename)


# Setting up entry fields
inputs = ["email", "password", "Job Title","Location", "Link", "Browser", "Select Location", "Browser Location"]
fields = []
labels = []

i = 0
# Goes through all the input values needed and adds them to the grid in a more dynamic matter
for input in inputs:
    if input == "Browser":
        e = tk.OptionMenu(root, browser_value, *OPTIONS)
    elif input == "Select Location":
        e = tk.Button(root, text="Select Browser Location", command=setBrowserLocation)
    elif input == "Browser Location":
        e = tk.Entry(root, textvariable=browser_location)
    else:
        e = tk.Entry(root)    

    e.grid(row=i, column = 1)
    fields.append(e)


    lb = tk.Label(root, text=input + ":")
    lb.grid(row=i, column=0)
    labels.append(lb)
    i += 1

fields.append(menu)



# # A function that runs the selenium script
def run_apply():
    print("Attempting to apply")
    result = main_app.apply(fields[4].get(), browser_value.get(), fields[7].get(), ["user", "pass"],)
    if result == 1:
        mBox.showinfo("Success", "It appears that your application was successfully submitted!")
    elif result == 15:
        mBox.showinfo("Failure", "It appears there was an issue with opening your browser.")

link_apply = tk.Button(root, text="Apply to link", command=run_apply)
link_apply.place(relx=0.6, rely=0.9, anchor=tk.CENTER)
root.mainloop()
