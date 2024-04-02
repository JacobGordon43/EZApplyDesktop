import actions

questions = actions.handle_file('./json/unformatted_questions.json')
json = []
for question, value in questions.items():
    json_entry = {
        question: {
            "values": value
        }
    }
    if question == "firstName":
        json_entry["keywords"] = ["First Name", "First name",  "first name"]
        json_entry["select"] = False 
        json_entry["textarea"] = False 
        json_entry["checkbox"] = False
    elif question == "lastName":
        json_entry["keywords"] = ["Last Name", "Last name",  "last name"]
        json_entry["select"] = False 
        json_entry["textarea"] = False 
        json_entry["checkbox"] = False
    elif question == "zipcode":
        json_entry["keywords"] = ["Postal Code", "Postal code", "Zipcode", "Zip Code", "zipcode"]
        json_entry["select"] = False 
        json_entry["textarea"] = False 
        json_entry["checkbox"] = False
    elif question == "address":
        json_entry["keywords"] = ["Address Line 1", "Address line 1", "address line 1"]
        json_entry["select"] = False 
        json_entry["textarea"] = False 
        json_entry["checkbox"] = False
    elif question == "state":
        json_entry["keywords"] = ["State", "state"]
        json_entry["select"] = False 
        json_entry["textarea"] = False 
        json_entry["checkbox"] = False
    elif question == "city":
        json_entry["keywords"] = ["State", "state"]
        json_entry["select"] = False 
        json_entry["textarea"] = False 
        json_entry["checkbox"] = False
    elif question == "phoneNumber":
        json_entry["keywords"] = ["Phone Number", "Phone number", "Mobile Number", "Mobile number", "mobile number"]
        json_entry["select"] = False 
        json_entry["textarea"] = False 
        json_entry["checkbox"] = False 
    json.append(json_entry)
# with open("")
print(json)
