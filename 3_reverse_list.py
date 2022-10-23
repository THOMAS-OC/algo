

#I = 1

#1
# [5,1,2,3,4]

# I = 2

#2
# [5,4,1,2,3]

# I = 3

#3
# [5, 4, 3, 1, 2]

# I = 4

#4
# [5, 4, 3, 2, 1]




"""
On crée une var "iteration" avec pour valeur 1 et une var "index" avec valeur 0

tant que l'iteration i est inférieur au nombre d'éléments dans la liste:
    -On déplace le dernier élément de la liste à l'emplacement de "index"
    -On incrémente "iteration" et "index" de 1.
"""

"""
    Pour récupérer le dernier élément de la liste,
    -on utilise la méthode pop et on enregistre la valeur dans une variable "temp"
    -on utilise la méthode insert et on ajoute la valeur de temp au début de la liste.
    
"""

nb_list = [1, 2, 3, 4, 5, 6, 7, 8] # La liste contient 5 éléments, mais pour l'inverser on ne déplace que 4 éléments, le premier prendra sa                     place au bout de la 4ème itération.

iteration = 1 # Iteration en cour

index = 0 # Positionnement de l'élément déplacé

temp = 0 # valeur de l'élément en bout de liste (le plus à droite.)

while iteration < len(nb_list):
    
    temp = nb_list.pop()
    nb_list.insert(index, temp)
    
    iteration += 1
    index += 1
    
print(nb_list)

"""

Ecriture de la fonction :
La fonction 'inverser' aura pour argument "list_reverse" : une liste.
les variables iteration, index et temp seront locales à la fonction.

"""

def inverser(list_reverse):
    iteration = 1
    index = 0
    temp = 0
    
    while iteration < len(list_reverse):
    
        temp = list_reverse.pop()
        list_reverse.insert(index, temp)
        
        iteration += 1
        index += 1
        
    return list_reverse

abc = inverser(["c", "b", "a"])

print(abc)

milles = inverser([1000, 2000, 3000])

print(milles)