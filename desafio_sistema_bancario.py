menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
=> """

saldo = 0
limite = 500
extrato = ""
total_de_saques = 0
LIMITE_SAQUES = 3

while 1:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor a ser depositado: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depositado: R$ {valor:.2f}\n"
        else:
            print("Erro! O valor informado é invalido!")
    
    elif opcao == "2":
        valor = float(input("Informe o valor a ser sacado: "))
        saldo_ultrapassado = saldo < valor
        limite_ultrapassado = limite < valor
        limite_saques_ultrapassado = LIMITE_SAQUES <= total_de_saques

        if saldo_ultrapassado:
            print("Erro! Saldo insuficiente!")
        elif limite_ultrapassado:
            print("Erro! O valor do saque execedeu o limite!")
        elif limite_saques_ultrapassado:
            print("Erro! O limite de saques diarios foi ultrapassado!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Sacado: R$ {valor:.2f}\n"
            total_de_saques+= 1
        else:
            print("Erro! Valor informado é invalido")
    
    elif opcao == "3":
        print("\n"+"EXTRATO".center(25,"#"))
        print("Não houve movimentações na conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("".center(25,"#"))

    elif opcao == "4":
        break
    
    else:
        print("Opção invalida, digite o numero correspondente a uma das operações!")