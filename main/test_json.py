import actions as AC
import time
# def test_json():
#     questions = AC.handle_file("./json/questions.json")
#     print(questions)
#     counter = 0
#     while counter < 5:
#         counter += 1
#         print("\n")
#         time.sleep(1)
#     question_list = list(questions)
#     print(question_list)

# test_json()

# def pop_value():
#     questions = AC.handle_file("./json/questions.json")
#     questions = questions.pop("about_us")
#     print(questions)

# pop_value()

def del_value():
    questions = AC.handle_file("./json/questions.json")
    del questions["about_us"]
    # for key in questions.copy().items():
    #     print(key)
    #     if("about_us") in questions:
    #         del questions["first_name"]
    #         break
    print(questions)

del_value()