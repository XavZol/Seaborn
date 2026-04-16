import seaborn as sns
import matplotlib.pyplot as plt

propinas = sns.load_dataset("tips")

sns.catplot(data=propinas,
            kind="strip",
            x="day",
            y="total_bill",
            hue="smoker");
plt.show()

sns.catplot(data=propinas,
            kind="swarm", # evita el solapamiento
            x="day",
            y="total_bill",
            hue="smoker");
plt.show()

sns.catplot(data=propinas,
            kind="box", # diagrama de caja y bigotes
            x="day",
            y="total_bill",
            hue="smoker");
plt.show()

sns.catplot(data=propinas,
            kind="violin", 
            x="day",
            y="total_bill",
            hue="smoker");
plt.show()

sns.catplot(data=propinas,
            kind="point", 
            x="day",
            y="total_bill",
            hue="smoker");
plt.show()

sns.catplot(data=propinas,
            kind="bar", 
            x="day",
            y="total_bill",
            hue="smoker");
plt.show()

