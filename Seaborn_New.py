import seaborn as sns
import matplotlib.pyplot as plt

pinguinos = sns.load_dataset("penguins")
sns.jointplot(data=pinguinos,
                x="flipper_length_mm",
                y="bill_length_mm",
                hue="species")
plt.show()

sns.pairplot(data=pinguinos,
                hue="species",)
plt.show()