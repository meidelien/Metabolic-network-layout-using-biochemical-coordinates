import pandas as pd
from pyvis.network import Network

data = pd.read_csv("TCA_target_standardized.csv") # Make this file, ok :))))



g = Network(height='900px', width='100%')

featurex = "PC1"
featurey = "PC2"

g.add_nodes(data["BiGG"], 
            title = data["MNXM"],
            x = data[featurex],
            y= data[featurey],
            label = data["Name"],                        
)

g.add_edge(data["BiGG"], data["target"])

g.show(f"{featurex}_{featurey}.html")