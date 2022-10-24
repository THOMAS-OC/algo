i = 0

nb_boucle = 0

array = [3,5,2,1,9, -5, 4,20]

array_sorted = array[:]

array_sorted.sort()

while array != array_sorted:
    
    try :
        
        if array[i] > array[i+1]:
        
            temp = array[i]
            
            array[i] = array[i+1]
            
            array[i+1] = temp
            
            temp = False
            
        i += 1
        
    except :
        
        i = 0

print(array)