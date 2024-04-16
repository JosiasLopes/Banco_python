from datetime import datetime,date,timezone
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Table
from reportlab.lib.pagesizes import letter
from abc import ABC,abstractmethod,abstractproperty
import os
import conta as ct





class Cliente:
    _endereco =""
    _contas = []
    _nome =""
    _cpf = 0
    
    def adicionarConta(self,conta):
        self._contas.append(conta)

    def __init__(self,nome,endereco,cpf):
        self._nome = nome
        self._cpf = cpf
        self._endereco = endereco

    @property
    def name(self):
        return self._nome

    @name.setter
    def name(self,val):
        self._nome = val

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self,val):
        self._cpf = val

    @property
    def contas(self):
        return self._contas

    @property
    def limite(self):
        return self._limite

    

    

        
    

menu = f"""
    digite 0 para buscar e selecionar um Usuario
    digite 1 para depositar
    digite 2 para sacar
    digite 3 para extrato
    digite 4 para cadastrar um novo usuario
    digite 5 para cadastrar um nova conta
    digite 6 para listar contas
    digite 7 para fechar o app"""

numero_saques = 0
titulo_extrato = "EXTRATO"
titulo_extrato =titulo_extrato.center(50,"=")
titulo = "Bem vindo ao sistema bancario basico em Python"
titulo = titulo.center(50,"=")
opcao = ""

contas = []
clientes = []
indice_clientes = 0
indice_contas = 0
n_conta_selecionada = 0
cpf_selecionado =0
numero_inicial_conta = 0


#Função para cadastrar usurio
def cadastrarUsuario(nome,cpf,endereco):
    global clientes
    local_user = []
    #caso a lista esta vazia adicionamos o usuario
    if len(clientes)==0:
        clientes.append(Cliente(nome,endereco,cpf))
        print(f"Usuario : {clientes[0].name} cadastrado com sucesso")
    elif len(clientes)>0:
        local_user = UserExists(cpf)
        #se local_user tiver algum usuario fara a comparação com o nome
        if local_user!= None and local_user[0].cpf == cpf:
           print(f"Usuario : {local_user[0].name} Ja existe")
        elif local_user == None:
            print(clientes)
            clientes.append(Cliente(nome,endereco,cpf))
            print(f"Usuario : {clientes[-1].name} cadastrado com sucesso")
        
    else:
        print(f"Usuario : {nome} usuario ha existente")


#função para cadastro de agencia    
def cadastrarConta(agencia):
    
    global clientes
    global numero_inicial_conta
    cpf = int(input("Informe o cpf do usuario"))
    local_user = pegaCliente(cpf)
    numero_inicial_conta += 1
   
    if local_user!= None:
        print(f"Conta {numero_inicial_conta} vinculada ao usuario: {local_user.name}")
        conta_corrente = ct.ContaCorrente()
        conta_corrente._numero = numero_inicial_conta
        conta_corrente._cliente = local_user
        conta_corrente._agencia = agencia
        conta_corrente.limite = 500.0
        #nova_conta(local_user[0],numero_conta,agencia)
        local_user.adicionarConta(conta_corrente)
        contas.append(conta_corrente)

    elif local_user == None:
        print(clientes)
        print("usuario não encontrado")

def selecionarCliente():
    sub_opt = 0
    global clientes
    global contas
    global n_conta_selecionada
    global cpf_selecionado
    cpf = int(input("Informe o cpf do usuario"))
    local_user = pegaCliente(cpf)
    tmp_conta = []
    
    if local_user!= None:
        print(f"Usuario selecionado: {local_user.name}")
        if local_user.contas!= None:
            listarContas()
            cpf_selecionado = cpf
            while True:
                sub_opt = input("""
    Deseja escolher uma conta para operar ou voltar ao menu principal?
    Digite 1 para selecionar uma conta
    Digite 2 para voltar
                                """)
                if sub_opt == "1":
                        print("Escolha sua conta".center(50,"="))
                        numero_conta = int(input("Digite o numero da conta"))
                        tmp_conta = Conta(numero_conta,cpf_selecionado)
                        if tmp_conta.numero == numero_conta and tmp_conta.cliente.cpf==cpf_selecionado:
                            print(f"Conta : {numero_conta} do usuario: {local_user.name} selecionada")
                            n_conta_selecionada = numero_conta
                        else:
                            print(f"Conta : {numero_conta} do usuario: {local_user.name} não encontrada")
                    
                elif sub_opt == "2":
                    print("Voltando")
                    break
                
        else:
            print("O usuario não possui contas cadastradas")

    elif local_user == None:
        print(clientes)
        print("usuario não encontrado")
        

def pegaCliente(cpf):
    global clientes
    tmp_cliente = ""
    for i in range(len(clientes)):
        if clientes[i].cpf == cpf:
            tmp_cliente = clientes[i]
            return tmp_cliente


def Conta(numero,cpf):
    global contas
    tmp_cliente = pegaCliente(cpf)
    for i in range(len(contas)):
        if contas[i].cliente.cpf == tmp_cliente.cpf and contas[i].numero == tmp_cliente.contas[i].numero:
            return contas[i]
    
        

def listarContas():
    print("=".center(50,"="))
    for i in clientes:
        for j in contas:
            print(f"Agencia: --------------------------------------------------",j._agencia)
            print(f"Conta: --------------------------------------------------",j._numero)
            print(f"Usuario: --------------------------------------------------",j._cliente.name)
            print("=".center(50,"="))
        #print("=".center(50,"="))
    print("=".center(50,"="))
            

def ExtratoConta():
    tmp_cliente = UserExists(cpf_selecionado)
    try:
        conta = ChooseAcount(n_conta_selecionada,tmp_cliente[0].cpf)
        if conta !=None:
            conta.extrato.listar_transacao()
        else:
            print("Selecione uma conta para exibir seu extrato")
    except:
         print("Selecione uma conta para exibir seu extrato")
    
    
def Depositar(valor):
    global cpf_selecionado
    global n_conta_selecionada
    tmp_cliente = pegaCliente(cpf_selecionado)
    conta = Conta(n_conta_selecionada,tmp_cliente.cpf)
    if conta != None:
            if valor>0:
                print(f"Conta: {conta.numero}  titular: {conta.cliente.name} saldo atual: {conta.saldo}")
                conta.depositar(valor)
                deposito = ct.historico.Deposito()
                deposito.registrar(valor)
                conta.extrato.adicionar_transacao(deposito)
                
              
                print(f"Operacao de deposito realizada com sucesso seu saldo é: {conta.saldo}")
                print(f"Conta: {conta.numero}  titular: {tmp_cliente.name} saldo: {conta.saldo}")
            else:
                print("Operação não executada o valor não pode ser menor ou iguala zero")
    else:
            print("Não é possivel efetuar um Deposito sem selecionar uma conta")

    
   
    
    


def Sacar(valor):
    tmp_cliente = UserExists(cpf_selecionado)
    try:
        conta = ChooseAcount(n_conta_selecionada,tmp_cliente[0].cpf)
        if conta != None:
            if valor>0:
                    global indice
                    global numero_saques
                    if valor<=conta.limite:
                        if conta.saldo>0 and conta.saldo>=valor:
                            if numero_saques<conta.saques:
                                conta.sacar(valor)
                                saque = ct.historico.Saque()
                                saque.registrar(valor)
                                conta.extrato.adicionar_transacao(saque)
                                numero_saques +=1
                                
                                
                                print(f"Operacao de deposito realizada com sucesso seu saldo é: {conta.saldo}")
                                
                            else:
                                print("Operação não executada limite de saques atingido")
                        else:
                            print("Operação não executada o valor de saque não pode ser maior que o saldo, ou o saldo esta zerado")
                    else:
                        print(f"Operação não executada pois o saque não pode ultrapassar o limite de {conta.limite}")
            else:
                print("O valor a ser sacado não pode ser zero")
        else:
            print("deu merda")
    except:
        print("Não é possivel efetuar um Deposito sem selecionar uma conta")
print(titulo)

while True:
    opcao = input(menu)
    if opcao == "0":
        print("Buscar Cliente".center(50,"="))
        selecionarCliente()
    elif opcao == "1":
        print("Deposito".center(50,"="))
        Depositar(float(input("Informe o valor a ser depositado")))
    elif opcao == "2":
        print("Saque".center(50,"="))
        Sacar(float(input("Informe um valor a ser sacado")))
        
    elif opcao == "3":
        print(titulo_extrato)
        ExtratoConta()
    elif opcao=="4":
        print("Cadastrar Novo Usuario".center(50,"="))
        nome = input("Informe o nome completo do usuario")
        cpf = int(input("Informe o cpf"))
        endereco = input("Informe p endereço do usuario")
        cadastrarUsuario(nome,cpf,endereco)
    elif opcao=="5":
        print("Cadastrar Nova Conta".center(50,"="))
        agencia = "0001"
        cadastrarConta(agencia)
    elif opcao=="6":
        print("Listar Contas".center(50,"="))
        listarContas()
    elif opcao=="7":
        print("Sair...")
        break
    else:
        print(titulo)
