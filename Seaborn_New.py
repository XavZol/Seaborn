import seaborn as sns
import matplotlib.pyplot as plt

pinguinos = sns.load_dataset("penguins")
print(pinguinos.head())
sns.displot(data=pinguinos,
            x="body_mass_g",
            kde=True)

sns.displot(data=pinguinos,
            x="body_mass_g",
            kde=True,
            col="island")
plt.show()

sns.displot(data=pinguinos,
            x="flipper_length_mm",
            kind="kde",
            rug=True)
plt.show()

sns.displot(data=pinguinos, 
            x="flipper_length_mm",
            kind="ecdf",) # Dato de distribución acumulativa empirica, nos muestra la proporción de observaciones que caen por debajop de cada valor
plt.show()

