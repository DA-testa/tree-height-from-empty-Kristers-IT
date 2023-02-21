# python3

import sys
import threading
import numpy as np
import re


def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    return max_height


def main():
    # implement input form keyboard and from files
    text = input()
    if 'I' in text[:1]:
        elementu_skaits = input("Ievadi elementu skaitu: ")
    elif 'F' in text[:1]:
        if 'a' in text:
            print("Nosaukums satur burtu a")
            exit()
        else:
            text = input("Faila nosaukums: ")
            with open(text, "r") as f:
                text = f.read()
                elementu_skaits = input("Ievadi elementu skaitu: ")
    else:
        print("Nepareizs ievades formāts")
        
    vertibas = []

    for i in range(elementu_skaits):
        skaitli = int(input("Ievadi šos skaitļus: "))
        vertibas.append(skaitli)

    str_vertibas = map(str, vertibas)
    str_vertibas = ' '.join(str_vertibas)

    print(str_vertibas)
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
