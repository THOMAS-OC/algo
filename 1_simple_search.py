#Algorithme qui devine un nombre entre 1 et 100

# l'algo simple search

import random

search = random.randint(0,100)

array = list(range(0,100))

tentative = -1

def simple_search(array, search) :
    global tentative
    for item in array :
        tentative += 1
        if item == search :
            print("trouvé, c'est : ", item)
            break

print(search)
simple_search(array, search)
print("nombre de tentatives : ", tentative)

# La recherche binaire
