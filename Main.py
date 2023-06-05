from Conta import Conta
from Cliente import Cliente


class Main:
    pass


print("Testando o projeto")


c1 = Cliente("João", "114444-2222")
conta = Conta(c1._nome, 6565, 0)

conta.deposita(1000)
conta.saque(200)
conta.extrato()
