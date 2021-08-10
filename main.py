import copy

from src.Item import Item
from src.SimulatedAnnealing import simulated_annealing
from src.Knapsack import Knapsack

if __name__ == '__main__':
    capacidade = 20
    numeroItens = 10
    peso = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    valor = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    temperaturaInicial = 100
    temperaturaFinal = 1
    fatorReducaoTemperatura = 0.9
    totalPertubacoes = 5

    iteracoes = 100

    itens = []
    for i in range(numeroItens):
        item = Item(peso[i], valor[i])
        itens.append(item)

    mochila = Knapsack(numeroItens)

    resultado = simulated_annealing(mochila, iteracoes, temperaturaInicial, temperaturaFinal, fatorReducaoTemperatura,
                                    itens,
                                    totalPertubacoes, capacidade)

    melhorIteracao = copy.deepcopy(resultado[1])
    print(' ----- MELHOR SOLUCAO -----')
    resultado[0].imprimir(melhorIteracao, itens, resultado[2], resultado[3])
