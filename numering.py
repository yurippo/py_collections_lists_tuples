#Numering

# Gabriela está revisando um código em Python que contém uma lista de idades, que está percorrendo esta lista e mostrando o índice e a idade:

# idades = [15,87,37,45,56,32,49,37]
# for i in range(len(idades)):
#     print(i,idades[i])

# Este código faz a numeração da idade e a põe um index ao lado de cada idade, mas isto é muito trabalhoso de se fazer.
# Como o código pode ser melhorado, de modo a facilitar a implementação?

#Refactoring

idades = [15,87,37,45,56,32,49,37]

for index,age in enumerate(idades):
    print(index,age)
    
#Utilizando o enumerate para percorrer nossa lista e numerar cada valor
#Quando utilizamos o enumerate, ele faz a enumeração dos valores automaticamente, assim evitaremos código a mais

#Aprendemos nesse projeto
#Builtin Functions in Python
# O que são enumerated
# Como funciona a função range
# Desempacotar tuplas
# Utilizar a função len