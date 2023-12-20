#builtins como enumerated, range e desempacotamento automatico de tuplas

idades = [15,87,32,65,56,32,49,37]

# for idade in idades: can use this but will not give me the position of the object only the object itself :(
#     print(idade)

#to solve this problem we'll use range and len combined

idades_position = range(len(idades))

print(idades_position)

for idade in range(len(idades)):
    print(idade, idades[idade])
    
#  É super comum isso, então já deve existir algo na documentação do Python que permite pegarmos uma sequência de dados e enumere com 0, 1, 2, 3, 4, isto é, dê um número, enumere essa sequência, com o “Python enumerate”. Assim como o enumerate, existem diversas outras funcionalidades. Vamos pesquisar "documentation python enumerate” no google, disponível neste link. Existem, portanto, diversos Built-in Functions, diversas funções que o Python fornece como o enumerate(), e que farão diversos trabalhos em sequências.

range(len(idades)) #lazy...

enumerate(idades) #lazy

list = list(range(len(idades))) #forcei a geracao dos valores

print(list)

for valor in enumerate(idades):
    print(valor)

for indice, idade in enumerate(idades):
    print(indice,"X",idade)
    
usuarios = [
    ("Guilherme",37,1981),
    ("Daniela",31,1987),
    ("Paulo",39,1979)    
]

for usuario in usuarios:
    print(usuario)
    
#another exemple

for nome,idade,nascimento in usuarios: #ja desempacotando 
    print(nome)
    
    

for nome,_,_ in usuarios: #ja desempacotando ignorando o resto
    print(nome)
