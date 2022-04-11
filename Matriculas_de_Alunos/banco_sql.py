import pandas as pd
import numpy as np
from sqlalchemy import create_engine, MetaData, Table, inspect
from matriculas import Matriculas

class Banco_sql:

    matriculas = Matriculas()

    nomes_cursos = matriculas.cursos
    selecionando_cursos = matriculas.selecionando_cursos()
    nomes_alunos = matriculas.nomes
    matriculas_por_curso = selecionando_cursos.groupby('id_curso').count().join(matriculas.cursos['nome_do_curso']).rename(columns = {'id_alunos':'quantidade_alunos'})
    
    #criando_banco_sql(self):
    engine = create_engine('sqlite:///:memory:')
    matriculas_por_curso.to_sql('matriculas', engine)
    inspector = inspect(engine)

    # variaveis para busca no Banco:

    #matriculas em cursos com menos de 20 alunos
    query = 'select * from matriculas where quantidade_alunos < 20'
    matriculas_menor_vinte_alunos = pd.read_sql(query, engine)
    #só o nome do curso e a quantidade de alunos
    matriculas_curso_qtdalunos = pd.read_sql('matriculas', engine, columns=['id_curso','nome_do_curso','quantidade_alunos'])
    #cursos com muitas matriculas
    mais_matriculas = pd.read_sql('matriculas', engine, columns=['nome_do_curso','quantidade_alunos'])
    muitas_matriculas = mais_matriculas.query('quantidade_alunos > 70')

    #método para buscar no banco de dados as variáveis acima:
    def buscando_banco_sql(self):
        

        select_banco_sql = int(input('Escolha a opção: \n' +' [0]Banco_SQL quantidade_alunos < 20 \n' + ' [1]Banco_SQL Curso e Qtd alunos \n' + ' [2]Banco SQL com mais de 70 alunos: '))

        if select_banco_sql == 0:
            print('Banco_SQL quantidade_alunos < 20')
            print(self.matriculas_menor_vinte_alunos)
            self.matriculas_menor_vinte_alunos.to_csv('dados/matriculas_menor_vinte_alunos.csv', index=False)
        elif select_banco_sql == 1:
            print('Banco_SQL Curso e Qtd alunos')
            print(self.matriculas_curso_qtdalunos)
            self.matriculas_curso_qtdalunos.to_csv('dados/matriculas_curso_qtdalunos.csv', index=False)
        elif select_banco_sql == 2:
            print('Banco SQL com mais de 70 alunos')
            print(self.muitas_matriculas)
            self.muitas_matriculas.to_csv('dados/muitas_matriculas.csv', index=False)
        else:
            print('Não existe Banco SQL')
        
        return select_banco_sql


    def escrevendo_no_sql(self):
        matriculas = self.selecionando_cursos
        cursos = self.nomes_cursos
        self.muitas_matriculas.to_sql('muitas_matriculas', con=self.engine)
        #fazer input do id do curso
        id_curso = int(input('Digite o id do curso: '))
        nome_curso = cursos.loc[id_curso]
        nome_curso = nome_curso.nome_do_curso
        
        proxima_turma = matriculas.query(f"id_curso == {id_curso}")
        proxima_turma = proxima_turma.set_index('id_alunos').join(self.nomes_alunos.set_index('id_alunos'))['nome'].to_frame()
        
        proxima_turma.rename(columns = {'nome': f'Alunos do curso de {nome_curso}'})
        return proxima_turma.to_excel(f'dados/Turma_{nome_curso}.xlsx', index=False)



