# EZApply Desktop
Selenium Desktop Github: https://github.com/JacobGordon43/EZApplyDesktop
Web Application Github: https://github.com/JacobGordon43/EZApplyNow
### Description
EZApply is a two application capstone consisting of a website and a desktop application. The website, made using Next.js, was made to allow users to create accounts and upload the data that they would enter into a job application. The desktop application utilized tkinter for an interface. A start file determines if a user is logged in or not and displays the corresonding UI as needed. Once a user is logged in, they a UI pops up that allows a user to enter in a job link. A python selenium file then automates the job application process by using identifying keywords to locate the inputs to then enter in the corresponding values. When they log in, there job data is obtained from the database and stored, then formatted and stored again in the correct format so that it can be utilized by the software. Additionally, there is a button on the main UI that allows you to retrieve an updated version of your data from the database. A logout button deletes your files so that the start file can identify that you are no longer logged in.

### The Problem And Solution
To obtain a job, you must repeatedly apply to job after job. Many of these asks the same questions, from personal information to lengthy job and education history. Additionally, it can take 100-200 job applications to land a job, resulting in what can be countless hours wasted on job applications alone. EZApply uses a website to allow users to upload their job application information (first/last name, phone, work/education, etc.). The Desktop application then focuses on solving using that data by automating the job application process, using the data uploaded to fill out commonly asked questions to reduce minutes off each application you do.

### Technologies
* Next.js (React Framework) - Selected as it is fast and server side rendering. It was also a new technology I wanted to try.
* TailwindCSS - Selected as it comes by default with Next.js. It also made frontend development very fast and easy
* TypeScript - Selected as it comes with Next.js by default, but I also was interested in further exploring this technology. I'm glad that I did as it pushed me a lot.
* AWS DynamoDB, API Gateway, Lambda Functions (written in Node.js) - I wanted to utilize AWS as much as I could in my capstone. This approach allowed me to do that while also having an entire RESTful API developed to handle my entire backend.
* Redux (Global State Management) - Redux is a commonly used technology in the industry for React applications. Global state management helped with reducing the number of calls being made to API by keeping the data persistent.
* Python - I wanted to learn Python as I see it listed as a desired language in a lot of job applciations
* Selenium - It's the most commonly used web automation library, which meant that it would have a lot of support and documentation that I could use as issues came up.
* Tkinter - I used this library for the UI end of the desktop since it was one of the easier libraries to use and I didn't need anything particularly fancy or complex.
  
### Challenges
The large scope was, in itself, a significant challenge as I had to learn various different technologies and have them all implemented so to have a functional end product. I initially had anticipated on being done with the website within 2-3 weeks, however it became riddled with issues and it's development took much longer than I anticipated. Integrating lambda functions with the API Gateway was also a major learning curve and took a lot of trial and error to get implemented, which slowed the development process down significantly. Once I reached the desktop application, I had lost a lot of the time I thought I would have to perfect it. 

### What I learned
The biggest thing I learned was how to use selenium to effeciently manipulate a website to navigate through it. I also learned how to get around certain ways that websites try to block automation through shadow DOMs, which attempt to prevent the automation from clicking on certian things, i.e. buttons.

### Current Limitations
The Next.js application doesn't have many limitations, however one major issue it does have is that it is unable to build to be deployed to an S3 bucket. This is due to the implementation of localStorage, a client side technology that is being used in server side rendering.

As for the desktop application, the software is not dynamic enough to work on a larger variety of job applications. It only works on Workday applications, a result of how it identifies that it has reached a job application. It has logic that allows it to login, create an account, and click on apply so that it can access on job application. However, once on the application, it looks for "My Experience", an implementation that was done at the time to help get the process going, and as I testing other websites I would add more identifying keywords. This, however, never became the case, thus allowing it to only work on Workday. Additionally, at times the software may mess up, for example it does not always select 'Arizona' as the state but rather Arkansas. The software is also able to automate questiosn that are found in most applications, i.e. work history, first and last name, etc., however it is limited in the sense that there are a lot of questions that it can't answer, such as whether they've worked for the company, why they want to work for the company, etc.. Another big limitation is the lack of browser support. Initially, the plan was to allow Chrome, Edge, and FireFox be able to run this program, with the user having the option to select the browser from the start. However, it became apparent that this was not something that I could implement easily and instead focused my time and attention to the many other features that had to be developed beforehand. There also is a lack of certain error handling when logging in that revolves around getting the user's data. Specifically, if the user hasn't uploaded each form, then it will have an error and not log the user in until after they run the start file again.

Another issue I ran into was the new user experience. A lot of my testing has been done from the same account with the same information, however when I created a new account and fetched all new information, one of the biggest things that broke was education forms. It would work if I did a break point and did a step through to get it to add the education forms, but otherwise it had issues adding a form and thus would skip over the education. This was not an issue I had previously had and would need additional time to figure out how to resolve.

### Functional and Non-Functional Requirements
There were over 40 user stories between both applications. The following were the primary/largest in-scope:
* Functional
  * Login/Logout (both on Desktop and the Website)
  * Upload your personal information
  * Add and remove education and work forms
  * Create an account through the website
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
### Physical Solution
![image](https://github.com/JacobGordon43/EZApplyDesktop/assets/77366005/2c8a63ea-04ed-49d9-9293-ea98b55f3bc9)
In the physical solution, an S3 bucket holds our web application and is monitored by UptimeRobot, which alerts us if the application goes down. The contents of the S3 bucket is then delivered to the client side via HTTPS, so that it can be viewed on a client's device.
### Logical Solution
![image](https://github.com/JacobGordon43/EZApplyDesktop/assets/77366005/6bd8f793-ed74-4e89-a7ac-35176df71cdb)
The logical solution consists of a Next.js frontend application that uses redux, components, and pages, and is stored in an S3 bucket. It communicates to the AWS Backend Infrastructure, which is made up of the API gatway, Lambda functions, and DynamoDB database. Finally, the Desktop Python Application is developed with a TKinter UI and Selenium as it's automation tool, with Chrome Driver being used to handle the chrome browser.

### Website Sitemap
![image](https://github.com/JacobGordon43/EZApplyDesktop/assets/77366005/27f8a521-39e5-45ca-834a-1f67fa31a9d8)
This sitemap illustrates the users ability to navigate through the web application. 

### Website Wireframe
The following are the wireframes with the components outlined. The input component was removed in development due to issues with handling values in the overall form.
![image](https://github.com/JacobGordon43/EZApplyDesktop/assets/77366005/0dd2ea97-deb5-454f-bb9d-0268ab90b047)
![image](https://github.com/JacobGordon43/EZApplyDesktop/assets/77366005/f658ab69-e87b-499c-a4ec-b424bb98f6ae)
![image](https://github.com/JacobGordon43/EZApplyDesktop/assets/77366005/e00fc8aa-76e5-4877-aec5-99bbc73e9ad9)

### Code Snippets
![image](https://github.com/JacobGordon43/EZApplyDesktop/assets/77366005/8b874e05-7d15-4739-9b1e-0ca449292077)
This rather small function handles the entire logic for completing an application. It first finds the application by repeatedly running a function until it identifies that it found the actual application. Then, a new loop starts that runs the logic of identifying questions and inserting values to the corresponding input.

![image](https://github.com/JacobGordon43/EZApplyDesktop/assets/77366005/f98b64fe-9816-484a-b352-c7ea5bced744)
This snippet handles running the various specific aspects of application process. For example, it identifies whether or not there is a Work Section in the application, which if there is, it will run the logic to handle that accordingly.

![image](https://github.com/JacobGordon43/EZApplyDesktop/assets/77366005/45f2ffb2-329c-4f96-97c7-31791e55228a)
This further shows how the functions displayed above work. Each one is similar, but it uses a find_elements to see if it's on the application. It goes through each element and sees if it is displayed, which is how it identifies that it can access that part of the application. If it is found, it then will run a function that lets it handle education and work history
![image](https://github.com/JacobGordon43/EZApplyDesktop/assets/77366005/bd8043de-2ab5-4f08-837a-b8af0d5118ad)
There is a lot of logic that goes into finding an input for the questions, but ultimately this function is ran and enters in the input, and ensures that it is done correctly by entering. This helps with certain inputs as typing isn't enough to get the answer, such as selecting the source of how you found the job listing.

