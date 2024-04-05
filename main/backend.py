import requests
import aws
import json
import actions
import datetime
import format_questions as FQ
# Attempts to login using the provided username and password from the frontend.
def login(username, password):
    url = aws.login_url
    headers = {"Content-Type": "application/json"}
    data = json.dumps({"email": username, "password": password})
    print(data)
    # Makes a call to the database
    response = requests.post(url=url, headers=headers, data=data)
    print(json.loads(response.text))
    print(response.status_code)
    # Handles the status code by updating the login info pages and stores the user's ID
    if response.status_code == 200:
        data = json.loads(data)
        userId = response.json()["userId"]
        print(response.json())
        print(userId)
        with open("./json/login.json", 'w') as file: json.dump(data, file, indent=4)
        with open("./json/create_account.json", 'w') as file: json.dump(data, file, indent=4)
        with open("./json/userId.json", 'w') as file: json.dump({"userId": userId}, file, indent=4)
        get_data()

    return response.status_code

# Requests data from each table for a user
def get_data():
    userId = actions.handle_file('./json/userId.json')
    url = aws.data_url
    headers = {"Content-Type": "application/json"}


    print(userId["userId"])
    personal_data = json.dumps({            
        "domainName": "EZApply Desktop",
        "time": datetime.datetime.now(),
        "body": json.dumps({
            "tableName": "personalFormData",
            "expectsOne": True,
            "userId": userId["userId"]
        })
    }, default=str)
    

    print(personal_data)
   
    results = requests.post(url=url, data=personal_data, headers=headers)
    questions = json.loads(results.text)
    questions = questions['result']
    print(questions)
    with open("./json/unformatted_questions.json", 'w') as file: json.dump(questions, file, indent=4)
    # Formats a request for the non disclosure table into JSON
    disclosure_data = json.dumps({            
    "domainName": "EZApply Desktop",
    "time": datetime.datetime.now(),
    "body": json.dumps({
        "tableName": "nonDisclosureFormData",
        "expectsOne": False,
        "userId": userId["userId"]
    })
}, default=str)
    print(disclosure_data)
    # Sends a request to the API
    results = requests.post(url=url, data=disclosure_data, headers=headers)
    questions = json.loads(results.text)
    questions = questions['result']
    print(questions[0])
    # Sends the non disclosure information to a JSON file
    with open("./json/unformatted_disclosure.json", 'w') as file: json.dump(questions[0], file, indent=4)
    # Formats the personal and non disclosure data into a single file
    FQ.format_questions()
    # formats a request in JSON to send to the API
    skills_data =  json.dumps({            
    "domainName": "EZApply Desktop",
    "time": datetime.datetime.now(),
    "body": json.dumps({
        "tableName": "skillsFormData",
        "expectsOne": False,
        "userId": userId["userId"]
    })
}, default=str)
    print(skills_data)
    # Makes a request to the API
    results = requests.post(url=url, data=skills_data, headers=headers)
    questions = json.loads(results.text)
    questions = questions['result']
    # Sends the skills to a file
    with open("./json/unformatted_skills.json", 'w') as file: json.dump(questions[0], file, indent=4)
    # Formats the skills
    FQ.format_skills()
    # Formats a request for education to the API
    education_data = json.dumps({            
    "domainName": "EZApply Desktop",
    "time": datetime.datetime.now(),
    "body": json.dumps({
        "tableName": "educationFormData",
        "expectsOne": False,
        "userId": userId["userId"]
    })
}, default=str)
    print(education_data)
    # Sends the request
    results = requests.post(url=url, data=education_data, headers=headers)
    questions = json.loads(results.text)
    questions = questions['result']
    # Sends the result to a file
    with open("./json/unformatted_education.json", 'w') as file: json.dump(questions, file, indent=4)
    # Formats the education file
    FQ.format_education()
get_data()
