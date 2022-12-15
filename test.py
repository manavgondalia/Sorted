import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = []
y = []
SORTED = "#EB455F"
NOTSORTED = "#2B3467"
color = []


def take_input():
    global x, y
    vector = list(map(int, input("Enter array input: ").split()))
    y = np.array(vector)
    id = []
    for i in range(len(vector)):
        id.append(i)

    x = np.array(id)


# take_input()
# n = len(y)

n = 20

y = np.random.randint(0, 250, n)
x = np.arange(0, n, 1)

for i in range(n):
    color.append(NOTSORTED)

for i in range(n):
    id = i

    for j in range(i+1, n):
        if(y[j] < y[id]):
            id = j

    color[i] = SORTED
    plt.bar(x, y, color=color)
    plt.pause(0.1)
    if(i < n-1):
        plt.clf()

    y[i], y[id] = y[id], y[i]


plt.show()
