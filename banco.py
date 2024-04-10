from datetime import datetime,date,timezone
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Table
from reportlab.lib.pagesizes import letter
import os

dados = []
dia = ""
mes = ""
ano = ""
hora = ""
minuto = ""
segundo = ""
data =""
menu = f"""
    digite 1 para depositar
    digite 2 para sacar
    digite 3 para extrato
    digite 4 para exportar extrato
    digite 5 para cadastrar um novo usuario
    digite 6 para cadastrar um nova conta
    digite 7 para listar contas
    digite 8 para fechar o app"""
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
indice =0

past = os.path.dirname(__file__)
pdf = SimpleDocTemplate(
    past+"/extrato_tabela2.pdf",pagesize=letter)
table = [] 
elems = []

usuarios = []
contas = []

#Função para cadastrar usurio
def cadastrarUsuario(nome,cpf,endereco):
    global usuarios
    local_user = []
    #caso a lista esta vazia adicionamos o usuario
    if len(usuarios)==0:
        usuarios.append({"nome":nome,"cpf":cpf,"endereco":endereco})
        print(f"Usuario : {nome} cadastrado com sucesso")
    elif len(usuarios)>0:
        local_user = UserExists(cpf)
        #se local_user tiver algum usuario fara a comparação com o nome
        if local_user!= None and local_user[1] == cpf:
           print(f"Usuario : {nome} Ja existe")
        elif local_user == None or local_user != nome:
            print(usuarios)
            usuarios.append({"nome":nome,"cpf":cpf,"endereco":endereco})
            print(f"Usuario : {nome} cadastrado com sucesso")
        
    else:
        print(f"Usuario : {nome} usuario ha existente")


#função para cadastro de agencia    
def cadastrarConta(agencia):
    global usuarios
    cpf = int(input("Informe o cpf do usuario"))
    local_user = []
    local_user = UserExists(cpf)
    conta = 1
    conta = conta+len(contas)
   
    if local_user!= None:
        print(f"Conta {conta} vinculada ao usuario: {local_user[0]}")
        contas.append({"agencia":agencia,"numero":conta,"usuario":local_user[0]})
    elif local_user == None:
        print(usuarios)
        print("usuario não encontrado")
        
def UserExists(cpf):
    global usuarios
    tmp =[]
    user = []
    for indice in range(len(usuarios)): 
        tmp = usuarios[indice]
        if cpf == tmp.get("cpf"):
            user.append(tmp.get("nome"))
            user.append(tmp.get("cpf"))
           # user[0] = tmp.get("nome")
            return user
    else:
        return None
        

def listarContas():
    print("=".center(50,"="))
    for i in contas:
        for j,k in i.items():
            print(f"""{j}-----------------------------------------""",k)
        print("=".center(50,"="))
    print("=".center(50,"="))
            
            
    
def Depositar(valor):
    if valor>0:
            global saldo
            global indice
            saldo += valor
            data = datetime.today()
            ano = data.year
            mes = data.month
            dia = data.year
            hora = data.hour
            minuto = data.minute
            segundo = data.second
            dados.append(list())
            dados[indice].append(f"Valor depositado {valor} na data {dia}/{mes}/{ano} as {hora}:{minuto}:{segundo}")
           # extrato.append(f"Valor depositado {valor} na data {dia}/{mes}/{ano} as {hora}:{minuto}:{segundo}")
            print(f"Operacao de deposito realizada com sucesso seu saldo é: {saldo}")
            indice+=1
    else:
            print("Operação não executada o valor não pode ser menor ou iguala zero")


def Sacar(valor):
    if valor>0:
            global saldo
            global indice
            global numero_saques
            global LIMITE_SAQUES
            data = datetime.today()
            ano = data.year
            mes = data.month
            dia = data.year
            hora = data.hour
            minuto = data.minute
            segundo = data.second
            if valor<=limite:
                if saldo>0 and saldo>=valor:
                    if numero_saques<LIMITE_SAQUES:
                        saldo -= valor
                        numero_saques +=1
                        dados.append(list())
                        dados[indice].append(f"Valor sacado {valor} na data {dia}/{mes}/{ano} as {hora}:{minuto}:{segundo}")
                        print(f"Operação de saque executada com sucesso seu saldo é: {saldo}")
                        indice+=1
                    else:
                        print("Operação não executada limite de saques atingido")
                else:
                    print("Operação não executada o valor de saque não pode ser maior que o saldo, ou o saldo esta zerado")
            else:
                print(f"Operação não executada pois o saque não pode ultrapassar o limite de {limite}")
    else:
        print("O valor a ser sacado não pode ser zero")
print(titulo)

while True:
    opcao = input(menu)
    if opcao == "1":
        print("Deposito".center(50,"="))
        Depositar(float(input("Informe o valor a ser depositado")))
    elif opcao == "2":
        print("Saque".center(50,"="))
        Sacar(float(input("Informe um valor a ser sacado")))
        
    elif opcao == "3":
        print(titulo_extrato)
        for i in dados:
            print(i)
    elif opcao=="4":
        print("Exportar extrato".center(50,"="))
        table = Table(dados)
        elems.append(table)
        pdf.build(elems)
    elif opcao=="5":
        print("Cadastrar Novo Usuario".center(50,"="))
        nome = input("Informe o nome completo do usuario")
        cpf = int(input("Informe o cpf"))
        endereco = input("Informe p endereço do usuario")
        cadastrarUsuario(nome,cpf,endereco)
    elif opcao=="6":
        print("Cadastrar Nova Conta".center(50,"="))
        agencia = "0001"
        cadastrarConta(agencia)
    elif opcao=="7":
        print("Listar Contas".center(50,"="))
        listarContas()
    elif opcao=="8":
        print("Sair...")
    else:
        print(titulo)
