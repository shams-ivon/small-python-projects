import pandas

data = pandas.read_csv("central_park_squirrel_data.csv")

primary_fur_gray = data[data["Primary Fur Color"] == "Gray"]
primary_fur_cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
primary_fur_black = data[data["Primary Fur Color"] == "Black"]

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

color_data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

color_data_frame = pandas.DataFrame(color_data_dict)
color_data_frame.to_csv("color_data_csv.csv") 