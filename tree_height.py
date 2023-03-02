# python3
import sys
import threading
import numpy as np 
 
def compute_height(elementu_skaits, vertibas):

    # python3
import sys
import threading
import numpy as np 
 
def compute_height(elementu_skaits, vertibas):

    max_height = 0
    saraksts = []

    for j in range(elementu_skaits):
        saraksts.append(j)

    for i in range(elementu_skaits):
      height = get_height(i, vertibas, saraksts)

      if height > max_height:
        max_height = height
        
    return max_height

def get_height(i, vertibas, saraksts):

    if vertibas[i] == -1:
        return saraksts[i]
    
    elif saraksts[i] != 0:
        return saraksts[i]
    
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
 
    print(max_height + 1)
    
sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
