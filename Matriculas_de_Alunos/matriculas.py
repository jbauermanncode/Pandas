from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from data_frame_alunos import Data_frame_alunos
from cursos import Cursos

class Matriculas:

    alunos = Data_frame_alunos()
    cursos = Cursos('http://tabela-cursos.herokuapp.com/index.html')

    quantidade_nomes = alunos.qtd_nomes()
    alunos.incluindo_id_dos_alunos()
    nomes = alunos.criando_dominios()
    cursos = cursos.alterando_index_cursos()
    total_alunos = len(nomes)

    nomes['matriculas'] = np.ceil(np.random.exponential(size=total_alunos)* 1.5).astype(np.int)

    # Vizualizar gráfico da quantidade de matriculas por aluno
    def vizualizar_matriculas_grafico(self):
        sns.distplot(self.nomes.matriculas)
        return plt.show()

    def selecionando_cursos(self):
        todas_matriculas = []
        x = np.random.rand(20)
        prob = x / sum(x)

        for index, row in self.nomes.iterrows():
            id = row.id_alunos
            matriculas = row.matriculas
            for i in range(matriculas):
                mat = [id, np.random.choice(self.cursos.index, p = prob)]
                todas_matriculas.append(mat)

        return pd.DataFrame(todas_matriculas, columns = ['id_alunos', 'id_curso'])


import json

matriculas = Matriculas()

vizualizar_grafico = matriculas.vizualizar_matriculas_grafico()
selecionando_cursos = matriculas.selecionando_cursos()
quantidade_nomes = matriculas.quantidade_nomes

matriculas_por_curso = selecionando_cursos.groupby('id_curso').count().join(matriculas.cursos['nome_do_curso']).rename(columns = {'id_alunos':'quantidade_alunos'})

print(matriculas_por_curso)
print(f'Quantidade de alunos: {quantidade_nomes}')

# Saída em diferentes formatos

#Saída CSV
matriculas_por_curso.to_csv('matriculas_por_curso.csv', index=False)

#Saída JSON
print('\n')
print('##' * 60,'\n')
matriculas_json = matriculas_por_curso.to_json()
print('Saída em JSON:', '\n')
print(matriculas_json)

#Saída HTML
print('\n')
print('##' * 60,'\n')
matriculas_html = matriculas_por_curso.to_html()
print('Saída em HTML:', '\n')
print(matriculas_html)