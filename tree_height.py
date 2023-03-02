# python3
import sys
import threading
import numpy as np 
 
def compute_height(elementu_skaits, vertibas):

    max_height = 0
    for i in range(elementu_skaits):
      saraksts.append(i)

    for i in range(elementu_skaits):
      height = get_height(i, vertibas, saraksts)

      if height > max_height:
        max_height = height
        
    return max_height

def get_height(i, vertibas, saraksts):
    
    if saraksts[i] != 0:
        return saraksts[i]
    
    if vertibas[i] == -1:
        saraksts[i] = 1
 
    else:
        saraksts[i] = get_height(vertibas[i], vertibas, saraksts) + 1
    return saraksts[i]

def main():
    text = input()
    if text.startswith('I'):
        elementu_skaits = int(input("Ievadi elementu skaitu: "))
        vertibas = np.asarray(list(map(int,input("Ievadiet vērtības: ").split())))

    elif text.startswith('F'):
        nosaukums = input("Ievadi faila nosaukumu: ") 
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
