#Organizando a lista

# Aprendemos a ordenar a lista usando idades.sort(). Porém, podemos não querer alterar a lista original, mas visualizar os valores da lista em ordem crescente.

idades = [12,90,1,8,10,25,32,31,40,50]

#Como podemos fazer isso com Python?

new_idades = sorted(idades)

print(new_idades)

#Utilizaremos o sorted para retornar uma nova lista ordenada: sorted(idades)
# Caso utilizássemos o idades.sort(), a lista original seria alterada, pois esse comando, além de ordenar, atribui o valor à lista original

#Aprendemos nesse projeto
# -Utilizar a função sorted para fazer a ordenação sem mudar o conteúdo na lista original;
# -Usar a função sort para ordenar atribuindo e mudando a lista original;
# -Utilizar a função reversed que inverte os valores de uma lista sem alterar a lista original.