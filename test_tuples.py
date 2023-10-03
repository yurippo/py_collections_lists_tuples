from lists_with_objects_from_our_classes import ContaCorrente

conta_do_gui = ContaCorrente(15)

conta_do_gui.deposita(900)

conta_da_dani = ContaCorrente(16)
conta_da_dani.deposita(900)


# contas = [conta_do_gui , conta_da_dani]

# for conta in contas:
#     print(conta)
    
def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)
        
contas = [conta_do_gui , conta_da_dani]
print(contas[0],contas[1])
deposita_para_todas(contas)
print(contas[0],contas[1])

contas.insert(0,76)
print(contas[0],contas[1],contas[2])

#deposita_para_todas(contas) #it will fail AttributeError: 'int' object has no attribute 'deposita' because contas[0] is an int
# use a list in here that's the case of using a tuple instead
#print(contas[0],contas[1],contas[2])

#Tuples examples
#When we want a imutable representation of values for example user is name and age
#there's nothing more to add or remove this is not a list it's a tuple

#guilherme = ('Guilherme',37,1981) #Tuple that can have 2, 3 values as you prefer
#daniela = ('Daniela',31,1987)
#in tuples the position is also very important  create for example
#paulo = (39,'Paulo',1979) #Very bad ;( I broke my tuple rule in here doing that

#guilherme.append(6754) can't also use append in a Tuple :( it doesn't work
#It's common that When we have more complexity in a group of values including behaviors related to them 
#It's common that this tupple of 3 values becomes a class with 3 attributes and the methods
#and tuples also have their own methods they are not the methods that we're creating

#Could for example represent the lists we had created using tuples instead

conta_do_gui_tuple = (15,1000)
print(conta_do_gui_tuple[1]) #the access works no problem but I can't change anything inside it

#Example

#conta_do_gui_tuple[1] += 100 :( will fail TypeError: 'tuple' object does not support item assignment

#the problem first it's immutable, second I cannot add more values in this tuple, and 3 can't add methods to this tuple

#could not do conta_do_gui_tuple.deposita() :( OO variation
    
#I would have to do 

def deposita(conta):  #functional variation separating data behavior
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    print(codigo,novo_saldo)
    
deposita(conta_do_gui_tuple)

print(conta_do_gui_tuple)

#So if instead of working object oriented I work based in values, functions isolated will have a punch more of functional programming
#instead of object oriented they are 2 different areas

#In brief tuples is when we will mix different data types and the position is very important 

#General rule to remember:
#If the position indicates anything it probable has a fixed size it's probably a tuple
#If the position doesn't have any defined type all same type and the position doesn't matter much
#so it's probably a list that we'll use

#In the real world we work of a mix of everything tuples, lists, objects all mixed up as necessary

#could have for example 

guilherme = ('Guilherme',37,1981) #Tuple that can have 2, 3 values as you prefer
daniela = ('Daniela',31,1987)

usuarios = [guilherme, daniela] #usuarios is a list of tuples I'm mixing these 2 data structures
print(usuarios)

#so Why I've used a list for my users because I've decided that in the future my system will have more users so I can add them
#to this list using append for example

usuarios.append(('Paulo',39,1979))

print(usuarios) #now I can see Paulo the new user
#the usuarios list is mutable so it makes sense I add new users to it

# usuarios[0][0] = 'Guilherme Silveira' can't do that TypeError: 'tuple' object does not support item assignment 
#cannot assign item to tuple

#Another example

conta_corrente_do_gui = ContaCorrente(15)
conta_corrente_do_gui.deposita(500)

conta_corrente_da_dani = ContaCorrente(234876)
conta_corrente_da_dani.deposita(1000)

#if I'm creating a report for example and nobody can add or remove an account from my report that's the case I can
#add my accounts in a tuple like I've done below

contas_tupla_new = (conta_corrente_do_gui, conta_corrente_da_dani)

print(contas_tupla_new)
# #I see the 2 objects inside
# (<lists_with_objects_from_our_classes.ContaCorrente object at 0x000002617B99FE50>, <lists_with_objects_from_our_classes.ContaCorrente object at 0x000002617B99FBE0>)

for conta in contas_tupla_new:
    print(conta)
    
#but in this situation I can change the value of the object we'll see the amount was added
#but in this situation we're using we normaly don't use a tuple it would be more of a list

contas_tupla_new[0].deposita(300)

for conta in contas_tupla_new:
    print(conta)


#Tip tuple will not change size but the objects there inside can change that's what we have to think we we think about tuple