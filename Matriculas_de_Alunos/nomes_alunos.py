import pandas as pd

class Nomes_alunos:

    def __init__(self, nome_feminino, nome_masculino):
        self.nome_feminino = nome_feminino
        self.nome_masculino = nome_masculino

    def set_nome_feminino(self, nome_feminino):
        self.nome_feminino = nome_feminino

    def get_nome_feminino(self):
        return self.nome_feminino

    def set_nome_maticalino(self, nome_masculino):
        self.nome_masculino = nome_masculino

    def get_nome_masculino(self):
        return self.nome_masculino



