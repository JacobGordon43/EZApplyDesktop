import tkinter as tk;
import tkinter.messagebox as mBox;
import main_app;
from tkinter import filedialog
from tkinter import Label
import os
import shutil
from pathlib import Path
import sys
# Setting up the UI of the main window
main_ui = tk.Tk()
main_ui.geometry("800x500")
main_ui.title("EZApply")

# Browser Options
OPTIONS = [
    "Chrome",
    "Edge",
    "FireFox"
]

browser_value = tk.StringVar(main_ui)
browser_value.set(OPTIONS[0])

username = os.environ.get('USERNAME')
browser_location = tk.StringVar(main_ui)
browser_location.set("C:\Program Files\Google\Chrome\Application")

resume_location = tk.StringVar(main_ui)

menu = tk.OptionMenu(main_ui, browser_value, *OPTIONS)
# Logouts the user by deleting the necessary files and closing the window
def logout():
    #Uses error handling in the event that the file has already been deleted
    try:
        login_path = Path('./json/login.json')
        login_path.unlink()
    except Exception as e:
        print(e)
    try:
        register_path = Path('./json/create_account.json')
        register_path.unlink()
    except Exception as e:
        print(e)
    main_ui.destroy()

def setBrowserLocation():
    filename = filedialog.askopenfilename()
    browser_location.set(filename)
    print("Selected: ", filename)

def setResumeLocation():
    filename = filedialog.askopenfilename(filetypes=[("PDF", "*.pdf"), ("Word", "*.docx"), ("Word", "*.doc"), ("Text", "*.txt")])
    resume_location.set(filename)
    uploadResume(resume_location.get())
    print("Selected: ", filename)

# Uploads a selected pdf file resume from the users PC
def uploadResume(resume):
    try:
        # Locates the folder that contains the resume file
        folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '../uploadables/resume'))
        # Removes all files in the resume folder.
        for file in os.listdir(folder):
            path = os.path.join(folder, file)
            try:
                os.unlink(path)
            except Exception as e:
                print(e)
        # copies the resume selected and places it into the resume folder
        shutil.copy(resume, os.getcwd() + "/uploadables/resume")
        for field in fields:
            # Checks if the field is a labe
            if type(field) is Label:
                resume_path = os.getcwd() + "/uploadables/resume"
                resume_dir = os.listdir(resume_path)
                # Updates the Label to indicate the successful new file upload
                field.config(fg="green", text=resume_dir[0])
    
    except Exception as e:
        print(e)
        mBox.showinfo("Error", "There was an issue uploading your resume")

def update():
    print("Updating")

# Setting up entry fields
inputs = ["email", "password", "Job Title","Location", "Link", "Browser", "Select Location", "Browser Location", "Upload Resume", "Uploaded Resume"]
fields = []
labels = []

i = 0
# Goes through all the input values needed and adds them to the grid in a more dynamic matter
for input in inputs:
    if input == "Browser":
        e = tk.OptionMenu(main_ui, browser_value, *OPTIONS)
    elif input == "Select Location":
        e = tk.Button(main_ui, text="Select Browser Location", command=setBrowserLocation)
    elif input == "Browser Location":
        e = tk.Entry(main_ui, textvariable=browser_location)
    elif input == "Upload Resume":
        e = tk.Button(main_ui, text="Select Resume Location", command=setResumeLocation)
    elif input == "Uploaded Resume":
        resume_path = os.getcwd() + "/uploadables/resume"
        resume_dir = os.listdir(resume_path)
        if len(resume_dir) == 0:
            e = tk.Label(main_ui, text="No Resume Uploaded", fg="red")
        else:
            resume = resume_dir[0]
            e = tk.Label(main_ui, text=resume, fg="green")
    else:
        e = tk.Entry(main_ui)    

    e.grid(row=i, column = 1)
    fields.append(e)

    lb = tk.Label(main_ui, text=input + ":")
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
    elif result == 3:
        mBox.showinfo("Missing File", "It appears that an important file was missing, the application could not be filled out.")
    elif result == 4:
        mBox.showinfo("Failure", "There was an issue while filling out the application")
    elif result == 5:
        mBox.showinfo("Unknown File Error", "There was an with handling files.")
    elif result == 15:
        mBox.showinfo("Failure", "It appears there was an issue with opening your browser.")

link_apply = tk.Button(main_ui, text="Apply to link", command=run_apply)
link_apply.place(relx=0.6, rely=0.9, anchor=tk.CENTER)
logout_btn = tk.Button(main_ui, text="Logout", command=logout)
logout_btn.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
update_info_btn = tk.Button(main_ui, text="Update Information", command=update)
update_info_btn.place(relx=.38, rely="0.9", anchor=tk.CENTER)
main_ui.mainloop()
