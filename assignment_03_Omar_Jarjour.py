def GetAverageScore(data_frame):
    data_frame_average = {}
    for i in data_frame:
        if "Name" in i and "Score" in i:
            data_frame_average[i["Name"]] = sum(i["Score"]) / len(i["Score"])
    return data_frame_average

data_frame= [{"Name": "Omar", "Age": 23, "Score": (89, 90, 99)}, {"Name": "Ahmad", "Age": 101, "Score": (50, 50, 50)}]

print(data_frame)
print(GetAverageScore(data_frame))
