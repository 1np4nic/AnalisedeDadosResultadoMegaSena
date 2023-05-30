import pandas as pd

# Carregando os dados
df = pd.read_csv('mega_sena.csv', delimiter=',')

# Selecione as colunas de bolas_sorteadas
bolas_sorteadas = ['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6']

# Criar novas colunas para pares e ímpares
df['pares'] = df[bolas_sorteadas].apply(lambda row: sum(n % 2 == 0 for n in row), axis=1)
df['impares'] = df[bolas_sorteadas].apply(lambda row: sum(n % 2 != 0 for n in row), axis=1)

# Criar coluna de combinação
df['combinacao'] = df['pares'].astype(str) + ',' + df['impares'].astype(str)

# Criar um novo DataFrame com as colunas desejadas e salvar em um arquivo CSV
resultado = df[['pares', 'impares', 'combinacao']]
resultado.to_csv('resultado_combinacao.csv', index=False)
