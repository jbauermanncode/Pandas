from matplotlib import matplotlib_fname
import pandas as pd
matplotlib_fname 
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(14, 6))

from tratamento_dados_faltantes import TratamentoDadosFaltantes

class Identificando_e_removendo_outliers:

    identificando_e_removendo_outliers = TratamentoDadosFaltantes()

    dados = identificando_e_removendo_outliers.dados

    def boxplot(self):
        self.dados.boxplot(['Valor'])
        return plt.show()

    dados[dados['Valor'] >= 500000]
    valor = dados['Valor']

    # Primeiro, calcularemos Q1 o primeiro quartil
    Q1 = valor.quantile(.25)

    # Em seguida calcularemos o Q3
    Q3 = valor.quantile(.75)

    # E calcularemos o IIQ
    iiq = Q3 - Q1

    # Precisamos, ainda calcular os limites
    limite_inferior = Q1 - 1.5 * iiq

    limite_superior = Q3 + 1.5 * iiq

    # Fazer um novo boxplot
    selecao = (valor >= limite_inferior) & (valor <= limite_superior)
    dados_new = dados[selecao]

    def new_boxplot(self):
        self.dados_new.boxplot(['Valor'])
        return plt.show()

    def historiograma(self):
        self.dados.hist(['Valor'])
        self.dados_new.hist(['Valor'])
        return plt.show()

    # Separar por tipo
    def boxplot_valor_e_tipo(self):
        self.dados.boxplot(['Valor'], by = ['Tipo'])
        return plt.show()

    grupo_tipo = dados.groupby('Tipo')['Valor']

    # Primeiro, calcularemos Q1 o primeiro quartil
    Q1_tipo = grupo_tipo.quantile(.25)

    # Em seguida calcularemos o Q3
    Q3_tipo = grupo_tipo.quantile(.75)

    # E calcularemos o IIQ
    iiq_tipo = Q3_tipo - Q1_tipo

    # Precisamos, ainda calcular os limites
    limite_inferior_tipo = Q1_tipo - 1.5 * iiq_tipo

    limite_superior_tipo = Q3_tipo + 1.5 * iiq_tipo

    def grupo_tipo_boxplot(self):
        grupo_tipo = self.grupo_tipo
        dados = self.dados
        limite_inferior = self.limite_inferior_tipo
        limite_superior = self.limite_superior_tipo

        self.dados_new = pd.DataFrame()
        for tipo in grupo_tipo.groups.keys():
            eh_tipo = self.dados['Tipo'] == tipo
            eh_dentro_limite = (dados['Valor'] >= limite_inferior[tipo]) & (dados['Valor'] <= limite_superior[tipo])
            selecao = eh_tipo & eh_dentro_limite
            dados_selecao = dados[selecao]
            self.dados_new = pd.concat([self.dados_new, dados_selecao])
        self.dados_new.boxplot(['Valor'], by = ['Tipo'])
        plt.show()

        return self.dados_new.to_csv('aluguel_residencial_sem_outliers.csv', sep=';', index=False)

dados = Identificando_e_removendo_outliers()

dados.grupo_tipo_boxplot()