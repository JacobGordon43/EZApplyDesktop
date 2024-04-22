# EZApply Desktop
### Description
The desktop application utilized tkinter for an interface. A start file determines if a user is logged in or not and displays the corresonding UI as needed. Once a user is logged in, they a UI pops up that allows a user to enter in a job link. A python selenium file then automates the job application process by using identifying keywords to locate the inputs to then enter in the corresponding values. When they log in, there job data is obtained from the database and stored, then formatted and stored again in the correct format so that it can be utilized by the software. Additionally, there is a button on the main UI that allows you to retrieve an updated version of your data from the database. A logout button deletes your files so that the start file can identify that you are no longer logged in.

### What I learned
The biggest thing I learned was how to use selenium to effeciently manipulate a website to navigate through it. I also learned how to get around certain ways that websites try to block automation through shadow DOMs, which attempt to prevent the automation from clicking on certian things, i.e. buttons.
