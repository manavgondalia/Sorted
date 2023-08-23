import numpy as np
import matplotlib.pyplot as plt
import random
import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Sorter")
LABEL = "Welcome to Sorter! \nNavigate using the arrow keys or mouse.\n Choose array elements randomly or by yourself."

img = pygame.image.load('icon.png')
pygame.display.set_icon(img)


x = []
y = []
y_custom = np.array([])
SORTED = "#EB455F"
NOTSORTED = "#2B3467"
SELECTED = "#F7B801"


n = 20
y = np.random.randint(0, 250, n)
x = np.arange(0, n, 1)
use_custom_array = False


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


def partition(xcopy, ycopy, l, r, ncopy, color):
    pivot = ycopy[r]
    color[r] = SELECTED
    i = l-1
    for j in range(l, r):
        if(ycopy[j] < pivot):
            i += 1
            ycopy[i], ycopy[j] = ycopy[j], ycopy[i]

            plt.bar(xcopy, ycopy, color=color)
            plt.pause(n/1000)
            plt.clf()

    ycopy[i+1], ycopy[r] = ycopy[r], ycopy[i+1]
    color[i+1] = SORTED
    plt.bar(xcopy, ycopy, color=color)
    plt.pause(n/1000)
    plt.clf()
    return i+1


def quick_sort(xcopy, ycopy, l, r, ncopy, color):
    if(l <= r):
        pi = partition(xcopy, ycopy, l, r, ncopy, color)

        plt.bar(xcopy, ycopy, color=color)
        plt.pause(n/1000)
        plt.clf()

        quick_sort(xcopy, ycopy, l, pi-1, ncopy, color)
        quick_sort(xcopy, ycopy, pi+1, r, ncopy, color)

        plt.bar(xcopy, ycopy, color=color)
        plt.pause(n/1000)
        plt.clf()


def set_insanity(value, size):
    global n, x, y
    n = size
    y = np.random.randint(0, 250, n)
    x = np.arange(0, n, 1)
    print(f"Will use the random array: {y}")


def generate_random_array():
    global n, x, y
    y = np.random.randint(0, 250, n)
    x = np.arange(0, n, 1)
    print(f"Will use the random array: {y}")


def set_algo(value, algo):
    global selected_algorithm
    selected_algorithm = value


def start_algorithm():
    print("#"*50)
    print(f"Running {selected_algorithm[0][0]} ...")
    selected_algorithm[0][1]()
    print(f"{selected_algorithm[0][0]} completed.")
    print("#"*50)


def set_array(value):
    global n, x, y, y_custom
    y_custom = np.array(value.split(' '))
    n_custom = len(y)
    x_custom = np.arange(0, n, 1)
    if(use_custom_array):
        y = y_custom
        n = len(y)
        x = np.arange(0, n, 1)
        try:
            y = y.astype(int)
            print(f"Will be using the custom array: {y_custom}")
        except:
            print(
                "Please enter valid integers separated by spaces or don't use custom input.")


def toggle_custom_array(value):
    global use_custom_array, y_custom, n, x, y
    use_custom_array = value
    if(use_custom_array):
        print(f"Will be using the custom array: {y_custom}")
        y = y_custom
        n = len(y)
        x = np.arange(0, n, 1)
        try:
            y = y.astype(int)
        except:
            print(
                "Please enter valid integers separated by spaces or don't use custom input.")
    else:
        n = 20
        y = np.random.randint(0, 250, n)
        x = np.arange(0, n, 1)
        print(f"Will use the random array: {y}")


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


def qt():
    color = []
    for i in range(n):
        color.append(NOTSORTED)
    xcopy = np.copy(x)
    ycopy = np.copy(y)
    ncopy = n
    quick_sort(xcopy, ycopy, 0, ncopy-1, ncopy, color)
    plt.title("Quick Sort Completed")
    plt.bar(xcopy, ycopy, color=color)
    plt.show()


algorithms = [("Bubble Sort", bt), ("Selection Sort", st),
              ("Insertion Sort", it), ("Merge Sort", mt), ("Quick Sort", qt)]

selected_algorithm = (("Bubble Sort", bt), 0)


# Menu for the selection of various settings
menu = pygame_menu.Menu('Welcome', 1000, 600,
                        theme=pygame_menu.themes.THEME_DARK)

menu.add.label(LABEL, max_char=-1, font_size=25, font_color=(255, 255, 255))

menu.add.dropselect(
    'Size of array :', [('Small: 20', 20), ('Medium: 50', 50), ('Large: 100', 100)], onchange=set_insanity)

menu.add.button("New random array", generate_random_array)


menu.add.toggle_switch("Use custom array: ", False,
                       onchange=toggle_custom_array)
menu.add.text_input("Enter array elements: ",
                    input_underline='_', onchange=set_array)
select_algorithm = menu.add.dropselect(
    'Algorithm to run:', algorithms, default=0, onchange=set_algo)
menu.add.button('Start', start_algorithm,
                align=pygame_menu.locals.ALIGN_CENTER)
menu.add.button('Quit', pygame_menu.events.EXIT,
                align=pygame_menu.locals.ALIGN_CENTER)

menu.mainloop(surface)
