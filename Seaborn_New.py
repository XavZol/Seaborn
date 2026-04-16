import seaborn as sns
import matplotlib.pyplot as plt

propinas = sns.load_dataset("tips")
print(propinas)

sns.relplot(data=propinas,
            x="total_bill",
            y="tip", 
            hue="smoker",
            style="smoker",
            size="size")
plt.show()


sns.relplot(data=propinas,
            x="total_bill",
            y="tip", 
            hue="smoker",
            style="smoker",
            size="size",
            col="time",
            legend=None)
plt.show()