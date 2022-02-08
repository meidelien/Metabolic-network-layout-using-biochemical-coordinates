from pyvis.network import Network
import json
"""
"shape (str (optional)) – The shape defines what the node looks like. There are two types of nodes. One type has the label inside of it and the other type has the label underneath it.
The types with the label inside of it are:
1) ellipse
2) circle
3) database
4) box
5) text

The ones with the label outside of it are:
1) image
2) circularImage
3) diamond
4) dot
5) star
6) triangle
7) triangleDown
8) square
9) icon

size (num (optional)) – The size is used to determine the size of node shapes that do not have the label inside of them. These shapes are: image, 
circularImage, diamond, dot, star, triangle, triangleDown, square and icon."





"""
file = "./stuff/alcuin_letters.json" 


def get_data():
    with open (file) as json_file:
        data = json.load(json_file)
        return (data["alcuin_letters"])


# bgcolor = "#222222"


def map_data(letter_data, ep_color="#03DAC6", ms_color="#da03b3", edge_color="#018786", ep_shape= "ellipse", ms_shape = "box"):
    g = Network(height = "1500px", width = "75%", bgcolor = "black", font_color ="white")
    for letter in letter_data:
        ep = (letter["ep_num"])[0]
        mss = (letter["mss"])
        g.add_node(ep, color = ep_color, shape = ep_shape)
        for ms in mss:
            g.add_node(ms, color = ms_color, shape = ms_shape)
            g.add_edge(ep, ms, color = edge_color)
    g.barnes_hut()
    g.show("letters.html")


epp_data = get_data()


map_data(letter_data = epp_data, ms_shape ="database", ep_shape = "text")
# print(epp_data)