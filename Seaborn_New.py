import seaborn as sns
import matplotlib.pyplot as plt


pinguinos = sns.load_dataset("penguins")

sns.displot(data=pinguinos,
            x="flipper_length_mm",
            hue="species",
            multiple="stack")
plt.show()

sns.histplot(data=pinguinos,
            x="flipper_length_mm",
            hue="species",
            multiple="stack")
plt.show()

sns.displot(data=pinguinos,
            x="flipper_length_mm",
            hue="species",
            multiple="stack",
            col="species");
plt.show()

sns.relplot(data=pinguinos,
            x="flipper_length_mm",
            y="bill_length_mm",
            col="sex")
plt.show()

graf = sns.relplot(data=pinguinos,
            x="flipper_length_mm",
            y="bill_length_mm",
            col="sex")
graf.set_axis_labels("Largo Aletas (mm)")
plt.show()

