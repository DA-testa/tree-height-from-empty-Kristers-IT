# python3
import sys
import threading
import numpy as np 
 
def compute_height(elementu_skaits, vertibas):

    max_height = 0
    augstums = [0] * elementu_skaits
    for virsotne in range(elementu_skaits):
      height = get_height(virsotne, vertibas, augstums)
      if height > max_height:
        max_height = height
        
    return max_height

def get_height(virsotne, vertibas, augstums):

    if augstums[virsotne] != 0:
        return augstums[virsotne]
    if vertibas[virsotne] == -1:
        augstums[virsotne] = 1
    else:
        augstums[virsotne] = get_height(vertibas[virsotne], vertibas, augstums) + 1
    return augstums[virsotne]

def main():

    text = input()
    if text.startswith('I'):
        elementu_skaits = int(input("Ievadi elementu skaitu: "))
        vertibas = np.asarray(list(map(int,input("Ievadiet vērtības: ").split())))
    elif text.startswith('F'):
        nosaukums = input() 
        if 'a' in nosaukums:
           return
        fails = open("./test/" + nosaukums, "r")
        elementu_skaits = int(fails.readline())
        vertibas = np.asarray(list(map(int,fails.readline().split())))
    
    max_height = compute_height(elementu_skaits, vertibas)
 
    print(max_height)
    
sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
