tableau = [3,2,6, - 10, 1,7,0,9,4,-4,-7]


# On compare la valeur de mini et de temp à chaque itération et si temp est inférieur à mini alors on assigne la valeur de temps à mini.

def mini(array) :
    
    mini = 0

    for t in array :
        
        # On assigne la valeur de départ à mini seulement si on est au début du tableau
        if t == tableau[0]:
            mini = t

        if t < mini :
            mini = t

    return mini
        
    
minimum = mini(tableau)

print(minimum)