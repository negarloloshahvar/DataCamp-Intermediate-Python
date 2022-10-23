import pandas as pd
import numpy as np
cars = pd.read_csv('cars.csv', index_col= 0)

cpc = cars['cpc']
many_cars = cpc > 500
car_maniac = cars[many_cars]
# print(car_maniac)
#The output shows that the US, Australia and Japan have a cars_per_cap of over 500.

between = np.logical_and(cpc > 100, cpc < 500)
print(cars[between])