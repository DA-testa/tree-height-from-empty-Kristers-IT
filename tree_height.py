# python3
import sys
import threading
import numpy as np
import urllib.request
import io


def compute_height(elementu_skaits, vertibas):
    # Write this function
    max_height = 0
  
    for virsotne in range(elementu_skaits):
      height = 0
      i = virsotne
      while i != -1:
        height = height + 1
        i = vertibas[i] 
      max_height = max(max_height,height)
    
    return max_height


def main():

    text = input()
    if text.startswith('I'):
        elementu_skaits = int(input("Ievadi elementu skaitu: "))
        skaitli = input("Ievadiet vērtības: ")
    elif text.startswith('F'):
        nosaukums = input("Faila nosaukums: ") 
        if 'a' or 'A' in nosaukums:
           return
        with urllib.request.urlopen(nosaukums) as response:
            dati = response.read().decode()
            f = io.StringIO(dati)
            for rinda in f.readlines():
                elementu_skaits = rinda[0]
                skaitli = rinda[1]
   
    vertibas = np.zeros(elementu_skaits, dtype=int)
    skaitli = [int(skaitli) for skaitli in skaitli.split()]
    vertibas = np.array(skaitli)
    max_height = compute_height(elementu_skaits, vertibas)

    print(max_height)
    
sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
