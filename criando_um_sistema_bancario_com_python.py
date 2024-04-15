menu = """
########################################
##                                    ##
##                                    ##
##             Bem vindo              ##
##     Selecione a opção desejada     ##
##          [1] Sacar                 ##
##          [2] Depositar             ##
##          [3] Extrato               ##
##          [4] Sair                  ##
##                                    ##
##                                    ##
########################################
"""

saldo = 0.00
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor que deseja sacar: "))
        
        if numero_saques < LIMITE_SAQUES:
            if valor <= limite:
                if saldo >= valor:
                    saldo -= valor
                    extrato += (f"Saque: R$ {valor}\n")
                    numero_saques += 1
                    print(f"Saque no valor de {valor}\n")
        
                else:
                    print("Seu saldo é inferior ao valor solicitado, por favor tente novamente!")
            else:
                print("Valor de saque excede o limite, tente novamente!")
        else:
            print("Limite de saques diários atingido, tente novamente no dia seguinte!")

    elif opcao == "2":
        valor =  float(input("Digite o valor que deseja depositar: "))
        if valor > 0:
            saldo += valor
            extrato += (f"Deposito: R$ {valor}\n")
            print(f"Deposito no valor de {valor}\n")
        else:
            print("Valor inválido, tente novamente!")

    elif opcao == "3":
        titulo_extrato = '''
########################################
##                                    ##
##            SEU EXTRATO             ##
##                                    ##
########################################
        '''
        print(titulo_extrato)
        print(extrato)
        print(f"Seu saldo é de R$ {saldo}")

    elif opcao == "4":
        break

    else:
        print("Opção inválida, tente novamente!")