array = [3,1,4,7,2, 10,20,60, 7, 7, 3, 2, 1]
array_sort = array[:]
array_sort.sort()

index_inf = 0

tested = []

while array != array_sort :
    
    
    tested = []

    for index, value in enumerate(array):
        
        
        if index >= 1 :
            
            index_inf = index
            
            while index_inf - 1 > -1 :
                
                index_inf -= 1
                
                if array[index_inf] > value:
                    
                    move = array.pop(index_inf)
                    
                    array.insert(index, move)
                    tested.append(False)

                    
                else :
                    tested.append(True)


        else :
            pass
        
print("-------")

print(array)