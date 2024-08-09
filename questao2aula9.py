#2. Um professor de Matemática deseja construir um programa para imprimir uma Progressão Aritmética (PA). 
#Para isso, devem ser informados 3 argumentos: a) primeiro termo, b) quantidade de termos e c) razão.

primeiro_termo= int(input("Digite o primeiro termo: "))
quant_termo = int(input("Digite a quantidade de termos: "))
raz = int(input("Digite a razão do termo: "))

ultimo_termo = primeiro_termo +(quant_termo-1)*raz
for termo in range(primeiro_termo,ultimo_termo+1,raz):
    print(termo)
print("FIM")
