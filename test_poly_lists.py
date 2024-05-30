from polymorphims_lists import Conta , ContaCorrente , ContaPoupanca , ContaSalario
from _operator import attrgetter


#Testing Class Conta
#new_conta = Conta(88)

#print(new_conta)


#Testing Class ContaCorrente

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)


#Testing Class ContaPoupanca

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)


#Testing List of Accounts

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta17 = ContaPoupanca(17)
conta17.deposita(1000)
contas = [conta16,conta17]

for conta in contas:
  conta.passa_o_mes() #duck typing nao importa se eh ContaCorrente ou ContaPoupanca se ele faz quack responde como um pato ok entao posso pedir para fazer duck se responde ao passa o mes ok
  print(conta)



conta1 = ContaSalario(37)
print(conta1)

conta2 = ContaSalario(37)
print(conta2)

#conta1 isnot like conta2 because they would be the same only if they were pointing to the same object not only if their values are the same
#conta1 and conta2 are referencing 2 different objects they are 2 different objects in memory per coincidence they have the same values inside 

# print(conta1 == conta2) False

#This another example that proves conta1 is not like conta2

# contas = [conta1]

# print(conta1 in contas) #True

# print(conta2 in contas) #False

#We used our __eq__ method to define equality and now comparing contas 1 and 2  print(conta1 == conta2)
#it returns True because our equality method does that althought they are 2 different objects in memory

conta1.deposita(10)

#if I deposit 10 in conta1 conta1 and conta2 are no longer the same because the saldo is not the same

#print(conta1 == conta2) #returns False

conta1 = ContaSalario(37)
conta2 = ContaCorrente(37)

print(conta1 == conta2)


print(isinstance(ContaCorrente(34),ContaCorrente)) #To check if it's an instance of a specific type

print(isinstance(ContaCorrente(34),Conta))

conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

lista_contas =[conta_do_guilherme, conta_da_daniela, conta_do_paulo]

for conta in lista_contas:
  print(conta)
  
# sorted(lista_contas)
# throw an error 
# TypeError: '<' not supported between instances of 'ContaSalario' and 'ContaSalario'

#Way to fix the error
#using a function
# def extrai_saldo(conta):
#   return conta._saldo

#using a function to reduce the object in something comparable
# def extrai_saldo(conta):
#  return conta._saldo

# lista_key = sorted(lista_contas,key= extrai_saldo)
# print(lista_key)

# for conta in sorted(lista_contas, key=extrai_saldo):
#   print(conta)
  
# #another way is importing attrgetter from operator to get the parameter

# for conta in sorted(lista_contas,key=attrgetter("_saldo")):
#   print(conta)

# print(conta_do_guilherme > conta_da_daniela)

conta_do_guilhermet = ContaSalario(20)
conta_do_guilhermet.deposita(300)

conta_da_danielat = ContaSalario(15)
conta_da_danielat.deposita(200)

print(conta_do_guilhermet)

print(conta_da_danielat)

print(conta_do_guilhermet > conta_da_danielat)
print(conta_do_guilhermet < conta_da_danielat)

for conta in sorted(lista_contas):
  print(conta)


for conta in sorted(lista_contas, reverse=True):
  print(conta)


conta_do_guilhermen = ContaSalario(17)
conta_do_guilhermen.deposita(500)

conta_da_danielan = ContaSalario(3)
conta_da_danielan.deposita(1000)

conta_do_paulon = ContaSalario(133)
conta_do_paulon.deposita(500)

lista_contasn =[conta_do_guilhermen, conta_da_danielan, conta_do_paulon]

for conta in sorted(lista_contasn):
  print(conta)

print(conta_do_guilhermen == conta_da_danielan)