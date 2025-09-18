# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

# data = pd.read_csv("weather_data.csv")
# print(type(data["temp"]))
# data_dict = data.to_dict()

# print(data_dict)
# print(data["temp"])

# temp_list = data["temp"].to_list()
# print(len(temp_list))
# sum_temp = 0
# for temp in temp_list:
#     sum_temp += temp
# print(sum_temp)
# print(sum_temp / len(temp_list))
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["condition"])


# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])  
# 
#  
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp*9/5 + 32
# print(monday_temp)
# print(monday_temp_f)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pd.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv", index=False)  # to remove index column
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }


data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
blck_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
squirrel_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_squirrels_count, blck_squirrels_count, cinnamon_squirrels_count]
}
squirrel_data = pd.DataFrame(squirrel_dict)
squirrel_data.to_csv("squirrel_count.csv", index=False)
print(squirrel_data)