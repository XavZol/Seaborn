import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model

df = pd.DataFrame()
df["Area"] = [2600, 3000, 3200, 3600, 4000]
df["Precio"] = [550000, 565000, 610000, 680000, 725000]

plt.scatter(df["Area"],df["Precio"]);
plt.show()

X = df[["Area"]]
print(type(df[["Area"]]))

y = df["Precio"]

modelo = linear_model.LinearRegression()
modelo.fit(X, y)
print(modelo.predict([[3300]]))

# Relación entre las Areas y los precios
plt.plot(df["Area"],modelo.predict(X));
plt.show()

plt.scatter(df["Area"], df["Precio"])
plt.plot(df["Area"],modelo.predict(X));
plt.show()