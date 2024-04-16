import historico

class Conta:
    _saldo = 0.0
    _numero = 0
    _agencia = ""
    _cliente = ""
    _historico = historico.Historico()

    @property
    def saldo(self):
        return self._saldo

    def nova_conta(self,cliente,numero,agencia):
        self._cliente = cliente
        self._numero = numero
        self._agencia = agencia
        self._saldo = 0.0
        return Conta

    def sacar(self,valor):
         self._saldo -= valor
         return True

    def depositar(self,valor):
        self._saldo += valor
        return True

    @property
    def extrato(self):
        return self._historico

    @property
    def cliente(self):
        return self._cliente

    @property
    def numero(self):
        return self._numero

    

class ContaCorrente(Conta):
    _limite = 0.0
    _limite_saques= 3


    @property
    def limite(self):
        return self._limite
    
    @limite.setter
    def limite(self,val):
        self._limite = val

    @property
    def saques(self):
        return self._limite_saques

    def decrementaLimite():
        self._limite_saques -= 1
