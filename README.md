# EZApply Desktop
### Description
The desktop application utilized tkinter for an interface. A start file determines if a user is logged in or not and displays the corresonding UI as needed. Once a user is logged in, they a UI pops up that allows a user to enter in a job link. A python selenium file then automates the job application process by using identifying keywords to locate the inputs to then enter in the corresponding values. When they log in, there job data is obtained from the database and stored, then formatted and stored again in the correct format so that it can be utilized by the software. Additionally, there is a button on the main UI that allows you to retrieve an updated version of your data from the database. A logout button deletes your files so that the start file can identify that you are no longer logged in.

### What I learned
The biggest thing I learned was how to use selenium to effeciently manipulate a website to navigate through it. I also learned how to get around certain ways that websites try to block automation through shadow DOMs, which attempt to prevent the automation from clicking on certian things, i.e. buttons.

### Current Limitations
As it is, the software is not dynamic enough to work on a larger variety of job applications. It only works on Workday applications, a result of how it identifies that it has reached a job application. It has logic that allows it to login, create an account, and click on apply so that it can access on job application. However, once on the application, it looks for "My Experience", an implementation that was done at the time to help get the process going, and as I testing other websites I would add more identifying keywords. This, however, never became the case, thus allowing it to only work on Workday. Additionally, at times the software may mess up, for example it does not always select 'Arizona' as the state but rather Arkansas. The software is also able to automate questiosn that are found in most applications, i.e. work history, first and last name, etc., however it is limited in the sense that there are a lot of questions that it can't answer, such as whether they've worked for the company, why they want to work for the company, etc.. Another big limitation is the lack of browser support. Initially, the plan was to allow Chrome, Edge, and FireFox be able to run this program, with the user having the option to select the browser from the start. However, it became apparent that this was not something that I could implement easily and instead focused my time and attention to the many other features that had to be developed beforehand.

### Functional and Non-Functional Requirements
There were a great deal of requirements for the desktop application:
* Work
> Work
