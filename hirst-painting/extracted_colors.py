import colorgram as cg

color_object_list = cg.extract("img.jpg", 1000)
color_tuple_list = []

for color_object in color_object_list:
    color = color_object.rgb
    color_tuple = (color.r, color.g, color.b)
    color_tuple_list.append(color_tuple)
    