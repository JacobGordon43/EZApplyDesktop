import actions as AC
import insert
import interface

# def test_browser_error():
#     result = AC.handle_browser("Not a browser option", "path")
#     if result == 15:
#         return True
#     else:
#         return False

# if test_browser_error:
#     print("Browser Error functionality: Successful")
# else:
#     print("Browser Error functionality: Unsuccessful")

# def test_browser_opens():
#     link = "https://www.youtube.com/"
#     driver = AC.handle_browser("Chrome", "path")
#     driver.get(link)
#     return driver.current_url == link

# if test_browser_opens:
#     print("Browser opening functionality: Successful")
# else:
#     print("Browser opening functionality: Unsuccessful")

# # Tests both uploading a resume successfully and limiting uploadable files to text, work, and pdfs
# def test_resume_upload():
# # Does not work
#     interface.uploadResume("C:\\Users\\jacob\\Downloads\\Contract.pdf")

# # Tests if uploading a resume is limited accordingly
#     interface.uploadResume("C:\\Users\\jacob\\Downloads\\ArchitectureDesign.drawio.png")

# test_resume_upload()

# # # This test tests 3 different features/user stories: finding the application, creating an account, and logging in
# # # To test if it creates an account successfully, change the credentials in create_account.json and login.json to a fake email.
def test_find_application():
    driver = AC.handle_browser("Chrome", "path")
    # Change link as needed, preferably keep it within workday to best show that it is able to find an applicaiton
    driver.get("https://earlywarning.wd5.myworkdayjobs.com/earlywarningcareers/job/Intern---DevOps-Software-Engineering--Summer-2024-_REQ2024173?utm_source=ziprecruiter")
    found = False
    while not found:
        found_application = AC.find_application(driver)
        if found_application == 3 or found_application == 5:
            found = found_application
            break    
    return found

if test_find_application():
    print("Application found job application: Successful")
else:
    print("Application found job application: Unsuccessful")

# # This test is tested by not by a return value 
def test_resume_pauses():
    driver = AC.handle_browser("Chrome", "path")
    driver.get("https://earlywarning.wd5.myworkdayjobs.com/earlywarningcareers/job/Intern---DevOps-Software-Engineering--Summer-2024-_REQ2024173?utm_source=ziprecruiter")
    AC.find_application(driver)
    insert.fill_out_application(driver)

test_resume_pauses()