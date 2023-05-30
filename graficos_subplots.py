import pandas as pd
import matplotlib.pyplot as plt

# Carregando os dados
df = pd.read_csv('mega_sena.csv', delimiter=',')

# Concatenando todas as colunas de bola em uma série
balls = pd.concat([df[f'bola {i}'] for i in range(1, 7)])

# Contando a frequência de cada número
num_frequency = balls.value_counts()

# Criando um novo DataFrame e ordenando por frequência
df_freq = pd.DataFrame({'Number': num_frequency.index, 'Frequency': num_frequency.values}).sort_values('Frequency')

df_freq_sorted = df_freq.sort_values(by='Frequency', ascending=True)

# Calculando as percentagens
total_num = df_freq_sorted["Frequency"].sum()
df_freq_sorted["Percentage"] = df_freq_sorted["Frequency"] / total_num * 100

# Definindo as colunas que contêm os números sorteados
draw_columns = [f'bola {i}' for i in range(1, 7)]

# Contando a quantidade de números pares e ímpares
df['even'] = df[draw_columns].apply(lambda row: sum(n % 2 == 0 for n in row), axis=1)
df['odd'] = df[draw_columns].apply(lambda row: sum(n % 2 != 0 for n in row), axis=1)

# Criando uma nova coluna com a combinação dos números ímpares e pares como uma string
df['combinacao'] = df['odd'].astype(str) + ',' + df['even'].astype(str)

# Contando a frequência de cada combinação
freq = df['combinacao'].value_counts()

# Calculando a percentagem
total_comb = freq.sum()
percentages = freq / total_comb * 100

# Agrupando pela contagem de números baixos e altos e contando quantos sorteios tiveram essa combinação
df['low'], df['high'] = zip(*df[draw_columns].apply(lambda row: (sum(1 for n in row if n <= 30), sum(1 for n in row if n > 30)), axis=1))
grouped_df = df.groupby(['low', 'high']).size().reset_index(name='frequency')

# Criando uma nova coluna para a combinação de números baixos e altos como uma string para exibir no gráfico
grouped_df['low_high'] = grouped_df['low'].astype(str) + ', ' + grouped_df['high'].astype(str)

# Calculando a porcentagem
total_low_high = grouped_df['frequency'].sum()
grouped_df['percentage'] = grouped_df['frequency'] / total_low_high * 100

# Criando o objeto de subplots
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(12,18))

# Plotando os gráficos de barras
bars = axes[0].bar(df_freq_sorted['Number'].astype(str), df_freq_sorted['Frequency'], label='Frequência dos Números')
bars2 = axes[1].bar(freq.index, freq.values, label='Frequência de Combinação de Pares e Ímpares')
bars3 = axes[2].bar(grouped_df['low_high'], grouped_df['frequency'], label='Frequência de Contagem de Números Baixos e Altos')

# Adicionando a porcentagem acima das barras
for ax, bars, percentages in zip(axes, [bars, bars2, bars3], [df_freq_sorted["Percentage"], percentages, grouped_df['percentage']]):
    for bar, percentage in zip(bars, percentages):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height,
                f'{percentage:.2f}%', ha='center', va='bottom',fontsize=6)

# Definindo os labels para os eixos x e y
for ax in axes:
    ax.set_xlabel('Combinação')
    ax.set_ylabel('Frequência')
    #ax.legend()

plt.tight_layout()
plt.show()