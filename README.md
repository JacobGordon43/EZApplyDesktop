# EZApply Desktop
### Description
The desktop application utilized tkinter for an interface. A start file determines if a user is logged in or not and displays the corresonding UI as needed. Once a user is logged in, they a UI pops up that allows a user to enter in a job link. A python selenium file then automates the job application process by using identifying keywords to locate the inputs to then enter in the corresponding values. When they log in, there job data is obtained from the database and stored, then formatted and stored again in the correct format so that it can be utilized by the software. Additionally, there is a button on the main UI that allows you to retrieve an updated version of your data from the database. A logout button deletes your files so that the start file can identify that you are no longer logged in.

### The Problem And Solution
To obtain a job, you must repeatedly apply to job after job. Many of these asks the same questions, from personal information to lengthy job and education history. Additionally, it can take 100-200 job applications to land a job, resulting in what can be countless hours wasted on job applications alone. EZApply's Desktop application focuses on solving this issue by automating the process, filling out commonly asked questions to reduce minutes off each application you do.

### Technologies
* Python
* Selenium
* WebDriver
* Tkinter
  
### What I learned
The biggest thing I learned was how to use selenium to effeciently manipulate a website to navigate through it. I also learned how to get around certain ways that websites try to block automation through shadow DOMs, which attempt to prevent the automation from clicking on certian things, i.e. buttons.

### Current Limitations
As it is, the software is not dynamic enough to work on a larger variety of job applications. It only works on Workday applications, a result of how it identifies that it has reached a job application. It has logic that allows it to login, create an account, and click on apply so that it can access on job application. However, once on the application, it looks for "My Experience", an implementation that was done at the time to help get the process going, and as I testing other websites I would add more identifying keywords. This, however, never became the case, thus allowing it to only work on Workday. Additionally, at times the software may mess up, for example it does not always select 'Arizona' as the state but rather Arkansas. The software is also able to automate questiosn that are found in most applications, i.e. work history, first and last name, etc., however it is limited in the sense that there are a lot of questions that it can't answer, such as whether they've worked for the company, why they want to work for the company, etc.. Another big limitation is the lack of browser support. Initially, the plan was to allow Chrome, Edge, and FireFox be able to run this program, with the user having the option to select the browser from the start. However, it became apparent that this was not something that I could implement easily and instead focused my time and attention to the many other features that had to be developed beforehand.

### Functional and Non-Functional Requirements
There were a great deal of requirements for the desktop application, with the following being the primary/largest in-scope:
* Functional
  * Login/Logout
  * Fill out a job application
  * Navigate to a job application
  * Retrieve user's data from the database
* Non-Functional
  * Be able to select Chrome, Edge, or FireFox to run the software
    
### Flowcharts
![image](https://github.com/JacobGordon43/EZApplyDesktop/assets/77366005/7d3d1b5f-2bc2-4e9d-b984-c986441903f3)
This flowchart illustrates the general flow of the software. There are some parts that weren't fully implemented. such as browser version error. Rather than using a different library, it instead now will display an error message. Most of the rest of the logic still holes true, from finding the application to how it handles history, identifying different types of inputs and handling them, etc.
![image](https://github.com/JacobGordon43/EZApplyDesktop/assets/77366005/d9037dbc-8836-4329-bd48-03c8c3d3925c)
This flowchart shows how it finds the application by identifying aspects of the website, such as apply buttons, login content, etc., and how to handle it. There have been some alterations, such as the logic being more of in a loop logic rather than apply > login > form.


### Code Snippets
![image](https://github.com/JacobGordon43/EZApplyDesktop/assets/77366005/8b874e05-7d15-4739-9b1e-0ca449292077)
This rather small function handles the entire logic for completing an application. It first finds the application by repeatedly running a function until it identifies that it found the actual application. Then, a new loop starts that runs the logic of identifying questions and inserting values to the corresponding input.

![image](https://github.com/JacobGordon43/EZApplyDesktop/assets/77366005/f98b64fe-9816-484a-b352-c7ea5bced744)
This snippet handles running the various specific aspects of application process. For example, it identifies whether or not there is a Work Section in the application, which if there is, it will run the logic to handle that accordingly.

![image](https://github.com/JacobGordon43/EZApplyDesktop/assets/77366005/45f2ffb2-329c-4f96-97c7-31791e55228a)
This further shows how the functions displayed above work. Each one is similar, but it uses a find_elements to see if it's on the application. It goes through each element and sees if it is displayed, which is how it identifies that it can access that part of the application. If it is found, it then will run a function that lets it handle education and work history
![image](https://github.com/JacobGordon43/EZApplyDesktop/assets/77366005/bd8043de-2ab5-4f08-837a-b8af0d5118ad)
There is a lot of logic that goes into finding an input for the questions, but ultimately this function is ran and enters in the input, and ensures that it is done correctly by entering. This helps with certain inputs as typing isn't enough to get the answer, such as selecting the source of how you found the job listing.

