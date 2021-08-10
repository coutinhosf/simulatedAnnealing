from src.Item import Item


class Knapsack:
    def __init__(self, tamanhoMochila):
        self.mochila = [False] * tamanhoMochila
        self.valorSolucao = 0
        self.pesoMochila = 0
        self.valorItens = 0

    def calcula_solucao(self, items: Item):
        total = 0
        for i in range(len(items)):
            if self.mochila[i]:
                total += items[i].getValor() / items[i].getPeso()

        self.valorSolucao = total

    def calcula_peso_mochila(self, items: Item):

        total = 0
        for i in range(len(items)):
            if self.mochila[i]:
                total += items[i].getPeso()

        self.pesoMochila = total

    def calcula_valor_itens_mochila(self, items: Item):

        total = 0
        for i in range(len(items)):
            if self.mochila[i]:
                total += items[i].getValor()

        self.valorItens = total

    def calculaMochila(self, items: Item):
        self.calcula_solucao(items)
        self.calcula_peso_mochila(items)
        self.calcula_valor_itens_mochila(items)

    def imprimir(self, totalIteracoes, items: Item):
        print('Iteracao: ' + str(totalIteracoes))
        print('MelhorSolucao:{ ')
        print(' | '.join(str(p) for p in self.mochila))
        print('}')
        print('Itens - { ')
        print('Peso e Valor: ', end='|')
        for i in range(len(items)):
            if self.mochila[i]:
                print(' ' + str(items[i].getPeso()) + ' ' + str(items[i].getValor()), end=' |')
            else:
                print(' ' + '0' + ' ' + '0', end=' |')
        print('}')
        print('Valor Solucao: ' + str(self.valorSolucao))
        print('Peso Mochila: ' + str(self.pesoMochila))
        print('Valor Mochila: ' + str(self.valorItens))
        print()
        print()
