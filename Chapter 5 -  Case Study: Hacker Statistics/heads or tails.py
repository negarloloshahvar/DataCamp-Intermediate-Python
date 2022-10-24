import numpy as np
np.random.seed(123)

outcome = []

for iter in range(10):
    coin = np.random.randint(0, 2)
    if coin == 0:
        outcome.append('heads')
    else:
        outcome.append('tails')

print(outcome)

