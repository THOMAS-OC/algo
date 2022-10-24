"""
Tri par sélection simplifié
----------------------------

1 Trouver le minium et l'enregistrer dans une variable "mini"
2 Ajouter le minium en bout de liste nommé "list_sorted"
3 Supprimer le minimum de la liste raw_list à l'aide de ma méthode remove

"""

array = [1,4,2,8,5,-2, 1, 1, 1, 2, 2]


def selection_sort(raw_list):
    
    copy_list = raw_list[:]
    
    list_sorted = []
    
    
    while len(list_sorted) != len(raw_list) :

        mini = min(copy_list)
        
        list_sorted.append(mini)
        
        copy_list.remove(mini)
        
        
    return list_sorted
        
tri = selection_sort(array)

print(tri)