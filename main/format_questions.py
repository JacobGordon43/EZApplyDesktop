import actions
import json
def format_questions():
    questions = actions.handle_file('./json/unformatted_questions.json')
    json_arr = {}

    for question, value in questions.items():
        json_entry = {
            "values": value
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
            json_entry["keywords"] = ["City", "city"]
            json_entry["select"] = False 
            json_entry["textarea"] = False 
            json_entry["checkbox"] = False
        elif question == "phoneNumber":
            json_entry["keywords"] = ["Phone Number", "Phone number", "Mobile Number", "Mobile number", "mobile number"]
            json_entry["select"] = False 
            json_entry["textarea"] = False 
            json_entry["checkbox"] = False 
        json_arr[question] = json_entry

        questions = actions.handle_file('./json/unformatted_disclosure.json')

        for question, value in questions.items():
            json_entry = {
                "values": value
            }
            if question == "ethnicity":
                json_entry["keywords"] = ["ethnicity"]
                json_entry["select"] = False 
                json_entry["textarea"] = False 
                json_entry["checkbox"] = False 
            elif question == "sex":
                json_entry["keywords"] = ["sex", "gender"]
                json_entry["select"] = False 
                json_entry["textarea"] = False 
                json_entry["checkbox"] = False 
            elif question == "veteran":
                json_entry["keywords"] = ["veteran"]
                json_entry["select"] = True 
                json_entry["textarea"] = False 
                json_entry["checkbox"] = False 
            elif question == "disability":
                json_entry["keywords"] = ["disability"]
                json_entry["select"] = False 
                json_entry["textarea"] = False 
                json_entry["checkbox"] = True 
            json_arr[question] = json_entry

    with open("./json/tempfile.json", "w") as file: json.dump(json_arr, file, indent=4)
    print(json_arr)

def format_education():
    schools = actions.handle_file('./json/unformatted_education.json')
    count = 0
    json_arr = {}
    for school in schools:
        count += 1
        str_count = str(count)
        school_key = 'School' + str_count
        json_arr[school_key] = {
        } 
        for question, value in school.items():
            
            print(question)
            json_entry = {
                "values": value
            }
            if question == "endDate":
                json_entry["keywords"] = ["From", "End date",  "end date", "End Date"]
                json_entry["select"] = False 
                json_entry["textarea"] = False 
                json_entry["checkbox"] = False
            elif question == "degree":
                json_entry["keywords"] = ["Degree", "degree"]
                json_entry["select"] = False 
                json_entry["textarea"] = False 
                json_entry["checkbox"] = False
            elif question == "startDate":
                json_entry["keywords"] = ["Start Date", "Start date", "To", "to", "start date"]
                json_entry["select"] = False 
                json_entry["textarea"] = False 
                json_entry["checkbox"] = False
            elif question == "schoolName":
                json_entry["keywords"] = ["School", "University"]
                json_entry["select"] = False 
                json_entry["textarea"] = False 
                json_entry["checkbox"] = False
            elif question == "field":
                json_entry["keywords"] = ["Field of Study", "Field", "Study"]
                json_entry["select"] = False 
                json_entry["textarea"] = False 
                json_entry["checkbox"] = False
            elif question == "GPA":
                json_entry["keywords"] = ["GPA"]
                json_entry["select"] = False 
                json_entry["textarea"] = False 
                json_entry["checkbox"] = False
            else:
                continue
            json_arr[school_key][question] = json_entry

        

    with open("./json/education_tempfile.json", "w") as file: json.dump(json_arr, file, indent=4)
    print(json_arr)
# format_education()
format_questions()