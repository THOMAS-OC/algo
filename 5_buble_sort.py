i = 0

nb_boucle = 0

array = [3,5,2]

tested = False

while True:
    
    try :
        
        if array[i] > array[i+1]:
        
            temp = array[i]
            
            array[i] = array[i+1]
            
            array[i+1] = temp
            
            temp = 0
            
            tested = True
            
        i += 1
        
    except :
        
        if not tested :
            break
        
        else :
            tested = False
            
        i = 0

print(array)