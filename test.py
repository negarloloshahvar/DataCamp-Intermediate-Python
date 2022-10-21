import pandas as pd
from matplotlib import pyplot as plt

life_exp = pd.read_csv('life_exp.csv')
gdp_cap = pd.read_csv('gdp_cap.csv')

plt.scatter(life_exp, gdp_cap)
plt.show()
