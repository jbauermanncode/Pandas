import pandas as pd
import numpy as np
from sqlalchemy import create_engine, MetaData, Table, inspect
from matriculas import Matriculas

class Banco_sql:

    matriculas = Matriculas()

    selecionando_cursos = matriculas.selecionando_cursos()

    matriculas_por_curso = selecionando_cursos.groupby('id_curso').count().join(matriculas.cursos['nome_do_curso']).rename(columns = {'id_alunos':'quantidade_alunos'})
    
    #criando_banco_sql(self):
    engine = create_engine('sqlite:///:memory:')
    matriculas_por_curso.to_sql('matriculas', engine)
    inspector = inspect(engine)

    def buscando_banco_sql(self):
        query = 'select * from matriculas where quantidade_alunos < 20'
        matriculas_menor_vinte_alunos = pd.read_sql(query, self.engine)
        
        matriculas_curso_qtdalunos = pd.read_sql('matriculas', self.engine, columns=['nome_do_curso','quantidade_alunos'])
        
        mais_matriculas = pd.read_sql('matriculas', self.engine, columns=['nome_do_curso','quantidade_alunos'])
        muitas_matriculas = mais_matriculas.query('quantidade_alunos > 70')

        select_banco_sql = int(input('Escolha a opção: \n' +' Banco_SQL quantidade_alunos < 20 \n' + ' Banco_SQL Curso e Qtd alunos \n' + ' Banco SQL com mais de 70 alunos: '))

        if select_banco_sql == 0:
            print('Banco_SQL quantidade_alunos < 20')
            print(matriculas_menor_vinte_alunos)
        elif select_banco_sql == 1:
            print('Banco_SQL Curso e Qtd alunos')
            print(matriculas_curso_qtdalunos)
        elif select_banco_sql == 2:
            print('Banco SQL com mais de 70 alunos')
            print(muitas_matriculas)
        else:
            print('Não existe Banco SQL')
        
        return select_banco_sql


banco_sql = Banco_sql()

banco_sql.buscando_banco_sql()
