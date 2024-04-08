import actions
import json
def format_questions():
    questions = actions.handle_file('./json/unformatted_questions.json')
    json_arr = {}

    for question, value in questions.items():
        json_entry = {
            "values": [value]
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
        elif question == "phoneNumberType":
            json_entry["keywords"] = ["Device Type", "Phone Type", "Device type", "Phone type"]
            json_entry["select"] = True 
            json_entry["textarea"] = False 
            json_entry["checkbox"] = False
        else:
            continue 
        json_arr[question] = json_entry

        # json_arr['']
        questions = actions.handle_file('./json/unformatted_disclosure.json')

        for question, value in questions.items():
            json_entry = {
                "values": [value]
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
            else:
                continue
            json_arr[question] = json_entry
        # Pr
        json_arr["aboutUs"] = {
        "keywords": ["Hear", "About"],
        "values": ["LinkedIn"],
        "select" : False,
        "textarea": False,
        "checkbox" : False
        }
        
        json_arr["over18"] = {
                    "keywords": ["Are you age 18 or over", "Are you over 18", "18"],
        "values": "Yes",
        "select" : True,
        "textarea": False,
        "checkbox" : True
        }

        json_arr["relocate"] = {
                    "keywords": ["relocate"],
        "values": ["Yes"],
        "select" : True,
        "textarea": False,
        "checkbox" : True
        }

    json_arr["workLegally"] = {
        "keywords": ["work legally"],
        "values": ["Yes"],
        "select": True,
        "textarea": False,
        "checkbox": False
    }
    json_arr["felony"] = {
        "keywords": ["felony"],
        "values": ["No"],
        "select": True,
        "textarea": False,
        "checkbox": False
    }
    json_arr["compensation"] = {
        "keywords": ["compensation", "salary"],
        "values": ["20/hr"],
        "select": False,
        "textarea": False,
        "checkbox": False
    },

    with open("./json/questions.json", "w") as file: json.dump(json_arr, file, indent=4)
    print(json_arr)

def format_work():
    work_history = actions.handle_file('./json/unformatted_work.json')
    count = 0
    json_arr = {}
    for work in work_history:
        count += 1
        str_count = str(count)
        work_key = 'Work' + str_count
        json_arr[work_key] = {}
        for question, value in work.items():
            json_entry = {
                "values": [value]
            }
            if question == "location":
                json_entry["keywords"] = ["Location", "location"]
                json_entry["select"] = False 
                json_entry["textarea"] = False 
                json_entry["checkbox"] = False
            elif question == "company":
                json_entry["keywords"] = ["Company", "company"]
                json_entry["select"] = False 
                json_entry["textarea"] = False 
                json_entry["checkbox"] = False
            elif question == "from":
                json_entry["keywords"] = ["Start Date", "Start date", "From", "from", "start date"]
                json_entry["select"] = False 
                json_entry["textarea"] = False 
                json_entry["checkbox"] = False
            elif question == "to":
                json_entry["keywords"] = ["To","to", "End date",  "end date", "End Date"]
                json_entry["select"] = False
                json_entry["textarea"] = False
                json_entry["checkbox"] = False
            elif question == "description":
                json_entry["keywords"] = ["Description", "description"]
                json_entry["select"] = False 
                json_entry["textarea"] = False 
                json_entry["checkbox"] = False
            elif question == "workTitle":
                json_entry["keywords"] = ["Title", "title"]
                json_entry["select"] = False 
                json_entry["textarea"] = False 
                json_entry["checkbox"] = False
            else:
                continue
            json_arr[work_key][question] = json_entry
        
    with open("./json/work_tempfile.json", "w") as file: json.dump(json_arr, file, indent=4)

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
                "values": [value]
            }
            if question == "endDate":
                json_entry["keywords"] = ["To","to", "End date",  "end date", "End Date"]
                json_entry["select"] = False 
                json_entry["textarea"] = False 
                json_entry["checkbox"] = False
            elif question == "degree":
                json_entry["keywords"] = ["Degree", "degree"]
                json_entry["select"] = False 
                json_entry["textarea"] = False 
                json_entry["checkbox"] = False
            elif question == "startDate":
                json_entry["keywords"] = ["Start Date", "Start date", "From", "from", "start date"]
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

def format_skills():
    data = actions.handle_file('./json/unformatted_skills.json')
    skills = data['skills']
    skills_arr = []
    for value in skills:
        skills_arr.append(value['skill'])
    skills_data = {}
    skills_data["skills"] = {}
    skills_data["skills"]["keywords"] = ["Skills"]
    skills_data["skills"]["values"] = skills_arr
    with open("./json/skills.json", "w") as file: json.dump(skills_data, file, indent=4)

