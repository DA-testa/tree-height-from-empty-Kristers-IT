# python3
import sys
import threading
import numpy as np 
 

def compute_height(elementu_skaits, vertibas):
    # Write this function
    
  
    max_height = 0
    for virsotne in range(elementu_skaits):
        height = get_height(virsotne, vertibas)
        max_height = max(max_height, height)
        
    return max_height

def get_height(virsotne, vertibas):
    if virsotne == -1:
        return 0
    else:
        return 1 + get_height(vertibas[virsotne], vertibas)

def main():

    text = input()
    if text.startswith('I'):
        elementu_skaits = int(input("Ievadi elementu skaitu: "))
        vertibas = np.asarray(list(map(int,input("Ievadiet vērtības: ").split())))
    elif text.startswith('F'):
        nosaukums = input() 
        #if 'a' or 'A' in nosaukums:
           #return
        fails = open("./test/" + nosaukums, "r")
        elementu_skaits = int(fails.readline())

        vertibas = np.asarray(list(map(int,fails.readline().split())))
        #skaitli = [int(skaitli) for skaitli in skaitli.split()] 
    
    
    max_height = compute_height(elementu_skaits, vertibas)
 
    print(max_height)
    
sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
