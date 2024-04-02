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
    print(userId["userId"])
    data = json.dumps({            
        "domainName": "EZApply Desktop",
        "time": datetime.datetime.now(),
        "body": json.dumps({
            "tableName": "personalFormData",
            "expectsOne": True,
            "userId": userId["userId"]
        })
    }, default=str)
    
    # Create new lambda function to handle this request
    # data = json.dumps({"userId": userId["userId"]}, default=str)
    print(data)
    # Adds additional key value pairs to send to the API
    url = aws.data_url
    headers = {"Content-Type": "application/json"}
    # TODO create a separate call for each table, add a key value in data for that table
    # TODO create an additional file for determining how each call will handle it's data in formatting to the JSON format for this application
    # TODO create a separate function for each file. Specify which function is called based on the database.
    results = requests.post(url=url, data=data, headers=headers)
    questions = json.loads(results.text)
    questions = questions['result']
    print(questions['result'])
    with open("./json/unformatted_questions.json", 'w') as file: json.dump(questions["result"], file, indent=4)
    
    # print(results.text)
    # print(results.status_code)
get_data()
