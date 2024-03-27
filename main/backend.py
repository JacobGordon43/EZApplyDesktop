import requests
import aws
import json
import actions
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
        with open("./json/login.json", 'w') as file: json.dump(data, file, indent=4)
        with open("./json/create_account.json", 'w') as file: json.dump(data, file, indent=4)
    return response.status_code

def get_data():
    data = actions.handle_file('./json/userId.json')
    # Adds additional key value pairs to send to the API
    url = aws.login_url
    headers = {"Content-Type": "application/json"}
    # TODO create a separate call for each table, add a key value in data for that table
    # TODO create an additional file for determining how each call will handle it's data in formatting to the JSON format for this application
    # TODO create a separate function for each file. Specify which function is called based on the database.
    results = requests.post(url=url, data=data)
