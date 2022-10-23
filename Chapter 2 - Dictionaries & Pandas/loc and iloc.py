import pandas as pd

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
row_index = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

car_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}

cars = pd.DataFrame(car_dict)
cars.index = row_index

print(cars.loc[['IN']])
print(cars.iloc[[3]])
print('*************')
print(cars.loc[['US', 'EG']])
print(cars.iloc[[0,6]])
print('*************')
print(cars.loc[['JPN', 'US'], ['country', 'cars_per_cap']])
print(cars.iloc[[2, 0], [0, 2]])
print('*************')
print(cars)
print('*************')
print(cars.loc[:, 'drives_right'])
print(cars.loc[:, ['drives_right']])
print('*************')
print(cars.iloc[:, 1])
print(cars.iloc[:, [1]])
print('*************')
print(cars.loc[:, ['country', 'cars_per_cap']])
print(cars.iloc[:, [0, 2]])