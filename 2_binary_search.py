#Algorithme qui devine un nombre entre 1 et 100

# La recherche binaire

import random

secret = random.randint(0,50)

i = 0

print("le nombre secret est : ", secret)


dynamic_list = list(range(0,50))


while i < 5 :
    
    if secret > dynamic_list[max(dynamic_list)//2]:
        
        dynamic_list = list(range(dynamic_list[max(dynamic_list)//2], max(dynamic_list)))
        print("toto sup")

    else :
        
        mini = dynamic_list[min(dynamic_list)]
        
        maxi = max(dynamic_list)//2

        dynamic_list = list(range(mini, maxi))
        
        print("toto inf")
        
    i += 1
    
    print(dynamic_list)
        
        
print("Le nombre secret est contenu entre : ", min(dynamic_list), " et ", max(dynamic_list))