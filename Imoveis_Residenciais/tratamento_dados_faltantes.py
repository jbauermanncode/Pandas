import pandas as pd
from tipos_de_imoveis import TiposDeImoveis

class TratamentoDadosFaltantes:
    
    tratamentoDadosFaltantes = TiposDeImoveis()

    dados = tratamentoDadosFaltantes.dados

    #retorna onde os dados são nulos True e onde eles não são False
    def dados_nulos(self):
        return self.dados.isnull()

    #retorna onde os dados são nulos False e onde eles não são True
    def dados_nao_nulos(self):
        return self.dados.notnull()

    def tratamento_dados_faltantes(self):
        self.dados[self.dados['Valor'].isnull()]
        A = self.dados.shape[0]
        self.dados.dropna(subset = ['Valor'], inplace = True)
        B = self.dados.shape[0]
        A - B

        selecao = (self.dados['Tipo'] == 'Apartamento') & (self.dados['Condominio'].isnull())
        # ~ inverte a Series booleana
        a = self.dados.shape[0]
        dados = self.dados[~selecao]
        b = dados.shape[0]
        dados = dados.fillna({'Condominio': 0, 'IPTU': 0})
        print(dados)
        print(dados.info())
        dados.to_csv('aluguel_residencial_tratado.csv', sep = ';', index =False)

tratamentoDadosFaltantes = TratamentoDadosFaltantes()

tratamentoDadosFaltantes.tratamento_dados_faltantes()