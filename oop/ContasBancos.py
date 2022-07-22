from os import system

system('clear')


class ContaCorrente:

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta


conta_jefersom = ContaCorrente('Jefersom', '222.545.555-67', '0212', '55500')

print(f'Nome: {conta_jefersom.nome}')
print(f'CPF: {conta_jefersom.cpf}')
print('-' * 20)
