import seaborn as sns
import matplotlib.pyplot as plt

pinguinos = sns.load_dataset("penguins")
g = sns.PairGrid(pinguinos,
                    hue="species",
                    corner=True)
g.map_lower(sns.kdeplot,
            hue=None,
            level=5,
            color=".2")
g.map_lower(sns.scatterplot,
            marker="+")
g.map_diag(sns.histplot, 
            element="step",
            linewidth=0,
            kde=True)
g.add_legend(frameon=True)
g.legend.set_bbox_to_anchor((.61, .6))
plt.show()

