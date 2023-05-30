import pandas as pd

# Carregando os dados
df = pd.read_csv('mega_sena.csv', delimiter=',')

# Mantendo apenas as colunas de números
df_numbers = df[['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6']]

# 1. Análise de Frequência
numbers = df_numbers.values.flatten()
freq_series = pd.Series(numbers)
frequency = freq_series.value_counts().sort_index()
frequency_df = frequency.reset_index()
frequency_df.columns = ['Number', 'Frequency']
frequency_df.to_csv('frequency.csv', index=False)