# Menu de operações
menu = """

[d] depositar
[s] sacar
[e] extrato
[q] sair

=> """

# O saldo em zero e somente 3 saques diarios de 500 reais por saque
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

# Inicio do programa
while True:

    opcao = input(menu)

    # deposito
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}"

        else:
            print("Operação falhou! O valor informado é inválido.")

    # saque
    elif opcao == "s":
        valor = float(input("Informe valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    # extrato
    elif opcao == "e":
        print("\n============ EXTRATO ============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("======================================")

    # sair
    elif opcao == "q":
        break

    # opção fora da permitidas
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")