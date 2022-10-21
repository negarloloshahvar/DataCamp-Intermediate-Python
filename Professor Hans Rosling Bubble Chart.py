import pandas as pd
from matplotlib import pyplot as plt

life_exp = pd.read_csv('life_exp.csv')
life_exp1970 = pd.read_csv('life_exp1970.csv')
gdp_cap = pd.read_csv('gdp_cap.csv')

# plt.scatter(life_exp, gdp_cap)
# plt.hist(life_exp, bins= 15)
# plt.show()
# plt.clf()
#
# plt.hist(life_exp1970, bins= 15)
# plt.show()
# plt.clf()

plt.scatter(gdp_cap, life_exp)

plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Developement in 2007')
plt.xticks([1000, 10000, 100000], ['1K', '10K', '100K'])

plt.show()
