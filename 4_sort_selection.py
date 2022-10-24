"""
Le tri par sélection
Le tri par sélection est un algorithme de tri par comparaison.

C'est un tri en place (qui n'utilise donc pas de mémoire supplémentaire car on modifie directement le tableau à trier).

C'est un tri instable car il peut modifier l'ordre des éléments égaux.
"""

tableau = [3,2,6,1,7,0,9,4,-4]
copy = tableau[:]
copy.sort()

depart = 0

while tableau != copy :
    
    mini = max(tableau)

    for t in tableau[depart:] :
            
        if t < mini :
            mini = t
            tableau.remove(t)
        
        
    tableau.insert(depart, mini)
    
    depart += 1
    print(tableau)

    
    