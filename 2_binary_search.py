"""

Recherche dichotomique ou binary search
Pour rechercher un élément dans un tableau trié, l'algorithme optimal est la recherche dichotomique.

Le principe de l'algorithme est de comparer la valeur recherchée avec la valeur située au milieu du tableau :

si les valeurs sont égales, on retourne la position
si la valeur est supérieure à la valeur recherchée nous pouvons éliminer la moitié inférieure du tableau
si la valeur est inférieure à la valeur recherchée nous pouvons éliminer la moitié supérieure du tableau
Ensuite pour la tentative suivante nous prenons la moitié de la partie restante du tableau et ainsi de suite.


"""

"""

[1,2,3,4,5,6,7,8,9]

On cherche 3 avec pour nom "secret"

if mediane(tableau) == secret :
    return mediane(array)
    break
    
elif mediane(tableau) > secret :
    Supprimer la première moitié du tableau avec medianeArray compris
    
elif mediane(tableau) < secret :
    Supprimer la deuxième moitié du tableau avec medianeArray compris.

"""

import random

tableau = list(range(1,10))

secret = random.choice(tableau)


while len(tableau) > 1 :
    
    centerIndex = len(tableau)//2 # index central du tableau
    
    centerValue = tableau[centerIndex] # Valeur de l'index centrale du tableau à comparer
    
    if centerValue == secret :
        print("Le nombre secret est ", centerValue)
        break
    
    # Si la valeur du centre est supérieur à secret, alors on élimine la 2ème partie du tableau
    
    elif centerValue > secret :
        tableau = tableau[:centerIndex]
        
    # Si la valeur du centre est inférieure à secret, alors on élimine la 1ère partie du tableau
        
    elif centerValue < secret :
        tableau = tableau[centerIndex:]