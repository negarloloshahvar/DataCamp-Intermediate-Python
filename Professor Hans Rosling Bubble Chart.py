import pandas as pd
from matplotlib import pyplot as plt

life_exp = pd.read_csv('life_exp.csv')
gdp_cap = pd.read_csv('gdp_cap.csv')

print(life_exp.head())
print(gdp_cap.head())

plt.plot(life_exp, gdp_cap)
plt.show()