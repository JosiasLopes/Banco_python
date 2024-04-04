menu = f"""
    digite 1 para depositar
    digite 2 para sacar
    digite 3 para extrato
    digite 4 para sair"""
saldo = 0
limite = 500
extrato = []
numero_saques = 3
numero_saques = 0
LIMITE_SAQUES = 3
titulo_extrato = "EXTRATO"
titulo_extrato =titulo_extrato.center(50,"=")
titulo = "Bem vindo ao sistema bancario basico em Python"
titulo = titulo.center(50,"=")
opcao = ""
print(titulo)
while True:
    opcao = input(menu)
    if opcao == "1":
        valor = float(input("Informe o valor a ser depositado"))
        if valor>0:
            saldo += valor
            extrato.append(f"Valor depositado {valor}")
            print(f"Operacao de deposito realizada com sucesso seu saldo é: {saldo}")
        else:
            print("Operação não executada o valor não pode ser menor ou iguala zero")
    elif opcao == "2":
        valor = float(input("Informe um valor a ser sacado"))
        if valor>0:
            if valor<=limite:
                if saldo>0 and saldo>=valor:
                    if numero_saques<LIMITE_SAQUES:
                        saldo -= valor
                        numero_saques +=1
                        extrato.append(f"Valor sacado {valor}")
                        print(f"Operação de saque executada com sucesso seu saldo é: {saldo}")
                    else:
                        print("Operação não executada limite de saques atingido")
                else:
                    print("Operação não executada o valor de saque não pode ser maior que o saldo, ou o saldo esta zerado")
            else:
                print(f"Operação não executada pois o saque não pode ultrapassar o limite de {limite}")
        else:
            print("O valor a ser sacado não pode ser zero")
    elif opcao == "3":
        print(titulo_extrato)
        for i in extrato:
            print(i)
    elif opcao=="4":
        print("Saindo...")
        break
    else:
        print(titulo)
