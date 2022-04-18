from selecoes_e_frequencias import SelecoesEfrequencias
from tipos_de_imoveis import TiposDeImoveis
from imoveis_residenciais import ImoveisResidenciais

dados_tipos = TiposDeImoveis()
dados_imoveis_residenciais = ImoveisResidenciais()
dados_aluguel_residencial = SelecoesEfrequencias()

#print(dados.organizando_vizualizacao())
#dados.filtrar_dados_e_exportar_banco_de_dados()

print(f'#' * 20 + '  Seleção de Aluguéis Residenciais  ' + '#' * 20 + '\n\n')
dados_aluguel_residencial.quartos_aluguel()


