#1. Crie um programa no qual o usuário informe 2 números inteiros: a e b. Para que o programa continue sua execução, 
#verifique se a < b. Se sim, calcule a soma dos números inteiros no intervalo [a, b]. Caso contrário, informe uma mensagem de erro.

a = int(input("Digite uma número inteiro: "))
b = int(input("Digite uma número inteiro: "))

soma = 0
if a < b:
    for termo in range(a,b):
         soma+= termo
    print(soma)
else:
    print("Erro, tente novamente.")
