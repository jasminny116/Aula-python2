soma_dos_precos = 0
medicamento = input("Digite o nome do medicamento:")
preco = float(input("Digite o preço R$: "))

menor_preco= preco
med_barato = medicamento
soma_dos_precos += preco

for x in range(4):
   medicamento = input("Digite o nome do medicamento: ")
   preco       = float(input("Digite o preço R$: "))
   if preco < menor_preco:
      menor_preco = preco
      med_barato = medicamento
   soma_dos_precos += preco
m = soma_dos_precos/5
print(f"O medicamento mais barato é {med_barato} e o seu preço é {menor_preco}")
print(f"A média é dos preços dos medicamentos {m}")
   
