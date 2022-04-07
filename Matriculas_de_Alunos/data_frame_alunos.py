from nomes_alunos import Nomes_alunos
import pandas as pd
import numpy as np

class Data_frame_alunos:
    data = Nomes_alunos('https://guilhermeonrails.github.io/nomes_ibge/nomes-f.json', 'https://guilhermeonrails.github.io/nomes_ibge/nomes-m.json')
    
    feminino = pd.read_json(data.get_nome_feminino())
    masculino = pd.read_json(data.get_nome_masculino())
    
    # Quantidade de alunos somando os Data Frames
    def qtd_nomes(self):
        return str(len(self.feminino) + len(self.masculino))
    
    # Juntando os dois Data Frames
    frames = [feminino, masculino]
    nomes = pd.concat(frames)['nome'].to_frame()
    total_alunos = len(nomes)
    #np.random.seed(123)
    #nomes["id_alunos"] = np.random.permutation(total_alunos) + 1
    
    # Incluindo o ID dos alunos
    def incluindo_id_dos_alunos(self):
        np.random.seed(123)
        self.nomes["id_alunos"] = np.random.permutation(self.total_alunos) + 1
        return self.nomes
    

    def criando_dominios(self):
        dominios = ['@dominiodoemail.com.br', '@servicodoemail.com']
        self.nomes['dominio'] = np.random.choice(dominios, self.total_alunos)
        self.nomes['email'] = self.nomes.nome.str.cat(self.nomes.dominio).str.lower()
        return self.nomes


'''data_nomes = Data_frame_alunos()

print('Data Frame Feminino')
print(f'Quantidade de Nomes Femininos: {len(data_nomes.feminino)}')
print(data_nomes.feminino.sample(5))
print('##' * 40)
print('Data Frame Masculino')
print(f'Quantidade de Nomes Masculinos: {len(data_nomes.masculino)}')
print(data_nomes.masculino.sample(5))
print('##' * 40)
print('Junção dos Frames: Masculino e Feminino')
print(f'Quantidade de Nomes: {data_nomes.qtd_nomes()}')
print(data_nomes.nomes.sample(5))
print('##' * 40)
print(data_nomes.incluindo_id_dos_alunos())
print('##' * 40)
print(data_nomes.criando_dominios())'''
