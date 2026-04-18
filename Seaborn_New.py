import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

diamantes = sns.load_dataset("diamonds")

print(diamantes.head())

print(diamantes.describe())

sns.set_theme(style="whitegrid")

g = sns.relplot(data=diamantes,
                x="carat",
                y="price",
                kind="scatter",
                height=6,
                aspect=1.5)

g.fig.suptitle('Relación entre el Precio y el Peso en Quilates de los Diamantes',
                va='baseline',
                ha='center')

g.set_axis_labels('Peso en Quilates', 'Precio');
plt.show()

# Creando la visualización de la distribución del precio
g = sns.displot(data=diamantes,
                x="price",
                kind="hist",
                kde=True,
                color="blue",
                height=4,
                aspect=2)
g.figure.suptitle('Distribución del Precio de los Diamantes',
                va='baseline',
                ha='center')
g.set_axis_labels('Precio ($)', 'Frecuencia');
plt.show()

# Creando la visualización de la distribución del peso en quilates
g = sns.displot(data=diamantes,
                x="carat",
                kde=True,
                color="green",
                )
g.set_titles('Distribución del Precio en Quilates')
g.set(xlabel='Carat', ylabel='Frecuencia')
plt.show();

# Creando el gráfico catplot de tipo 'box'
g = sns.catplot(data=diamantes,
                kind="box",
                x="cut",
                y="price",
                height=5,
                aspect=2,
                order=["Fair", "Good", "Very Good", "Premium", "Ideal"])
# Establecido título
g.figure.suptitle('Comparación del Precio de los Diamantes por Calidad del Corte',
                    va='baseline',
                    ha='center')
# Establecido etiquetas de ejes
g.set_axis_labels("Calidad del Corte",
                    "Precio ($)");
plt.show();

# Utilizando joinplot para visualizar  la relación entre 'depth' y 'price' con un gráfico de densidad kernel
g = sns.jointplot(data=diamantes,
                    x="depth",
                    y="price",
                    kind="kde",
                    fill=True,
                    space=0,
                    color="purple")
# Cambiando las etiquetas de los ejes
g.set_axis_labels("Profundidad del Diamante (%)",
                    "Precio ($)")
# Mejorando el título
g.fig.suptitle('Relación entre la Profundidad y el Precio de los Diamantes',
                va='baseline',
                ha='center',
                fontsize=16);
plt.show()