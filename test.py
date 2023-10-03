from lists_with_objects_from_our_classes import ContaCorrente

# #Creating Objeto and Testing ContaCorrente Class
conta_do_yuri = ContaCorrente(15)
print(conta_do_yuri)

# #Testing Deposita Method
conta_do_yuri.deposita(500)
print(conta_do_yuri)

# #Testing creating a new object of ContaCorrente Class
conta_da_dani = ContaCorrente(47685)

# #Testing Deposita Method for conta_da_dani
conta_da_dani.deposita(1000)
print(conta_da_dani)

#Now I will work with list and it has 2 references for these 2 accounts
#if I try to just print contas it will not work just show the 2 objects
#I have to use a for loop described below

contas = [conta_do_yuri, conta_da_dani]
for conta in contas:
 print(conta)
 
 contas = [conta_do_yuri, conta_da_dani, conta_do_yuri]
 
 print(contas[0])
 
 conta_do_yuri.deposita(100)
 
 print(contas[0])
 
 print(contas[2])
 
 contas[2].deposita(300)
 
 print(conta_do_yuri)