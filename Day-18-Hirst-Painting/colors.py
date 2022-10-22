import colorgram

colors = colorgram.extract("cherryblossompainting.jpg", 20)
# first_color = colors[0]
# rgb1 = first_color.rgb


def color_to_rgb():
    rgb_colors = []
    for color in colors:
        r = color.rgb[0]
        g = color.rgb[1]
        b = color.rgb[2]
        rgb_colors.append((r, g, b))


rgb_list = [(0, 0, 0), (61, 86, 147), (190, 138, 192), (241, 207, 222), (38, 45, 57), (148, 101, 173), (106, 108, 178),
            (244, 240, 227), (210, 229, 221), (112, 81, 117), (223, 170, 208), (42, 60, 106), (126, 140, 194),
            (52, 38, 53), (196, 213, 230), (74, 55, 75), (85, 76, 74), (168, 207, 209), (20, 24, 23), (182, 174, 166)]


