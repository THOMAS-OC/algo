"""
Le tri par sélection
Le tri par sélection est un algorithme de tri par comparaison.

C'est un tri en place (qui n'utilise donc pas de mémoire supplémentaire car on modifie directement le tableau à trier).

C'est un tri instable car il peut modifier l'ordre des éléments égaux.
"""

# La variable i est incrémenter pour spécifier le départ de l'itération sur la liste et ignorer l'élément correctement placé

# Pour déplacer un élément on le supprime via son index pour éviter de supprimer un autre chiffre identique placé précédemment. Puis on l'insert à la position spécifié par i

array = [3, 2, 1, 5, 7, 3, 1, 9, -7]

i = 0

print(array)

print("----")

while True :
    
    mini = max(array) + 1
    
    for temp in array[i:]:
        
        if temp < mini :
            mini = temp
            index_delete = array.index(mini, i)
            
    array.pop(index_delete)
    array.insert(i, mini)
        
    i += 1
    
    if i == len(array) - 1 :
        break
    
print(array)
    