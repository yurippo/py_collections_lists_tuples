# Gabriel é programador e trabalha em uma escola dando aula de matemática. No fim do semestre, Gabriel passa as notas dos alunos para uma lista feita em Python que o ajuda no controle das notas. Um dia, acidentalmente, Gabriel duplicou as notas e precisava remover as duplicadas.

notas = [2,2,3,5]

#Como essa duplicidade pode ser removida?

# This is the most popular way by which the duplicates are removed from the list is set() method. But the main and notable drawback of this approach is that the ordering of the element is lost in this particular method.  


# initializing list

# print('The original list is:'+ str(notas))

# #problem resolved here ;)
# new_notas = list(set(notas))

# print('The list after removing duplicates is:'+ str(new_notas))

# #Another option would be to use the bultin function remove that will remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
# #list.remove(x)

print('The original list before remove function is:'+ str(notas))

notas.remove(2)
print('The list after removing duplicates with remove is:'+ str(notas))

#Topics we explored in this project

# What is collection;
# Create list;
# Check list type and list size;
# Show on screen the value according to its position in the list;
# Change values ​​that are inside the list;
# Add values ​​to the end of the list;
# Scroll through the list;
# Remove element from list;
# Remove all elements from the list;
# Check if the element is inside the list;
# Insert an element in the position we want;
# Use a list comprehension;
# Make filtering;
# Create a function and leave a default value;
# What are the problems of mutability.