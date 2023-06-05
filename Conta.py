class Conta:
    def __init__(self, titular, numero, saldo):
        self._saldo = 0
        self._numero = numero
        self._titular = titular

    def saque(self, valor):
        if(self._saldo >= valor):
            self._saldo -= valor
            print("Saque realizada com sucesso")
        else:
            print("Saldo insuficiente")
    
    def deposita(self,valor):
        self._saldo += valor
        
    def extrato(self):
        print("Cliente: ",self._titular, " Saldo Atual: ",self._saldo)
        
