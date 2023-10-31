import os

# Kauan Rodrigues
# Simulação do Mercado de Ações:

class SimuladorAcoes:

    def __init__(self, saldo_inicial=890500):
        self.saldo = saldo_inicial
        self.acoes = {'IMÓVEL': 90, 'FACEBOOK': 200, 'CONCESSIONÁRIA': 400, 'AEROPORTO': 250}
        self.precos = {'IMÓVEL': 550.0, 'FACEBOOK': 2500.0, 'CONCESSIONÁRIA': 800.0, 'AEROPORTO': 405.0}

# Jonas Moreira
# Lógica de Investimento:


    def comprar_acao(self, nome_acao, quantidade):
        if nome_acao in self.acoes:
            preco_acao = self.precos[nome_acao]
            preco_total = preco_acao * quantidade
            if preco_total <= self.saldo:
                self.acoes[nome_acao] += quantidade
                self.saldo -= preco_total
                print(f"Você comprou {quantidade} ações de {nome_acao} a ${preco_acao} cada.")
            else:
                print("Saldo insuficiente para comprar as ações.")
        else:
            print("Ação não encontrada.")

    def vender_acao(self, nome_acao, quantidade):
        if nome_acao in self.acoes:
            if quantidade <= self.acoes[nome_acao]:
                preco_acao = self.precos[nome_acao]
                preco_total = preco_acao * quantidade
                self.acoes[nome_acao] -= quantidade
                self.saldo += preco_total
                print(f"Você vendeu {quantidade} ações de {nome_acao} a ${preco_acao} cada.")
            else:
                print("Você não possui ações suficientes para vender.")
        else:
            print("Ação não encontrada.")

    def verificar_portfolio(self):
        print("\nPortfólio atual:")
        for acao, quantidade in self.acoes.items():
            print(f"{acao}: {quantidade} ações")

    def verificar_saldo(self):
        print(f"\nSeu saldo atual é de ${self.saldo}.")

if __name__ == "__main__":
    simulador = SimuladorAcoes()

# Vinicius Eduardo
# Interface do Usuário:

    while True:
        os.system('cls')  # Limpar a tela
        print("\nBem-vindo ao Simulador do Mercado de Ações!")
        print("1. Comprar Ação")
        print("2. Vender Ação")
        print("3. Verificar Portfólio")
        print("4. Verificar Saldo")
        print("5. Sair")

        escolha = input("Por favor, selecione uma opção: ")

#  Kacios Gleybson
# Integração e Testes:

        if escolha == '1':
            nome_acao = input("Digite o nome da ação: ")
            quantidade = int(input("Digite a quantidade a comprar: "))
            simulador.comprar_acao(nome_acao, quantidade)
        elif escolha == '2':
            nome_acao = input("Digite o nome da ação: ")
            quantidade = int(input("Digite a quantidade a vender: "))
            simulador.vender_acao(nome_acao, quantidade)
        elif escolha == '3':
            simulador.verificar_portfolio()
        elif escolha == '4':
            simulador.verificar_saldo()
        elif escolha == '5':
            print("Saindo do simulador. Até logo!")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")
        input("\nPressione Enter para continuar...")
