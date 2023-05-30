import pandas as pd

# Carregar o conjunto de dados
df = pd.read_csv('mega_sena.csv', delimiter=',')

# Manter apenas as colunas de números
df_numeros = df[['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6']]

# Análise de Frequência
# Achatar os valores em df_numeros para uma única série de números
# Calcular a frequência de cada número e salvar o resultado em 'frequencia.csv'
numbers = df_numeros.values.flatten()
freq_series = pd.Series(numbers)
frequencia = freq_series.value_counts().sort_index()
frequencia_df = frequencia.reset_index()
frequencia_df.columns = ['Number', 'frequencia']
frequencia_df.to_csv('frequencia.csv', index=False)

# Análise de Pares e Ímpares
# Calcular o número de pares e ímpares em cada linha
# Criar uma nova coluna 'combinacao' com a combinação de pares e ímpares como uma string
# Salvar o resultado em 'resultado_combinacao.csv'
df['pares'] = df_numeros.apply(lambda row: sum(n % 2 == 0 for n in row), axis=1)
df['impares'] = df_numeros.apply(lambda row: sum(n % 2 != 0 for n in row), axis=1)
df['combinacao'] = df['pares'].astype(str) + ',' + df['impares'].astype(str)
resultado = df[['pares', 'impares', 'combinacao']]
resultado.to_csv('resultado_combinacao.csv', index=False)

# Análise de Baixos e Altos
# Esta função calcula a quantidade de números baixos (≤30) e altos (>30) em cada linha
# Salvar o resultado em 'proporcao_baixos_altos.csv'
def baixos_altos_porporcao(row):
    baixo = sum([1 for n in row if n <= 30]) # Assumindo que 30 é a metade do intervalo de números
    alto = sum([1 for n in row if n > 30])
    return baixo, alto

df['baixo'], df['alto'] = zip(*df_numeros.apply(baixos_altos_porporcao, axis=1))
df[['baixo', 'alto']].to_csv('proporcao_baixos_altos.csv', index=False)
