menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair 


=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0 
LIMITES_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor  = float(input("Informe o Valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${saldo:.2f}\n"
        
        else:
            print("O Valor informado é inválido ")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saque = valor > saldo    
        excedeu_limite  = valor > limite
        excedeu_saques = numero_saque >= LIMITES_SAQUES

        if excedeu_saque:
            print("Valor de saque maior que o saldo")

        elif excedeu_saques:
            print("Limites de saques diários excedido")    

        elif excedeu_limite:
            print("Valor de saque diário excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saque +=1
    
        else:
            print("Operação falhou, o valor informado é inválido, tente novamente.")



    elif opcao == "e":
        print("\n================= extrato ==================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("============================================")

    elif opcao == "q":
        break

    else:
        print("Por favor, Digite uma operação válida. ")