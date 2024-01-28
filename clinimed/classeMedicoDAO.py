import ClasseConexaoBD as conexao
from IPython.core.display_functions import display
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


class MedicoDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def cadastrarMedico(self,medico):
        try:
            cursor = self.conexao.conexao.cursor()
            sql = "INSERT INTO medicos (cpf, nome, crm, especi_Medica, Data_de_Admissao, rg, Data_de_Demissao, " \
                  "statusMedico) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"

            valores = medico.cpfMedico, medico.nomeMedico, medico.crm, medico.especi_Medica, medico.Data_de_Admissao, medico.rg, medico.Data_de_Demissao, medico.statusMedico

            cursor.execute(sql, valores)
            self.conexao.conexao.commit()
            print("Medico Cadastrado com Sucesso!")

        except Exception as erro:
            print("Erro:",erro)


    def editarMedico(self, crmProcurado, conexao):
        cursor = self.conexao.conexao.cursor()
        sql = "SELECT crm FROM medicos WHERE crm = '{}'".format(crmProcurado)

        cursor.execute(sql)
        resultado = cursor.fetchall()

        if len(resultado) == 0:
            print("Registro não encontrado")

        else:
            cpfMedico = input("CPF: ")
            nomeMedico = input("Nome:")
            crm = input("crm: ")
            especi_Medica = input("Especialidade médica: ")
            Data_de_Admissao = input("Data de admissão: ")
            rg = input("RG: ")
            Data_de_Demissao = input("Data de Demissão: ")

            if not Data_de_Demissao:
                statusMedico = "Ativo"

            else:
                statusMedico = "Inativo"

            sql = "UPDATE medicos SET cpf = %s, nome = %s, crm = %s, especi_Medica = %s, Data_de_Admissao = %s, RG = " \
                  "%s, Data_de_Demissao = %s, statusMedico = %s WHERE crm = %s"

            valores = (cpfMedico, nomeMedico, crm, especi_Medica, Data_de_Admissao, rg, Data_de_Demissao,
                       statusMedico, crmProcurado)

            try:
                cursor.execute(sql, valores)
                conexao.conexao.commit()
                print(cursor.rowcount, "registro alterado")

            except Exception as erro:
                print("Erro: ", erro)

    def consultarMedico(self, crmProcurado):
        cursor = self.conexao.conexao.cursor()
        sql = "SELECT CPF, nome, crm, especi_Medica, Data_de_Admissao, rg, Data_de_Demissao, statusMedico " \
              "FROM medicos WHERE crm = '{}'".format(crmProcurado)

        cursor.execute(sql)
        resultado = cursor.fetchall()

        if len(resultado) == 0:
            print("Registro não encontrado!")

        else:
            resultados = []

            for result in resultado:
                result = list(result)
                resultados.append(result)

            colunas = ['cpf', 'nome', ' crm', 'especi_Medica', 'Data_de_Admissao', 'rg', 'Data_de_Demissao', 'statusMedico']
            tabela = pd.DataFrame(resultados, columns=colunas).to_string(index=False)
            display(tabela)

    def excluirMedico(self, crmProcurado, conexao):
        cursor = self.conexao.conexao.cursor()
        sql = "SELECT cpf, nome, crm, especi_Medica, Data_de_Admissao, rg, Data_de_Demissao, statusMedico FROM " \
              "medicos WHERE crm = '{}'".format(crmProcurado)

        cursor.execute(sql)
        resultado = cursor.fetchall()

        if len(resultado) == 0:
            print("Registro não encontrado!")

        else:
            resultados = []

            for result in resultado:
                result = list(result)
                resultados.append(result)

            colunas = ['cpf', 'nome', ' crm', 'especi_Medica', 'Data_de_Admissao', 'rg', 'Data_de_Demissao', 'statusMedico']
            tabela = pd.DataFrame(resultados, columns=colunas).to_string(index=False)
            display(tabela)

            print("\nDeseja excluir o registro acima?\n1- Sim ou 2- Não")
            opDesejada = int(input("Digite uma opção: "))

            if opDesejada == 1:
                sql = "DELETE FROM medicos WHERE crm = '{}'".format(crmProcurado)

                try:
                    cursor.execute(sql)
                    conexao.conexao.commit()
                    print(cursor.rowcount, "registro excluído")

                except Exception as erro:
                    print("Erro: ", erro)

            elif opDesejada == 2:
                print("Registro não excluído.")
                # VOLTAR AO MENU PRINCIPAL

            else:
                print("Opção inválida!")
