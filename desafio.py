menu = """
        menu
        [d] - depositar
        [s] - sacar
        [e] - extrato
        [q] - sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito:  R${valor:.2f}"

        else:
            print("Operação falhou, valor invalido.")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > valor
        excedeu_limite = valor > limite
        excedeu_saque = numero_saque >= LIMITE_SAQUE

        if excedeu_saque:
            print("Saldo insuficiente, faça um novo depósito.")
        elif excedeu_limite:
            print("Você só pode sacar R$ 500,00 por vez.")
        elif excedeu_saque:
            print(
                "Você já realizou três saques hoje. O limite de saque são três por dia."
            )
            if valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saque += 1

    elif opcao == "e":
        valor = saldo
        print("_______________EXTRATO_______________")

        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        
        print(f"\nSaldo: R$ {saldo:.2f}")
        
        print("_____________________________________")

    if opcao == "q":
        print("Operação encerrada")
        break
