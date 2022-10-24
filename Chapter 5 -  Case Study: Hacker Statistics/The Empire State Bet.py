import numpy as np
import matplotlib.pyplot as plt

all_walks = []
for i in range(500):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        if dice <= 2:
            step = max(0, step - 1)
        elif 3 <= dice <= 5:
            step += 1
        else:
            step = step + np.random.randint(1, 7)
        if np.random.rand() <= 0.001:
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

np_aw = np.array(all_walks)
# plt.plot(np_aw)
plt.clf()

np_aw_t = np.transpose(np_aw)
# plt.plot(np_aw_t)

ends = np_aw_t[-1]
# plt.hist(ends)

# print(ends)

number_of_wins = 0
for end in ends:
    if end >= 60:
        number_of_wins += 1

chance_win = number_of_wins / 500

print(chance_win)
# I have a chance of 0.796 to win the bet!