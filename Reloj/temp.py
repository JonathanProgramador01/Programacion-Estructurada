a = [15, 2, 20, 10, 9, 4, 18, 7, 25, 13, 30, 22, 5, 11, 17]


def bubble_sort(a: list):
    for i in range(len(a)):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


def insertion(a: list):
    for i in range(1, len(a), 1):
        j = i
        temp = a[i]
        while a[j - 1] > temp and j > 0:
            a[j] = a[j - 1]
            j -= 1
        a[j] = temp


def seleccion_sort(a:list):

    for i in range(len(a)):
        pequeño_index = i
        for j in range(i,len(a)):
            current = a[j]
            if a[pequeño_index] > current:
                pequeño_index = j

        a[i],a[pequeño_index] = a[pequeño_index],a[i]





def partition(l,h):
    pivot = a[l]
    i = a[l]
    j = a[h]















quicksort()
