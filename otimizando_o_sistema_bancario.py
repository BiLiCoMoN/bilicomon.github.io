def menu():
    menu = """\n
    ########################################
    ##                                    ##
    ##                                    ##
    ##             Bem vindo              ##
    ##     Selecione a opção desejada     ##
    ##          [1] Sacar                 ##
    ##          [2] Depositar             ##
    ##          [3] Extrato               ##
    ##          [4] Nova Conta            ##
    ##          [5] Novo Usuário          ##
    ##          [6] Listar Contas         ##
    ##          [0] Sair                  ##
    ##                                    ##
    ##                                    ##
    ########################################
    """
    return input(menu)

def depositar(saldo, valor, extrato,):
    if valor > 0:
        saldo += valor
        extrato += (f"Depósito: R$ {valor}\n")
        print(f"Deposito no valor de {valor}\n")
    else:
        print("Valor inválido, tente novamente!")
    return saldo, extrato    

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques < limite_saques:
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
    return saldo, extrato

def exibir_extrato(saldo,/ ,* , extrato):
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

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def novo_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def main():

    AGENCIA = "0001"
    saldo = 0.00
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("Digite o valor que deseja sacar: "))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
            

        elif opcao == "2":
            valor =  float(input("Digite o valor que deseja depositar: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            novo_usuario(usuarios)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Opção inválida, tente novamente!")


main()