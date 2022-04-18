import pandas as pd
from tipos_de_imoveis import TiposDeImoveis

class SelecoesEfrequencias:

    selecoes_e_frequencias = TiposDeImoveis()

    dados = selecoes_e_frequencias.dados

    #Selecione os imóveis classificados com tipo 'Apartamento'
    def selecao_apartamento(self):
        selecao = self.dados['Tipo'] == 'Apartamento'
        n = self.dados[selecao]
        n1 = self.dados[selecao].shape[0]
        print(f"Nº de imóveis classificados com tipo 'Apartamento' -> {n1} \n\n")
        print(n)

    #Selecione os imóveis classificados com tipos 'Casa', 'Casa de Condominio', e 'Casa de Vila'
    def tipo_casa(self):
        selecao = (self.dados['Tipo'] == 'Casa') | (dados['Tipo'] == 'Casa de Condomínio') | (dados['Tipo'] == 'Casa de Vila')
        n = self.dados[selecao]
        n1 = self.dados[selecao].shape[0]
        print(f"Nº de imóveis classificados com tipos 'Casa', 'Casa de Condominio', e 'Casa de Vila' -> {n1} \n\n")
        print(n)

    #Selecione os imóveis com área entre 60 e 100 metros quadrados, incluindo os limites
    #60 <= Area <= 100
    def area_sessenta_cem(self):
        selecao = (self.dados['Area'] >= 60) & (self.dados['Area'] <= 100)
        n = self.dados[selecao]
        n1 = self.dados[selecao].shape[0]
        print(f"Nº de imóveis com área entre 60 e 100 metros quadrados, incluindo os limites -> {n1}")
        print(n)

    #Selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00
    def quartos_aluguel(self):
        selecao = (self.dados['Quartos'] >= 4) & (self.dados['Valor'] < 2000)
        n = self.dados[selecao]
        n1 = self.dados[selecao].shape[0]
        print(f"Nº de imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00 -> {n1} \n\n")
        print(n)

dados = SelecoesEfrequencias()


    