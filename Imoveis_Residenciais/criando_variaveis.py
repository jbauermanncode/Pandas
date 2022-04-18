import pandas as pd
from tratamento_dados_faltantes import TratamentoDadosFaltantes

class Criando_variaveis:

    criando_variaveis = TratamentoDadosFaltantes()

    dados = criando_variaveis.dados

    def valor_bruto(self):
        self.dados['Valor Bruto'] = self.dados['Valor'] + self.dados['Condominio'] + self.dados['IPTU']
        return self.dados

    def valor_bruto_m2(self):
        self.dados['Valor Bruto m²'] = (self.dados['Valor Bruto'] / self.dados['Area']).round(2)
        return self.dados

    def valor_m2(self):
        self.dados['Valor m²'] = self.dados['Valor'] / self.dados['Area']
        self.dados['Valor m²'] = self.dados['Valor m²'].round(2)
        return self.dados

    def tipo_agregado(self):
        casa = ['Casa', 'Casa de Condomínio', 'Casa de Vila']
        self.dados['Tipo Agregado'] = self.dados['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Apartamento')
        return self.dados

    def excluir_variaveis(self):
        self.dados.drop(['Valor Bruto', 'Valor Bruto m²'], axis = 1, inplace = True)
        return self.dados.to_csv('aluguel_residencial_novo.csv', sep = ';', index =False)



dados = Criando_variaveis()

dados.valor_bruto()
dados.valor_m2()
dados.valor_bruto_m2()
dados.tipo_agregado()
dados.excluir_variaveis()

