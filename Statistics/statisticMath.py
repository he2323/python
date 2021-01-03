# import random as r
import statistics as s
import math as m
import matplotlib.pyplot as plt

stats = {
    "all": [90, 15, 95, 45, 27, 98, 45, 86, 39, 15, 45, 22, 45, 25, 96, 71, 62, 35, 25, 35, 90, 9, 60, 26, 20, 49, 36, 91, 42, 43, 44, 19, 35, 87, 21, 23, 81, 79, 50, 42],
    "young": [45, 22, 45, 25, 96, 71, 62, 35, 23, 81, 79, 50, 42],
    "middle": [90, 15, 95, 45, 27, 98, 45, 86, 39, 15],
    "afterThirty": [25, 35, 90, 9, 60, 26, 20, 49, 36, 91, 42, 43, 44, 19, 35, 87, 21]
}

means = []
medians = []
modes = []
variances = []
sqrVariances = []
allLists = {
    "mean": means,
    "median": medians,
    "mode": modes,
    "variance": variances,
    "sqrVariance": sqrVariances
}
for i in stats.values():
    medians.append(s.median(i))
    means.append(s.mean(i))
    modes.append(s.mode(i))
    variances.append(s.variance(i))
    sqrVariances.append(m.sqrt(s.variance(i)))

for key, values in allLists.items():
    print(key)
    for value in values:
        print(value)


# x-coordinates of left sides of bars
for key, value in allLists.items():
    left = [i for i in range(1, len(stats.keys())+1)]
    # heights of bars
    height = value

    # labels for bars
    tick_label = [i for i in stats.keys()]

    # plotting a bar chart
    plt.bar(left, height, tick_label=tick_label,
            width=0.5, color=['red', 'green', 'blue', 'purple'])

    # naming the x-axis
    plt.xlabel('groups')
    # naming the y-axis
    plt.ylabel(key)
    # plot title
    plt.title(key + "time to arrive")

    # function to show the plot
    plt.show()
