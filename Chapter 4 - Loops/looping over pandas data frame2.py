import pandas as np

brics = np.read_csv('brics.csv')

# Add a column to a DataFrame by calling a function on another column:
# Using the iterrows() method:
for lab, row in brics.iterrows():
    brics.loc[lab, 'name_lenght'] = len(row['country'])

# Using apply():
brics['name_lenght'] = brics['country'].apply(len)

print(brics)