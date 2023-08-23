import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Sorter")
LABEL = "Welcome to Sorter! \n Press any button to see the sorting algorithm in action. \n Or navigate using the arrow keys."

img = pygame.image.load('icon.png')
pygame.display.set_icon(img)


x = []
y = []
SORTED = "#EB455F"
NOTSORTED = "#2B3467"
SELECTED = "#F7B801"


n = 20
y = np.random.randint(0, 250, n)
x = np.arange(0, n, 1)


def bubble_sort(xcopy, ycopy, ncopy):
    color = []
    for i in range(ncopy):
        color.append(NOTSORTED)
    for i in range(ncopy):
        for j in range(ncopy-i-1):
            if(ycopy[j] > ycopy[j+1]):

                color[j] = SELECTED
                ycopy[j], ycopy[j+1] = ycopy[j+1], ycopy[j]
                plt.bar(xcopy, ycopy, color=color)
                plt.pause(n/500)
                plt.clf()
                color[j] = NOTSORTED

        color[ncopy-i-1] = SORTED
        plt.bar(xcopy, ycopy, color=color)
        plt.pause(n/500)
        if(i < n-1):
            plt.clf()
    plt.title("Bubble Sort Completed")
    plt.show()


def selection_sort(xcopy, ycopy, ncopy):
    color = []
    for i in range(ncopy):
        color.append(NOTSORTED)
    for i in range(ncopy):
        id = i
        for j in range(i+1, ncopy):
            if(ycopy[j] < ycopy[id]):

                color[j] = SELECTED
                plt.bar(xcopy, ycopy, color=color)
                plt.pause(n/1000)
                plt.clf()
                color[j] = NOTSORTED

                id = j
        ycopy[i], ycopy[id] = ycopy[id], ycopy[i]

        color[i] = SORTED
        plt.bar(xcopy, ycopy, color=color)
        plt.pause(n/1000)

        if(i < n-1):
            plt.clf()

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
            plt.pause(n/1500)
            plt.clf()
        ycopy[j+1] = curr
        color[i] = SORTED
        plt.bar(xcopy, ycopy, color=color)
        plt.pause(n/1500)
        if(i < n-1):
            plt.clf()
    plt.title("Insertion Sort Completed")
    plt.show()


def merge(xcopy, ycopy, l, m, r, ncopy, color):
    n1 = m-l+1
    n2 = r-m
    L = [0]*n1
    R = [0]*n2
    for i in range(n1):
        L[i] = ycopy[l+i]
    for i in range(n2):
        R[i] = ycopy[m+1+i]
    i = 0
    j = 0
    k = l
    while(i < n1 and j < n2):
        if(L[i] <= R[j]):
            color[l + i] = SORTED
            ycopy[k] = L[i]
            i += 1
        else:
            color[m + 1 + j] = SORTED
            ycopy[k] = R[j]
            j += 1
        k += 1
    while(i < n1):
        color[l + i] = SORTED
        ycopy[k] = L[i]
        i += 1
        k += 1
    while(j < n2):
        color[m + 1 + j] = SORTED
        ycopy[k] = R[j]
        j += 1
        k += 1


def merge_sort(xcopy, ycopy, l, r, ncopy, color):
    if l < r:
        m = (l+r)//2
        plt.bar(xcopy, ycopy, color=color)
        plt.pause(n/1000)
        plt.clf()
        merge_sort(xcopy, ycopy, l, m, ncopy, color)
        merge_sort(xcopy, ycopy, m+1, r, ncopy, color)

        plt.bar(xcopy, ycopy, color=color)
        plt.pause(n/1000)
        plt.clf()

        merge(xcopy, ycopy, l, m, r, ncopy, color)

        plt.bar(xcopy, ycopy, color=color)
        plt.pause(n/1000)
        plt.clf()
    else:
        return


def set_insanity(value, size):
    global n, x, y
    n = size
    y = np.random.randint(0, 250, n)
    x = np.arange(0, n, 1)


def bt():
    bubble_sort(np.copy(x), np.copy(y),  n)


def st():
    selection_sort(np.copy(x), np.copy(y),  n)


def it():
    insertion_sort(np.copy(x), np.copy(y),  n)


def mt():
    color = []
    for i in range(n):
        color.append(NOTSORTED)
    xcopy = np.copy(x)
    ycopy = np.copy(y)
    ncopy = n
    merge_sort(xcopy, ycopy, 0, ncopy-1, ncopy, color)
    plt.title("Merge Sort Completed")
    plt.bar(xcopy, ycopy, color=color)
    plt.show()


def set_algo(value, algo):
    global selected_algorithm
    selected_algorithm = value


def start_algorithm():
    selected_algorithm[0][1]()

def set_array(value):
    global n, x, y
    y = np.array(value.split(','))
    n = len(y)
    x = np.arange(0, n, 1)

algorithms = [("Bubble Sort", bt), ("Selection Sort", st),
              ("Insertion Sort", it), ("Merge Sort", mt)]
selected_algorithm = (("Bubble Sort", bt), 0)


# Menu for the selection of various settings
menu = pygame_menu.Menu('Welcome', 1000, 600,
                        theme=pygame_menu.themes.THEME_DARK)

menu.add.label(LABEL)

menu.add.selector(
    'Size of array :', [('Mild: 20', 20), ('Bold: 50', 50), ('Insane: 100', 100)], onchange=set_insanity)

select_algorithm = menu.add.dropselect(
    'Algorithm to run:', algorithms, default=0, onchange=set_algo)

menu.add.button('Start', start_algorithm)

menu.add.text_input("Enter array elements: ", default='1,2,3,4,5,6,7,8,9,10', onchange=set_array)

# menu.add.button('Bubble Sort', bt)
# menu.add.button('Selection Sort', st)
# menu.add.button('Insertion Sort', it)
# menu.add.button('Merge Sort', mt)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)
