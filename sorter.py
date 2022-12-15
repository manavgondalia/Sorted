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
    plt.title("Insertion Sort Completed")
    plt.show()


def st():
    selection_sort(np.copy(x), np.copy(y),  n)


def it():
    insertion_sort(np.copy(x), np.copy(y),  n)


menu = pygame_menu.Menu('Welcome', 1000, 600,
                        theme=pygame_menu.themes.THEME_BLUE)
menu.add.label(LABEL)
menu.add.button('Selection Sort', st)
menu.add.button('Insertion Sort', it)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)
