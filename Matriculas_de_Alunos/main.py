from data_frame_alunos import Data_frame_alunos
from matriculas import Matriculas
from banco_sql import Banco_sql

import json

alunos = Data_frame_alunos()
matriculas = Matriculas()
banco_sql = Banco_sql()

vizualizar_grafico = matriculas.vizualizar_matriculas_grafico()
selecionando_cursos = matriculas.selecionando_cursos()
quantidade_nomes = matriculas.quantidade_nomes

matriculas_por_curso = selecionando_cursos.groupby('id_curso').count().join(matriculas.cursos['nome_do_curso']).rename(columns = {'id_alunos':'quantidade_alunos'})

print(matriculas_por_curso)
print(f'Quantidade de alunos: {quantidade_nomes}')

# Saída em diferentes formatos
def saida_em_diferente_formatos():
    saida = input('Você quer imprimir os dados em algum formato?(yes/no) ')
    
    while (saida == 'yes'):

        select_saida = int(input('Escolha a opção: \n' +' [0]Saída em CSV \n' + ' [1]Saída em JSON \n' + ' [2]Saída em HTML \n' + ' [3]Saída em EXCEL: '))
        saida = input('Você quer imprimir os dados em algum formato?(yes/no) ')
        
        if (select_saida == 0):
            #Saída CSV
            matriculas_por_curso.to_csv('dados/matriculas_por_curso.csv', index=False)
        elif (select_saida == 1):
            print('\n')
            #Saída JSON
            matriculas_por_curso.to_json('dados/matriculas_json.json', index=False)
        elif (select_saida == 2):
            #Saída HTML
            matriculas_por_curso.to_html('dados/matriculas_html.html', index=False)
        elif (select_saida == 3):
            matriculas_por_curso.to_excel('dados/matriculas_por_curso.xlsx', index=False)
        else:
            print('Número Inválido!')

print('Data Frame Feminino')
print(f'Quantidade de Nomes Femininos: {len(alunos.feminino)}')
print(alunos.feminino.sample(10))
print('##' * 40)
print('Data Frame Masculino')
print(f'Quantidade de Nomes Masculinos: {len(alunos.masculino)}')
print(alunos.masculino.sample(10))
print('##' * 40)
print('Junção dos Frames: Masculino e Feminino')
print(f'Quantidade de Nomes: {alunos.qtd_nomes()}')
print(alunos.nomes.sample(10))
print('##' * 40)
print(alunos.incluindo_id_dos_alunos())
print('##' * 40)
print(alunos.criando_dominios())
saida_em_diferente_formatos()
banco_sql.buscando_banco_sql()
banco_sql.escrevendo_no_sql()
