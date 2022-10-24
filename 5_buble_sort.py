i = 0

nb_boucle = 0

array = [3,5,2, -7, -9]

tested = False

while True:
    
    try :
        
        if array[i] > array[i+1]:
        
            temp = array[i]
            
            array[i] = array[i+1]
            
            array[i+1] = temp

            # Si un test a été relevé alors la liste n'était pas triée !
            tested = True
            
        i += 1
        
    # La liste vient d'être parcour car array[i+1] renvoie une erreur.
    except :
        
        # Si aucun test relevé alors la liste est triée !
        if not tested :
            break
        
        # La liste a été parcouru, on reset tested
        else :
            tested = False
            
        # on reset i dans tous les cas pour reparcourir la liste
        i = 0

print(array)