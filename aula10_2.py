print("caixa eletrônico")


usuario = input("Digite seu nome: ")

erro = 0
while erro < 3:
        senha = int(input("Digite sua senha: "))
        if senha == 123456:
            print(f"Olá, {usuario}, Seja bem-vindo ao nosso banco!")
            break
        else:
              erro += 1
              if erro < 3:
                    print(f"Senha incorreta, voce tem {3 - erro} tentativas ")
              else:
                print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")
                break
