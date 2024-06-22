
print("""
===========================
           MENU
===========================           
 1- Depositar
 2- Sacar
 3- Extrato
 4- Sair           
==========================="""
)

valorDeposito = 0
totalConta = 0
limiteSaque = 500
LIMITE_DIARIO = 3
contadorDiario = 0
exibirExtrato = ""



while True:
    opcaoMenu = int(input("Digite a opção desejada: "))

    if(opcaoMenu == 1):
        valorDeposito = float(input("Digite o valor para depositar: "))
        if (valorDeposito >0):
            totalConta += valorDeposito
            print("===============================")
            print(f"Valor depositado com sucesso! \n Saldo: R$ {totalConta}")
            print("===============================")
            exibirExtrato += "\n" + "Deposito: R$ " + str (valorDeposito)
            
        else:
            print("====================================")
            print("Valor não é valido. Tente novamente!")
            print("====================================")
    
    elif(opcaoMenu == 2):

        valorSaque = float(input("Digite o valor para saque: "))

        esgotouSaque = valorSaque > limiteSaque
        esgotouLimite = contadorDiario >= LIMITE_DIARIO

        if(valorSaque > totalConta):
            print("========================================")
            print("Não é possivel sacar por falta de saldo!")
            print("========================================")

        elif(valorSaque <=0):
            print("================================")
            print("Valor inválido. Tente novamente!")
            print("================================")

        elif(esgotouSaque):
            print("================================")
            print("Limite de saldo diário excedido!")
            print("================================")

        elif(esgotouLimite):
            print("=======================")
            print("Limite diário excedido!")
            print("=======================")
            
        elif(valorSaque <= totalConta):
            totalConta = totalConta - valorSaque
            print("==============================")
            print(f"Saque realizado com sucesso! \n Saldo: R$ {totalConta}")
            print("==============================")
            exibirExtrato += "\n" + "Saque: R$ " + str (valorSaque)
            contadorDiario += 1


    elif(opcaoMenu == 3):
        if(exibirExtrato == ""):
            print("=======================================")
            print("Você não realizou nenhuma movimentação!")
            print("=======================================")
        else:
            print("======================")
            print("Segue o seu extrato:")
            print(exibirExtrato)
            print(f"Saldo: R$ {totalConta}")
            print("======================")
    else:
        break
