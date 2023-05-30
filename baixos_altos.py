import pandas as pd

# Carregando os dados
df = pd.read_csv('mega_sena.csv', delimiter=',')

# Selecione as colunas de bolas_sorteadas
df_numbers = df[['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6']]

# Esta função calcula a quantidade de números baixos (≤30) e altos (>30) em cada linha e salva o resultado em 'baixo_alto_ratio.csv'
def baixos_altos_porporcao(row):
    baixo = sum([1 for n in row if n <= 30]) # Assumindo que 30 é a metade do intervalo de números
    alto = sum([1 for n in row if n > 30])
    return baixo, alto

df['baixo'], df['alto'] = zip(*df_numbers.apply(baixos_altos_porporcao, axis=1))
df[['baixo', 'alto']].to_csv('proporcao_baixos_altos.csv', index=False)
