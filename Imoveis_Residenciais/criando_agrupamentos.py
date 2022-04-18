from matplotlib import matplotlib_fname
import pandas as pd
matplotlib_fname 
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(20, 10))

from tratamento_dados_faltantes import TratamentoDadosFaltantes

class Criando_agrupamentos:

    criando_agrupamentos = TratamentoDadosFaltantes()

    dados = criando_agrupamentos.dados

    bairros = ['Barra da Tijuca', 'Copacabana', 'Ipanema', 'Leblon', 'Botafogo', 'Flamengo', 'Tijuca']
    selecao = dados['Bairro'].isin(bairros)
    dados = dados[selecao]
    grupo_bairro = dados.groupby('Bairro')

    def agrupa_bairro(self):
        return self.grupo_bairro[['Valor', 'Condominio']].mean().round(2)

    # ESTATISTICAS DESCRITIVAS
    def min_max_sum(self):
        return self.grupo_bairro['Valor'].aggregate(['min', 'max', 'sum']).rename(columns={'min': 'Mínimo', 'max': 'Máximo', 'sum': 'Soma'})
    
    def grafico_valor_medio(self):
        font = {'family': 'Helvetica',
                'weight': 'bold',
                'size': 12}
        plt.rc('font', **font)
        fig = self.grupo_bairro['Valor'].mean().plot.bar(color='blue')
        fig.set_ylabel('Valor do Aluguel')
        fig.set_title('Valor Médio do Aluguel por Bairro', {'fontsize': 22})
        return plt.show()

        

dados = Criando_agrupamentos()

dados.agrupa_bairro()
dados.min_max_sum()
dados.grafico_valor_medio()