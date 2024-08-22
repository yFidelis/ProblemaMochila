import numpy as np
from tabulate import tabulate

# Resolve o problema da mochila e constrói a tabela dinamicamente
def knapsack(capacidade, pesos, valores):
    n = len(valores)
    dp = np.zeros((n+1, capacidade+1))

    for i in range(1, n+1):
        for w in range(1, capacidade+1):
            if pesos[i-1] <= w:
                dp[i][w] = max(valores[i-1] + dp[i-1][w-pesos[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    w = capacidade
    itensEscolhidos = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            itensEscolhidos.append(i)
            w -= pesos[i-1]

    return dp, dp[n][capacidade], itensEscolhidos

# Função principal
def runKnapsackExample():
    # Pesos e valores fornecidos
    pesos = [1, 3, 5, 8]
    valores = [1, 5, 8, 10]

    # Capacidade máxima da mochila
    capacidade = 11

    # Executa o algoritmo da mochila e obtém a tabela
    tabela, valorMaximo, itensEscolhidos = knapsack(capacidade, pesos, valores)

    # Imprime a tabela
    capacidadeShow = list(range(1, capacidade + 1))
    capacidadeShow = [0] + capacidadeShow[:]
    itensShow = [0] + pesos[:]
    
    print("Tabela de valores:")
    print(tabulate(tabela, headers=capacidadeShow, showindex=itensShow, tablefmt="mixed_grid"))

    # Imprime os resultados
    print(f"\nValor máximo que pode ser carregado: {valorMaximo}")
    print(f"Itens escolhidos (índice): {itensEscolhidos}")

    for item in itensEscolhidos:
        print(f"Item com peso {pesos[item-1]} e valor {valores[item-1]} foi adicionado à mochila.")

    capacidadeUsada = sum(pesos[item-1] for item in itensEscolhidos)
    capacidadeRestante = capacidade - capacidadeUsada
    print(f"Capacidade utilizada: {capacidadeUsada} ")
    print(f"Capacidade restante: {capacidadeRestante} ")

if __name__ == "__main__":
    runKnapsackExample()
