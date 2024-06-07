class Titular(object):
    def __init__(self,cpf,nome,sobrenome):
        self.cpf = cpf
        self.nome = nome
        self.sobrenome = sobrenome
    def get_cpf(self):
        return self.cpf
    def get_nome(self):
        return self.nome
    def set_nome(self,novo_nome):
        self.nome = novo_nome
        return self.nome
    def get_sobrenome(self):
        return self.sobrenome
    def nome_completo(self):
        nome_completo = f"{self.nome} {self.sobrenome}"
        return nome_completo

class Conta:
    def __init__(self,numero,obj_titular,saldo,limite):
        self.numero = numero
        self.titular = obj_titular
        self.saldo = saldo
        self.limite = limite
    def get_numero(self):
        return self.numero
    def get_titular(self):
        return self.titular
    def get_saldo(self):
        return self.saldo
    def set_saldo(self,novo_saldo):
        self.saldo = novo_saldo
        return self.saldo
    def get_limite(self):
        return self.limite
    def extrato1(self):
        return f"{self.numero},{self.saldo}"
    def extrato2(self):
        return f"{conta1.get_titular().get_nome()},{conta1.get_titular().get_sobrenome()},{conta1.get_titular().get_cpf()},{self.numero},{self.saldo}"
    def deposito(self,valor):
        self.saldo += valor
        return self.saldo
    def saque(self,valor):
        if valor > self.saldo + self.limite:
            print("Valor acima do saldo")
        else:
            self.saldo -= valor
            return self.saldo
    def transferencia(self,destino):
        valor = float(input("Valor da transferencia:"))
        if valor > self.saldo + self.limite:
            print("transferência inválida")
        else:
            self.saldo -= valor
            destino.saldo += valor

if __name__ == '__main__':
    titular1 = Titular(100,"Eduardo","Giannetti")
    titular2 = Titular(150,"Lucas","Mendes")
    conta1 = Conta(200,titular1,700,1000)
    conta2 = Conta(400,titular2,300,1200)
    print(titular1.nome_completo())
    print(conta1.get_titular().get_nome())
    print(conta1.extrato2())
    conta1.transferencia(conta2)
    print(conta1.get_saldo())
