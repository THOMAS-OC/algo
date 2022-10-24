tableau = [3,2,45,6, - 10, 1,7,0,9,4,-4,-7]


# On compare la valeur de  et de temp à chaque itération et si temp est supérieur à maxi alors on assigne la valeur de temp à .

def maxi(array) :
    
    maxi = 0

    for t in array :
        
        # On assigne la valeur de départ à maxi seulement si on est au début du tableau
        if t == tableau[0]:
            maxi = t

        if t > maxi :
            maxi = t

    return maxi
        
    
maximum = maxi(tableau)

print(maximum)