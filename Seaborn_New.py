import seaborn as sns
import matplotlib.pyplot as plt

pinguinos = sns.load_dataset("penguins")

sns.set_theme(style="dark")

sns.relplot(data=pinguinos,
            x="bill_length_mm",
            y="bill_depth_mm",
            hue="body_mass_g",
            palette="crest",
            marker="x",
            s=100)
plt.show()

g = sns.relplot(data=pinguinos,
            x="bill_length_mm",
            y="bill_depth_mm",
            hue="body_mass_g",
            palette="crest",
            marker="x",
            s=100)
g.set_axis_labels("Largo del Pico (mm)",
                "Grosor del Pico (mm)",
                labelpad=10)
plt.show()

g = sns.relplot(data=pinguinos,
            x="bill_length_mm",
            y="bill_depth_mm",
            hue="body_mass_g",
            palette="crest",
            marker="x",
            s=100)
g.set_axis_labels("Largo del Pico (mm)",
                    "Grosor del Pico (mm)",
                    labelpad=10)
g.legend.set_title("Masa\nCorporal (g)")
g.figure.set_size_inches(6.5, 4.5)
g.ax.margins(.15);
plt.show()
