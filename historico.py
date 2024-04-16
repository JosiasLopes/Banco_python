from abc import ABC,abstractmethod,abstractproperty
from datetime import datetime,date,timezone

class Transacao(ABC):

    @abstractmethod
    def registrar(self,conta):
        pass
    
class Historico:

    transacoes = []

    def adicionar_transacao(self,transacao: Transacao):
        self.transacoes.append(transacao)

    def listar_transacao():
        for i in transacoes:
            print(i)
        
        
class Deposito(Transacao):

    
    _valor = 0.0
    _deposito = ""           
                
    def registrar(self,valor):
        self._valor = valor
        data = datetime.today()
        ano = data.year
        mes = data.month
        dia = data.year
        hora = data.hour
        minuto = data.minute
        segundo = data.second
        self._deposito = f"Valor depositado {valor} na data {dia}/{mes}/{ano} as {hora}:{minuto}:{segundo}"

class Saque(Transacao):

    _valor = 0.0

    def registrar(self,valor):
        self._valor = valor
        data = datetime.today()
        ano = data.year
        mes = data.month
        dia = data.year
        hora = data.hour
        minuto = data.minute
        segundo = data.second
        self._deposito = f"Valor depositado {valor} na data {dia}/{mes}/{ano} as {hora}:{minuto}:{segundo}"

