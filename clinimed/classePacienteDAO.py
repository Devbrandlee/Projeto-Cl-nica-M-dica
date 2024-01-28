from IPython.core.display_functions import display
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


class PacienteDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def cadastrarPaciente(self, paciente):
        try:
            cursor = self.conexao.conexao.cursor()
            sql = "INSERT INTO pessoa (cpf, nome, endereco, cep, celular, data_de_nascimento, rg, telefone, sexo) VALUES " \
                  "(%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            valores = paciente.cpfPaciente, paciente.nomePaciente, paciente.enderecoPaciente, paciente.cepPaciente, \
                paciente.celularPaciente, paciente.dtNascPaciente, paciente.rgPaciente, paciente.TelResidPaciente, \
                paciente.sexoPaciente

            cursor.execute(sql, valores)
            self.conexao.conexao.commit()
            print("Paciente Cadastrado com Sucesso!")

        except Exception as erro:
            print("Erro:", erro)

    def editarPaciente(self, cpfProcurado, conexao):
        cursor = self.conexao.conexao.cursor()
        sql = "SELECT cpf FROM pessoa WHERE cpf = '{}'".format(cpfProcurado)

        cursor.execute(sql)
        resultado = cursor.fetchall()

        if len(resultado) == 0:
            print("Registro não encontrado")

        else:
            cpfPessoa = input("CPF: ")
            nomePessoa = input("Nome:")
            enderecoPessoa = input("Endereço: ")
            cepPessoa = input("CEP: ")
            telResidPessoa = input("Tel Residencial: ")
            celularPessoa = input("Celular: ")
            dtNascPessoa = input("Dt Nascimento: ")
            rgPessoa = input("RG: ")
            sexoPessoa = input("Sexo: ")

            sql = "UPDATE pessoa SET cpf = %s, nome = %s, endereco = %s, cep = %s, celular = %s, data_de_nascimento = " \
                  "%s, rg = %s, telefone = %s, sexo = %s WHERE cpf = %s"

            valores = (cpfPessoa, nomePessoa, enderecoPessoa, cepPessoa, telResidPessoa, celularPessoa, dtNascPessoa,
                       rgPessoa, sexoPessoa, cpfProcurado)

            try:
                cursor.execute(sql, valores)
                conexao.conexao.commit()
                print(cursor.rowcount, "registro alterado")

            except Exception as erro:
                print("Erro: ", erro)

    def consultarPaciente(self, cpfProcurado):
        cursor = self.conexao.conexao.cursor()
        sql = "SELECT cpf, nome, endereco, cep, celular, data_de_nascimento, rg, telefone, sexo FROM pessoa WHERE CPF " \
              "= '{}'".format(cpfProcurado)

        cursor.execute(sql)
        resultado = cursor.fetchall()

        if len(resultado) == 0:
            print("Registro não encontrado!")

        else:
            resultados = []

            for result in resultado:
                result = list(result)
                resultados.append(result)

            colunas = ['cpf', 'nome', ' endereco', 'cep', 'celular', 'data_de_nascimento', 'rg', 'telefone', 'sexo']
            tabela = pd.DataFrame(resultados, columns=colunas).to_string(index=False)
            display(tabela)

    def excluirPaciente(self, cpfProcurado, conexao):
        cursor = self.conexao.conexao.cursor()
        sql = "SELECT cpf, nome, endereco, cep, celular, data_de_nascimento, rg, telefone, sexo FROM pessoa WHERE CPF " \
              "= '{}'".format(cpfProcurado)

        cursor.execute(sql)
        resultado = cursor.fetchall()

        if len(resultado) == 0:
            print("Registro não encontrado!")

        else:
            resultados = []

            for result in resultado:
                result = list(result)
                resultados.append(result)

            colunas = ['cpf', 'nome', ' endereco', 'cep', 'celular', 'data_de_nascimento', 'rg', 'telefone', 'sexo']
            tabela = pd.DataFrame(resultados, columns=colunas).to_string(index=False)
            display(tabela)

            print("\nDeseja excluir o registro acima?\n1- Sim ou 2- Não")
            opDesejada = int(input("Digite uma opção: "))

            if opDesejada == 1:
                sql = "DELETE FROM pessoa WHERE cpf = '{}'".format(cpfProcurado)

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
