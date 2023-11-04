import random

error_messages = [
    "You had one job, choose a number from 1 to 8!!",
    "Invalid choice. Please choose a number between 1 and 8.",
    "Try again. Pick a number from 1 to 8."
]
#Choice1
def GetAverageScore():
    data_frame = ChooseDataFrame()
    data_frame_average = {}
    for i in data_frame:
        data_frame_average[i["Name"]] = sum(i["Score"]) / len(i["Score"])
    return data_frame_average
#Choice 2
def GetYoungestStudent():
    data_frame = ChooseDataFrame()
    data_frame_sorted = sorted(data_frame, key=lambda student: student["Age"])
    return data_frame_sorted[0]["Name"]

#Choice 3
def GetHighestScore(data_frame):
    data_frame_total_score = {}
    highest_valued_score_student = []
    for i in data_frame:
        data_frame_total_score[i["Name"]] = sum(i["Score"])
    highest_valued_key = sorted(list(data_frame_total_score.values()), reverse=True)[0]
    for key in data_frame_total_score:
        if data_frame_total_score[key] == highest_valued_key:
            # list of the students since there might be more than 1 highest same total score
            highest_valued_score_student.append(key)
    return highest_valued_score_student

#Choice 4
def AddStudent():
    data_frame = ChooseDataFrame()
    name = EnterName()
    age = EnterAge()
    scores = EnterScores()
    new_student = {"Name": name, "Age": age, "Score": scores}
    if data_frame == "df1":
        df1.append(new_student)
    elif data_frame == "df2":
        df2.append(new_student)
    elif data_frame == "df3":
        df3.append(new_student)
    elif data_frame == "df4":
        df4.append(new_student)
#Choice 5
def RemoveStudent():
    data_frame = ChooseDataFrame()
    data_frame_content = dfs[dfs_string.index(data_frame)]
    print(f"Content of the chosen data frame:\n{data_frame_content}")
    name = ChooseName(dfs[dfs_string.index(data_frame)])
    index_of_student = None
    for i in data_frame_content:
        if i["Name"] == name:
            index_of_student = data_frame_content.index(i)
            del dfs[dfs_string.index(data_frame)][index_of_student]
            print("The student was deleted successfully!")
        else:
            print("The name entered was not found in the data frame chosen \n\t Re-enter ")

#GeneralUseMethod
def ChooseName(data_frame):
    name = input("Enter the name of the student to delete: ")
    for i in data_frame:
        if i["Name"] == name:
            return name
        else:
            print("The name entered was not found! \n\t Try again..")
            return ChooseName(data_frame)
"""def ChooseNameV2(data_frame1, data_frame2):
    name = input("Enter the name of the student to delete: ")
    for i in data_frame1:
        if i["Name"] == name:
            return name
    for i in data_frame2:
        if i["Name"] == name:
            return name
        else:
            print("The name entered was not found! \n\t Try again..")
            return ChooseNameV2(data_frame1, data_frame2)"""

#GeneralUseMethod
def ChooseDataFrame():
    choice = input(f"Choose a Data Frame: {dfs_string}: ")
    if choice in dfs_string:
        return choice
    else:
        print("Data frame not found \n\t Try Again..")
        return ChooseDataFrame()

def ChooseDataFrameV2():
    choice = input(f"Choose a Data Frame: {dfs_string}: ")
    if choice in dfs_string:
        return dfs[dfs_string.index(choice)]
    else:
        print("Data frame not found \n\t Try Again..")
        return ChooseDataFrame()


#GeneralUseMethod
def EnterName():
    digits = '1234567890'
    chars = '~!@#$%^&*()+-={}[]\ |/<>'
    name = input("Name:")
    for i in name:
        if i in chars:
            print("You could be special \n\t But that doesn't mean you can use special characters.. \n\t\t Try again..")
            return EnterName()
        if i in digits:
            print("What type of equation are you? Quadratic? \n\t Digits are not allowed in names \n\t\t Try again..")
            return EnterName()
    return name
#GeneralUseMethod
def EnterAge():
    while True:
        age = input("Age:")
        if age.isdigit():
            int_age = int(age)
            return int_age
        else:
            print("Age is a matter of numbers. Try again.")
#GeneralUseMethod
def EnterScores():

    while True:
        s1 = input("First Score:")
        if s1.isdigit():
            break
        else:
            print("Score should be a number. Try again.")

    while True:
        s2 = input("Second Score:")
        if s2.isdigit():
            break
        else:
            print("Score should be a number. Try again.")

    while True:
        s3 = input("Third Score:")
        if s3.isdigit():
            break
        else:
            print("Score should be a number. Try again.")

    scores = int(s1), int(s2), int(s3)
    return scores

def GetCommonStudents():
    print("1st DF:")
    data_frame1 = ChooseDataFrameV2()
    print("2nd DF:")
    data_frame2 = ChooseDataFrameV2()
    common_student_list = []
    for i in data_frame1:
        for j in data_frame2:
            if i["Name"] == j["Name"]:
                #to make sure there are no repetitions, we can use dictionary key is name and value is repetition.
                #or cast the list into a set, them, tuple, but the question didnt specify
                common_student_list.append(i["Name"])
    if len(common_student_list) == 0:
        print("No common students in the chosen data frames")
    return common_student_list

def ConsistentImprovement():
    data_frame = ChooseDataFrameV2()
    student_name_list = []
    for i in data_frame:
        temp_score_list = list(i["Score"])
        if temp_score_list[0] < temp_score_list[1] < temp_score_list[2]:
            student_name_list.append(i["Name"])
    student_names = tuple(set(student_name_list))
    if len(student_names) == 0:
        print('Their are no students with consistent improvement in this data frame.')
    elif len(student_names) > 0:
        print(f'Below are the students with consistent improvement: \n{student_names} ')
    return student_names

def InputChoiceVerifier():
    input_choice = input("Enter a choice number: ")
    if input_choice.isdigit() and 1 <= int(input_choice) <= 8:
        return int(input_choice)
    else:
        print(random.choice(error_messages))
        return InputChoiceVerifier()


def DisplayMenu():
    print("""    
    1. Get Average Score                         |
    2. Get Youngest  Student                     |     
    3. Get Highest Score                         |    
    4. Add Student                               |    
    5. Remove Student                            |                
    6. Get Common Students                       |    
    7. Find Students with Consistent Improvement |
    8. Exit                                      |
    _____________________________________________|
    """)
    menu_options = {
        1: GetAverageScore,
        2: GetYoungestStudent,
        3: GetHighestScore,
        4: AddStudent,
        5: RemoveStudent,
        6: GetCommonStudents,
        7: ConsistentImprovement
    }

    while True:
        input_choice = InputChoiceVerifier()
        if input_choice == 8:
            break
        elif input_choice in menu_options:
            menu_options[input_choice]()



def main():
    DisplayMenu()

df1= [{"Name": "Omar", "Age": 23, "Score": (100, 90, 100)}, {"Name": "Ahmadi", "Age": 101, "Score": (100, 100, 100)}, {"Name": "Ahmad", "Age": 35, "Score": (85, 80, 100)}]
df2 = [{"Name": "Omari", "Age": 23, "Score": (100, 90, 100)}, {"Name": "Ahmad", "Age": 101, "Score": (100, 100, 100)}, {"Name": "Ehab", "Age": 35, "Score": (85, 90, 100)}]
df3 = []
df4 = []
dfs = [df1, df2, df3, df4]
dfs_string = ['df1', 'df2', 'df3', 'df4']
#main()


main()