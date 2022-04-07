from matriculas import Matriculas
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