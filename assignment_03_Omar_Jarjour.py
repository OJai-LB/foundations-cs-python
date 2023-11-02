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
    name = EnterName()


#GeneralUseMethod
def ChooseDataFrame():
    choice = input(f"Choose a Data Frame: {dfs_string}: ")
    if choice in dfs_string:
        return choice
    else:
        print("Data frame not found \n\t Try Again..")
        return ChooseDataFrame()


#GeneralUseMethod
def EnterName():
    digits = '1234567890'
    chars = '~!@#$%^&*()+-={}[]\|/<>'
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
    input_choice = int(input())

#def main():

   # DisplayMenu()

df1= [{"Name": "Omar", "Age": 23, "Score": (100, 100, 100)}, {"Name": "Ahmad", "Age": 101, "Score": (100, 100, 100)}]
df2 = []
df3 = []
df4 = []
dfs = [df1, df2, df3, df4]
dfs_string = ['df1', 'df2', 'df3', 'df4']
#main()


RemoveStudent()


