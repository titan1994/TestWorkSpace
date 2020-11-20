from RandomChoice import RandomWalk

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    import os
    os.system('pip install matplotlib')

# squares = [1, 4, 9, 16, 25]
# plt.plot(squares)
# plt.show()

rw = RandomWalk(10000)

rw.fill_walk()

plt.figure(dpi=256, figsize=(10, 6))

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=2)

plt.scatter(0, 0, c='green', edgecolors='none', s=30)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=30)

plt.show()
