#Our own objects

class ContaCorrente:
    
    def __init__(self,codigo):
        self.codigo = codigo
        self.saldo = 0
        
    def deposita(self,valor):
        self.saldo += valor
        
    def __str__(self):
        return '[>>Codigo {} Saldo {}<<]'.format(self.codigo, self.saldo)
    
    #So as learned we have a class ContaCorrente,
    # a constructor def __init__(self,codigo):
        # self.codigo = codigo
        # self.saldo = 0
    # a method 
    # def deposita(self,valor):
    #     self.saldo += valor
    #and a String representation
    # def __str__(self):
    #     return '[>>Codigo {} Saldo {}<<]'.format(self.codigo, self.saldo)
    
    #Now we're gonna test our class
    
    