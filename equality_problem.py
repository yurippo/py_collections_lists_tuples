# No banco onde Guilherme trabalha está acontecendo um problema: está acontecendo a comparação de duas contas com os mesmos atributos. Observe o seguinte código:

# conta_do_gui = ContaCorrente(15)

# conta_da_dani = ContaCorrente(15)

# if(conta_do_gui == conta_da_dani):
#     print(“São iguais”)
# else:
#     print(“São diferentes”)

# Quando fazemos a comparação com o if, está retornando False, quando deveria retornar True.

# O que Guilherme pode fazer para que o retorno seja True?

# Resposta: Implementar o método eq, onde comparamos o que está vindo como parâmetro ao invés do objeto inteiro.
# Com o método eq podemos fazer a comparação que desejamos.

#O que aprendemos?

# Utilizar o __eq__;
# Utilizar boas práticas para comparação ;
# Usar o isinstance para verificar se uma instância de um objeto;