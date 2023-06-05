class Conta:
    def __init__(self, titular, numero, saldo):
        self.saldo = 0
        self.numero = numero
        self.titular = titular

    def saque(self, valor):
        if(self.saldo >= valor):
            self.saldo -= valor
            print("Saque realizada com sucesso")
        else:
            print("Saldo insuficiente")
    
    def deposita(self,valor):
        self.saldo += valor
        
    def extrato(self):
        print("Cliente: ",self.titular, " Saldo Atual: ",self.saldo)
        
