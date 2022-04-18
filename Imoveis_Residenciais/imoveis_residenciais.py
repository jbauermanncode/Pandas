import pandas as pd
from tipos_de_imoveis import TiposDeImoveis

class ImoveisResidenciais():

    imoveis_residenciais = TiposDeImoveis()

    dados = imoveis_residenciais.dados

    def filtrar_dados_e_exportar_banco_de_dados(self):
        # criar series booleana usando o método isn()
        residencial = ['Quitinete', 'Casa', 'Apartamento', 'Casa de Condomínio', 'Casa de Vila']
        selecao = self.dados['Tipo'].isin(residencial)
        dados_residencial = self.dados[selecao]
        #apagar Tipo duplicados
        list(dados_residencial['Tipo'].drop_duplicates())
        dados_residencial.index = range(dados_residencial.shape[0])
        return dados_residencial.to_csv('aluguel_residencial.csv', sep=';', index=False)








