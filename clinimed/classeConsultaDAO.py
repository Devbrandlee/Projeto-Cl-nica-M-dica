import mysql.connector
from IPython.core.display_functions import display
import pandas as pd
import time

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

class ConsultaDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def cadastrarConsulta(self, consulta):
        try:
            cursor = self.conexao.conexao.cursor()
            sql = "INSERT INTO consulta (cod_consulta, dt_consulta, hr_consulta, medico_consulta, paciente_consulta) " \
                  "VALUES (%s, %s, %s, %s, %s)"

            valores = consulta.codConsulta, consulta.dtConsulta, consulta.hrConsulta, consulta.idMedico, \
                consulta.idPaciente

            cursor.execute(sql, valores)
            self.conexao.conexao.commit()
            print("Consulta cadastrada com sucesso!")

        except mysql.connector.Error as erro:
            if erro.errno == 1452:
                print("Erro 1452: Violação de Chave Estrangeira!")
                input()

            else:
                print(f"Erro: {erro}")
