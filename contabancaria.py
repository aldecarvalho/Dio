print("menu\n\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair\n\n => ***")
saldo = 0
saldof = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3



while True:
    print("menu\n\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair\n\n => ***")
    opcao = input("Digite opcao desejada: ")

    if opcao == "d":
        valor_deposito = int(input("Valor do Deposito: "))
        
        if valor_deposito <= 0:
            print("Valor inválido para depósito! ")
            saldo = saldo + valor_deposito
        else:
            saldo = saldo + valor_deposito
            valor_deposito_f = "{:.2f}".format(valor_deposito)
            extrato = extrato + "Depósito: R$" + str(valor_deposito_f) + "\n"

    elif opcao == "s":    
        if LIMITE_SAQUES == numero_saques:
            print("\nLimite de 3 saques diários excedido!\n\n ")
        else:
            valor_saque = int(input("Confirme valor para saque: "))
            if valor_saque < 0 or valor_saque > 500:  
                print("Valor inválido para saque! ")
            else:
                if saldo < valor_saque:
                    print(f"\nSaldo Indisponível!\n\nSaldo Atual: R${saldo}\n")
                else:    
                    saldo = saldo - valor_saque
                    numero_saques = numero_saques + 1
                    print(f"Saldo Atual: {saldo}")
                    valor_saque_f = "{:.2f}".format(valor_saque)
                    extrato = extrato + "Saque: R$" + str(valor_saque_f) + "\n"

    elif opcao == "e":
        print("\n" + "Extrato".center(36,"#") + "\n\n" + extrato + "\n")
        if extrato == "":
            print("Não foram realizadas movimentações!\n\n")
        else:
            print(f"O saldo atual da conta é: R${saldo:.2f}\n")
    elif opcao == "q":
        break

    else:
        print("\nDigite uma opcao válida!\n")  