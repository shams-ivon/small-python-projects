import pandas

data = pandas.read_csv("data.csv")
data_list = data["temp"].tolist()

max_temp = data["temp"].max()
average_temp = data["temp"].mean()
max_temp_row = data[data["temp"] == max_temp]
monday_row = data[data["day"] == "Monday"]
monday_row_as_list = monday_row.values[0]
monday_row_temp = int(monday_row["temp"])

print(data_list)
print(max_temp)
print(average_temp)
print(max_temp_row)
print(monday_row)
print(monday_row_as_list)
print(monday_row_temp)

data_dictionary = {
    "People": ["abc", "xyz", "pqr"],
    "Age": [7, 19, 2]
}

data_frame = pandas.DataFrame(data_dictionary)
data_frame.to_csv("created_csv_file.csv")