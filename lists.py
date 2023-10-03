age1 = 39
age2 = 30
age3 = 27
age4 = 18

print(age1)
print(age2)
print(age3)
print(age4)

#creating list we normally use list with same data type

ages = [39,30,27,18]

print(ages)

print(type(ages))

print(len(ages))

print(ages[0])
print(ages[1])
print(ages[2])
print(ages[3])

ages.append(15)

print(ages)

print(ages[4])


for age in ages:
    print(age)
    
ages.remove(30)

print(ages)

#ages.remove(30)
ages.append(27)
ages.remove(27)
print(ages)

print(28 in ages)

print(15 in ages)

if 15 in ages:
    print('Yes 15 is in! Removing...')
    ages.remove(15)
else:
    print('No 15 is not :(')
    

if 28 in ages:
    print('yes 28 is in! Removing...')
    ages.remove(28)
else:
    print('No 18 is not :(')
       
print(ages)

ages.append(19)

print(ages)

ages.insert(0,20)

print(ages)

ages = [20,39,18]

print(ages)

ages.append([27,19])

print(ages)

for element in ages:
    print('Received the element',element)
    
ages = [20,39,18]
ages.extend([27,19])
print(ages)

#ages in the next year that means ages + 1

for element in ages:
    print(element + 1)
    
#how to create a list for that old style

ages_next_year = []
for element in ages:
    ages_next_year.append(element + 1) 
print(ages_next_year)


#I can also use a shorter sintaxe to do that
#to create a list applying something to all elements
#that's a good way to work 

ages_next_year_shorter = [(element + 1) for element in ages]
print(ages_next_year_shorter) #voila it worked perfect!

#we can also filter our lists 
#so I'm gonna filter my list for elements greater than 21 using if
#this process is called list comprehension

idades = [20,39,18,27,19]
print(idades)
idades_greater_21 = [(idade)for idade in idades if idade > 21]
print(idades_greater_21)

#another example using a function

def proximo_ano(idade):
    return idade + 1

proximo_ano_var = [proximo_ano(idade)for idade in idades if idade > 21]
print(proximo_ano_var)

#problemas de imutabilidade da lista

def faz_processamento_de_visualizacao(lista):
    print(len(lista))
    lista.append(13) #Python doesn't let me append in here

idades=[16,21,29,56,43]
idades.append(13)
print(idades)

faz_processamento_de_visualizacao(idades)


def faz_processamento_de_visualizacao_test(list = []):
    print(len(list))
    print(list)
    list.append(13)
    
faz_processamento_de_visualizacao_test()

faz_processamento_de_visualizacao_test()

faz_processamento_de_visualizacao_test()

faz_processamento_de_visualizacao_test()

#Result that happens because python always refers to the same object
# 0
# []
# 1
# [13]
# 2
# [13, 13]
# 3
# [13, 13, 13]


#so a good practice is to do it this way

def faz_processamento_de_visualizacao_test_two(lista = None):
    if lista == None:
        lista = list()
    print(len(lista))
    print(lista)
    lista.append(13)
    
faz_processamento_de_visualizacao_test_two()

faz_processamento_de_visualizacao_test_two()

faz_processamento_de_visualizacao_test_two()

faz_processamento_de_visualizacao_test_two()

#New behavior and bug fixed 

# 0
# []
# 0
# []
# 0
# []
# 0
# []