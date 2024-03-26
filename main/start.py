import json
def check_if_logged_in():
    try:
        with open("./json/login.json") as file:
            data = json.load(file)

            print(data["email"])
            if data["email"] != "" and data["password"] != "":
                import interface
            else:
                import login_ui
    except:
        import login_ui
    
check_if_logged_in()