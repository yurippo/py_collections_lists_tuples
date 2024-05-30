# Estamos desenvolvendo um projeto para o banco digital Bytebank que trabalha com contas salário. Na nossa classe de conta salário, implementamos os seguintes métodos :

class ContaSalario:
  
  def __init__(self,codigo):
    self._codigo = codigo
    self._saldo = 0

  def __eq__(self,outro):
    if(type(outro) != ContaSalario):
      return False
    return self._codigo == outro._codigo and self._saldo == outro._saldo

  def deposita(self, valor):
    self._saldo += valor
  def __str__(self):
    return "[>>> codigo: {} Saldo: {}]".format(self._codigo, self._saldo)
  

#   Nenhum desses métodos retorna o saldo da conta salário e sabemos que, para manter as boas práticas, não podemos acessar diretamente o atributo da classe para obter o saldo que precisamos.

# Qual é a melhor maneira para se obter o saldo?

#Opcao 1

#Importar o attrgetter e passar o valor do saldo por parâmetro key=attrgetter("_saldo").

#Quando importamos o attrgetter, temos que passar a chave do valor que queremos, pois assim não acessamos o atributo diretamente.

#Opacao 2

#fazer uma função def extrai_saldo(conta), que retorna o saldo da conta. def extrai_saldo(conta): return conta._saldo
#Porem Não é uma boa prática, pois pegamos o atributo saldo direto da conta.


#Answer


import operator
class ContaSalario:
    def __init__(self, codigo):
        self.codigo = codigo

    codigo = property(operator.attrgetter("_codigo"))

    @codigo.setter
    def codigo(self, cod):
        print("Chamando setter")
        self._codigo = cod



# Neste caso, o problema é conseguirmos pegar o valor de _saldo diretamente, o que não é uma boa prática. Usando o attrgetter estamos pegando o valor indiretamente, ou seja, usamos uma ponte para chegarmos ao valor que precisamos, seria o mesmo caso de utilizar uma property para retornar o valor de _saldo, onde usamos uma "ponte" para retornar o atributo "privado". Podemos utilizar o attrgetter para devolver uma property, o que seria ideal como demonstrado acima

# aprendemos neste Projeto:

# O que é ordem natural;
# Ordenar e comparar objetos;
# Utilizar o attrgetter
# Usar o __lt__: menor que (less than) para comparações;



