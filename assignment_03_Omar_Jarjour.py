def GetAverageScore(data_frame):
    data_frame_average = {}
    for i in data_frame:
        if "Name" in i and "Score" in i:
            data_frame_average[i["Name"]] = sum(i["Score"]) / len(i["Score"])
    return data_frame_average

def GetYoungestStudent(data_frame):
    data_frame_sorted = sorted(data_frame, key=lambda student: student["Age"])
    return data_frame_sorted[0]["Name"]


def GetHighestScore(data_frame):
    data_frame_total_score = {}
    for i in data_frame:
        if "Name" in i and "Score" in i:
            data_frame_total_score[i["Name"]] = sum(i["Score"])
    highest_valued_score_student = []
    highest_valued_key = sorted(list(data_frame_total_score.values()), reverse=True)[0]
    for key in data_frame_total_score:
        if data_frame_total_score[key] == highest_valued_key:
            highest_valued_score_student.append(key)


    return highest_valued_score_student

data_frame= [{"Name": "Omar", "Age": 23, "Score": (100, 100, 100)}, {"Name": "Ahmad", "Age": 101, "Score": (100, 100, 100)}]
print(GetHighestScore(data_frame))