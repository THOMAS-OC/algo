"""
Le tri par sélection
Le tri par sélection est un algorithme de tri par comparaison.

C'est un tri en place (qui n'utilise donc pas de mémoire supplémentaire car on modifie directement le tableau à trier).

C'est un tri instable car il peut modifier l'ordre des éléments égaux.
"""

mini = 100

array = [3, 2, 1, 5, 7, 3, 1, 9]

array2 = []

i = 0

print(array)

print("----")

while True :
    
    mini = 100
    
    for temp in array[i:]:
        
        if temp < mini :
            mini = temp
            index_delete = array.index(mini, i)
            
    print("le plus petit est : ", mini, " \n ")
    
    array.pop(index_delete)
    array.insert(i, mini)
        
    i += 1
    
    print(array)
    
    if i == len(array) - 1 :
        break