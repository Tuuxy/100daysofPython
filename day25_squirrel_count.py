import pandas

data = pandas.read_csv("day25_2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color_counts = data["Primary Fur Color"].value_counts()

fur_color_counts.to_csv("day25_squirrel_color_count.csv")
