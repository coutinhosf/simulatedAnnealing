import copy
import random
import numpy as np

from src.Knapsack import Knapsack


def factor_boltzmann(valorMochilaAtual, valorMochilaPertubacao, temperaturaAtual):
    probabilidade = np.exp(-np.absolute(valorMochilaPertubacao - valorMochilaAtual) / temperaturaAtual)

    return probabilidade


def pertubacao(mochila: Knapsack):
    totalItensMochila = len(mochila.mochila)
    totalPertubacao = random.randint(1, totalItensMochila)
    mochilaNova = copy.deepcopy(mochila)

    for i in range(totalPertubacao):
        posicaoSorteada = random.randint(0, totalItensMochila - 1)
        if mochila.mochila[posicaoSorteada]:
            mochilaNova.mochila[posicaoSorteada] = False
        else:
            mochilaNova.mochila[posicaoSorteada] = True

    return mochilaNova


def simulated_annealing(mochila: Knapsack, iteracoes, temperaturaAtual, temperaturaFinal, fatorReducao, items,
                        pertubacoes, capacidade):
    mochilaAlternativa = pertubacao(mochila)
    mochilaAlternativa.calculaMochila(items)
    totalIteracoes = 0
    totalPertubacoes = 0
    melhorMochila = copy.deepcopy(mochila)
    melhoriteracao = 0

    while (temperaturaAtual > temperaturaFinal) and (totalIteracoes < iteracoes):
        totalIteracoes += 1

        while totalPertubacoes < pertubacoes:
            totalPertubacoes += 1
            deltaF = mochilaAlternativa.valorSolucao - mochila.valorSolucao
            probabilidade = factor_boltzmann(mochila.valorSolucao, mochilaAlternativa.valorSolucao, temperaturaAtual)
            intervalo = np.random.random()

            if (deltaF < 0) or (probabilidade > intervalo):
                if capacidade > mochilaAlternativa.pesoMochila:
                    mochila = copy.deepcopy(mochilaAlternativa)
                    if mochila.valorSolucao > melhorMochila.valorSolucao:
                            melhorMochila = copy.deepcopy(mochila)
                            melhoriteracao = totalIteracoes

            mochilaAlternativa = pertubacao(mochila)
            mochilaAlternativa.calculaMochila(items)

        totalPertubacoes = 0
        mochila.imprimir(totalIteracoes, items)
        temperaturaAtual = fatorReducao * temperaturaAtual

    return [melhorMochila , melhoriteracao]
