#Inicialize a variável produto com o valor 1.
#Crie um laço de repetição que se repita 10 vezes. 
#Solicite ao usuário que digite um número inteiro.
#Leia o número digitado pelo usuário.
#Multiplique o número digitado pela variável produto.
#Atribua o resultado da multiplicação à variável produto.
#Exiba o valor final da variável produto.

produto = 1

for i in range(1, 11):
  fator = int(input("Digite um número inteiro: "))
  produto *= fator

print("O valor final do produto é:", produto)
