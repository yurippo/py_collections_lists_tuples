#Inheritance and Polymorphims
from functools import total_ordering
from abc import ABCMeta, abstractmethod
from operator import __lt__

#using (metaclass=ABCMeta) turns my class into an abstract class
#we use an abstract class when there are still methods to be implemented like in this example passa_o_mes 
#if the class is tried to be instanced without the method implementation it will throw an error :(
    
class Conta(metaclass=ABCMeta):
    
    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0
            
        
    def deposita(self,valor):
        self._saldo += valor
    
    #in the last versions of python we can create the passa_o_mes method to be implemented with a deorator it's an abstract method 
    #a method to be implemented who inherintace the class will have to implement the method
    
    @abstractmethod    
    def passa_o_mes(self):
        pass
    
    
    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)
    
   
class ContaCorrente(Conta):
    
    def passa_o_mes(self):
        self._saldo -= 2
        
class ContaPoupanca(Conta):
    
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3
        
        
class ContaInvestimento(Conta):
    pass

#We're using functools here total ordering
#Podemos fazer uma anotação e fazer a importação da biblioteca total_ordering
#Com isto não precisamos implementar todos os métodos de comparação
#mas para isso ser possivel temos que ter os métodos eq e o lt implementados
@total_ordering    
class ContaSalario:
    
    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0
        
    def deposita(self,valor):
        self._saldo += valor
    
    #In Python we use the __eq__ method to define equality (verify equality) outro is the other object I'm comparing to
    #and I can implement the method as I prefer
        
    def __eq__(self,outro):
      if type (outro) != ContaSalario:
          return False
              
      return self._codigo == outro._codigo and self._saldo == outro._saldo
  

    def __lt__(self, outro):
      if self._saldo != outro._saldo:
       return self._saldo < outro._saldo
      
      return self._codigo < outro._codigo


    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)
    
    
class ContaMultiploSalario(ContaSalario):
    pass
        
        