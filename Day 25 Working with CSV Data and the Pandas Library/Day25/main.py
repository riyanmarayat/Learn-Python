# Part 190 Reading CSV Data in Python
# with open("weather_data.csv", mode="r") as data_file:
#     data = data_file.readlines()
#     print(data)



# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         try:
#             temp = int(row[1])
#             temperatures.append(temp)
#         except ValueError:
#             continue
#     print(temperatures)



# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])



# Part 191 DataFrames & Series: Working with Rows & Columns
# import  pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)
# print(data["temp"].max())
#
# #Get Data in Columns
# print(data["condition"])
# print(data.condition)

#Get data in Rows
# print(data[data.day == "Monday"])
# temp_max = data["temp"].max()
# # print(temp_max)
# print(data[data.temp == 24])

# monday = data[data.day == "Monday"]
# monday_temp_in_fahrenheit = monday.temp[0] * 9/5 + 32
# print(monday_temp_in_fahrenheit)

#Create a DataFram from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")



#Part 192 The Great Squirrel Census Data Analysis (with Pandas!)
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count],
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")