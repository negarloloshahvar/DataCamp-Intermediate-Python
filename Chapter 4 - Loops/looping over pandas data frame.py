import pandas as np

cars = np.read_csv('cars.csv', index_col= 0)

# for index, row in cars.iterrows():
#     print(str(index) +': ' + str(row['cpc']))

for index, row in cars.iterrows():
    cars.loc[index, 'COUNTRY'] = row['country'].upper()

print(cars)



