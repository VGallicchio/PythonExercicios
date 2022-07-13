# Classe principal.
class Contas():
    def __init__(self, saldo, titular):
        self.saldo = float(saldo)
        self.titular = titular

    #Criando funções, para saldo, sacar e depositar.
    def extrato(self):
        print(f"Saldo de {self.saldo} do titular {self.titular}\n")


    def deposita(self, valor):
        valor = float(valor)
        self.saldo += valor
        print(f'Valor {valor} depositado com sucesso')


    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.saldo
        return valor_a_sacar <= valor_disponivel_a_sacar


    def saca(self, valor):
        valor = float(valor)
        if(self.__pode_sacar(valor)):
            self.saldo -= valor
            print(f'Saque de {valor} realizado com sucesso')
        else:
            print(f"Saldo insuficiente!")

    @staticmethod
    def codigos_bancos():
        return {'Itau':'341', 'Bradesco':'237'}

# Classes filho, para discriminar banco.
#As classes contém a função de transferir com seus parametros.
class Itau(Contas):
    def transferencia(self, valor, titular, banco):
        if banco == "341":
            self.saldo -= valor
            titular.saldo += valor
            print("Transação concluída!")
        else:
            total = (valor + (valor * 0.01))
            if total <= self.saldo:
                if self != titular:
                    self.saldo -= total
                    titular.saldo += valor
                    print("Transação concluída!")
                else:
                    print("Impossível transferir para sua própria conta")
            else:
                print('Saldo insuficiente!')


class Bradesco(Contas):
    def transferencia(self, valor, titular, banco):
        if banco == "237":
            self.saldo -= valor
            titular.saldo += valor
            print("Transação concluída!")
        else:
            total = (valor + (valor * 0.005 + 5))
            if total <= self.saldo:
                if self != titular:
                    self.saldo -= total
                    titular.saldo += valor
                    print("Transferencia concluída!")
                else:
                    print("Impossível transferir para sua própria conta")
            else:
                print('Saldo insuficiente!')


# Tester:
print("Teste Transferencias".center(30))
conta1 = Itau(800, "Vitor")
conta2 = Bradesco(600, "Rodrigo")
conta3 = Itau(800, "Lucas")

conta1.transferencia(10, conta3, "341")
conta1.extrato()
conta3.extrato()

conta1.transferencia(10, conta2, "237")
conta1.extrato()
conta2.extrato()

print("Teste Depositando".center(30))
conta1.extrato()
conta1.deposita(100)
conta1.extrato()

print("Teste sacando".center(30))
conta1.extrato()
conta1.saca(450)
conta1.extrato()

conta3.saca(5000)
