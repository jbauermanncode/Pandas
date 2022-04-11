import html5lib
import pandas as pd

class Cursos:

    def __init__(self, url):
        self.url = url
        self.cursos = pd.read_html(self.url)

    def get_url(self):
        return self.url

    def set_url(self, url):
        self.url = url
    
    # transformar a tabela em data frame e alterar o index dos cursos
    def alterando_index_cursos(self):
        cursos = self.cursos[0]
        cursos = cursos.rename(columns = {'Nome do curso':'nome_do_curso'})
        cursos['id'] = cursos.index + 1
        cursos = cursos.set_index('id')
        return cursos
