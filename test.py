import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = []
y = []
SORTED = "#EB455F"
NOTSORTED = "#2B3467"


def duplicate(x):
    return x


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


def selection_sort(xcopy, ycopy, ncopy):
    color = []
    counter = 0
    for i in range(ncopy):
        color.append(NOTSORTED)
    for i in range(ncopy):
        id = i
        for j in range(i+1, ncopy):
            if(ycopy[j] < ycopy[id]):
                id = j
        if(i < n-1):
            plt.clf()
        ycopy[i], ycopy[id] = ycopy[id], ycopy[i]
        color[i] = SORTED
        plt.bar(xcopy, ycopy, color=color)
        plt.pause(n/500)
    plt.title("Selection Sort Completed")
    plt.show()


def insertion_sort(xcopy, ycopy, ncopy):
    color = []
    for i in range(ncopy):
        color.append(NOTSORTED)
    for i in range(1, n):
        curr = ycopy[i]
        j = i-1
        color[j] = SORTED
        while(j >= 0 and ycopy[j] > curr):
            ycopy[j+1] = ycopy[j]
            j -= 1
            plt.bar(xcopy, ycopy, color=color)
            plt.pause(n/1000)
            plt.clf()
        ycopy[j+1] = curr
        color[i] = SORTED
        plt.bar(xcopy, ycopy, color=color)
        plt.pause(n/1000)
        if(i < n-1):
            plt.clf()
    plt.title("Selection Sort Completed")
    plt.show()


print("1. Selection Sort")
print("2. Insertion Sort")
choice = int(input("What sorting operation do you want to see: "))

if(choice == 1):
    selection_sort(np.copy(x), np.copy(y),  n)
if(choice == 2):
    insertion_sort(np.copy(x), np.copy(y),  n)
