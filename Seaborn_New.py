import seaborn as sns
import matplotlib.pyplot as plt

# Aplicar un temaa por defecto
sns.set_theme()

# Cargando un dataset
propinas = sns.load_dataset("tips")

# Crear una visualización
sns.relplot(
    data=propinas,
    x="total_bill",
    y="tip",
    col="time",
    hue="smoker",
    style="smoker",
    size="size",
)

plt.show()