#Python Documentation
#Data Structures
#https://docs.python.org/3/tutorial/datastructures.html


idades = [15,87,32,65,56,32,49,37]

sorted_idades = sorted(idades)
print(sorted_idades)


reversed_idades = list(reversed(idades))
print(reversed_idades)



sorted_idades_reversed = sorted(idades,reverse=True)
print(sorted_idades_reversed)


idades.sort() #to sort the same list
print(idades)