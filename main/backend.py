import requests
import aws
import json
import actions
import datetime
def login(username, password):
    url = aws.login_url
    headers = {"Content-Type": "application/json"}
    data = json.dumps({"email": username, "password": password})
    print(data)
    response = requests.post(url=url, headers=headers, data=data)
    print(json.loads(response.text))
    print(response.status_code)
    if response.status_code == 200:
        data = json.loads(data)
        userId = response.json()["userId"]
        print(response.json())
        print(userId)
        with open("./json/login.json", 'w') as file: json.dump(data, file, indent=4)
        with open("./json/create_account.json", 'w') as file: json.dump(data, file, indent=4)
        with open("./json/userId.json", 'w') as file: json.dump({"userId": userId}, file, indent=4)

    return response.status_code
# login("jacobg1@cox.net", "Password43!")
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
    
#     education_data = json.dumps({            
#     "domainName": "EZApply Desktop",
#     "time": datetime.datetime.now(),
#     "body": json.dumps({
#         "tableName": "educationFormData",
#         "expectsOne": False,
#         "userId": userId["userId"]
#     })
# }, default=str)
#     print(education_data)
#     results = requests.post(url=url, data=education_data, headers=headers)
#     questions = json.loads(results.text)
#     questions = questions['result']
#     print(questions)
#     with open("./json/unformatted_education.json", 'w') as file: json.dump(questions, file, indent=4)

#     disclosure_data = json.dumps({            
#     "domainName": "EZApply Desktop",
#     "time": datetime.datetime.now(),
#     "body": json.dumps({
#         "tableName": "nonDisclosureFormData",
#         "expectsOne": False,
#         "userId": userId["userId"]
#     })
# }, default=str)
#     print(disclosure_data)
#     results = requests.post(url=url, data=disclosure_data, headers=headers)
#     questions = json.loads(results.text)
#     questions = questions['result']
#     print(questions[0])
#     with open("./json/unformatted_disclosure.json", 'w') as file: json.dump(questions[0], file, indent=4)

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
    results = requests.post(url=url, data=skills_data, headers=headers)
    questions = json.loads(results.text)
    questions = questions['result']
    skills = questions[0]['skills']
    skills_arr = []
    for value in skills:
        skills_arr.append(value['skill'])
    skills_data = {}
    skills_data["skills"] = {}
    skills_data["skills"]["keywords"] = ["Skills"]
    skills_data["skills"]["values"] = skills_arr
    
    with open("./json/unformatted_skills.json", 'w') as file: json.dump(questions[0], file, indent=4)
get_data()
