import pandas as pd

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
row_index = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

car_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}

cars = pd.DataFrame(car_dict)
cars.index = row_index

print(cars)

