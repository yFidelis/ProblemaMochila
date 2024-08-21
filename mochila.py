import random

def gerar_itens_aleatorios(quantidade_itens, peso_maximo, valor_maximo):
    pesos = [random.randint(1, peso_maximo) for _ in range(quantidade_itens)]
    valores = [random.randint(1, valor_maximo) for _ in range(quantidade_itens)]
    return pesos, valores

def mochila(pesos, valores, capacidade):
    n = len(pesos)  # Número de itens
    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    # Preencher a matriz dp
    for i in range(1, n + 1):
        for c in range(1, capacidade + 1):
            if pesos[i - 1] <= c:  # Se o peso do item i pode ser incluído na mochila
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - pesos[i - 1]] + valores[i - 1])
            else:
                dp[i][c] = dp[i - 1][c]

    # Valor máximo estará em dp[n][capacidade]
    valor_maximo = dp[n][capacidade]

    # Para rastrear os itens que foram incluídos na mochila
    itens_selecionados = []
    c = capacidade
    for i in range(n, 0, -1):
        if dp[i][c] != dp[i - 1][c]:  # Significa que o item i foi incluído
            itens_selecionados.append(i - 1)  # Armazenar o índice do item
            c -= pesos[i - 1]  # Reduzir a capacidade restante

    itens_selecionados.reverse()  # Reverter a lista para obter na ordem original

    return valor_maximo, itens_selecionados

# Configurações para os itens aleatórios
quantidade_itens = 10  # Número de itens
peso_maximo = 10  # Peso máximo de cada item
valor_maximo = 100  # Valor máximo de cada item
capacidade_mochila = 30  # Capacidade da mochila

# Gerar itens aleatórios
pesos, valores = gerar_itens_aleatorios(quantidade_itens, peso_maximo, valor_maximo)

print("Pesos dos itens:", pesos)
print("Valores dos itens:", valores)

# Resolver o problema da mochila
valor_maximo, itens_selecionados = mochila(pesos, valores, capacidade_mochila)

print(f"O valor máximo que pode ser obtido é: {valor_maximo}")
print("Itens selecionados (índices):", itens_selecionados)
print("Pesos dos itens selecionados:", [pesos[i] for i in itens_selecionados])
print("Valores dos itens selecionados:", [valores[i] for i in itens_selecionados])
