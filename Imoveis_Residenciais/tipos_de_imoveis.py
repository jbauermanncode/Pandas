import pandas as pd
from base_de_dados import BaseDeDados


class TiposDeImoveis():
    
    base_de_dados = BaseDeDados(input('Digite arquivo: '))

    dados = pd.read_csv(f'{base_de_dados.get_imoveis()}', sep = ';')

    tipo_de_imovel = dados.Tipo
    #apagar os tipos que repetem
    tipo_de_imovel.drop_duplicates(inplace = True)

    def organizando_vizualizacao(self):
        tipo_de_imovel = pd.DataFrame(self.tipo_de_imovel)
        tipo_de_imovel.index = range(tipo_de_imovel.shape[0])
        tipo_de_imovel.columns.name = 'id'
        return tipo_de_imovel


