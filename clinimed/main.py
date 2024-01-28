import time

import pyautogui as pyautogui

import ClasseConexaoBD as conexao
import classePaciente as paciente
import classePacienteDAO as pacienteDAO
import classeMedico as medico
import classeMedicoDAO as medicoDAO
import classeConsulta
import classeConsultaDAO

if __name__ == "__main__":
    conexao = conexao.ConexaoBanco(host="localhost",
                                   user="root",
                                   password="",
                                   database="clinimed")

    conexao.conectar()

    print("**** CLINIMED ****")
    print("\n1. Área de Pacientes|\n2. Área de Médicos\n3. Consultas")
    opMenuPrincipal = int(input("Escolha uma opção:"))

    if opMenuPrincipal == 1:
        print("**Área de Pacientes **")
        print("1. Cadastrar\n2. Editar\n3. Consultar cadastro\n4. Excluir Cadastro")
        opMenu = int(input("\nEscolha uma opção: "))

        match opMenu:
            case 1:
                cursor = conexao.conexao.cursor()
                print("**Cadastro De Pacientes **")
                cpfPaciente = input("\nCPF:")

                sql = "SELECT CPF FROM PESSOA WHERE CPF = '{}'".format(cpfPaciente)

                cursor.execute(sql)
                resultado = cursor.fetchall()

                if len(resultado) != 0:
                    print("Registro já cadastrado!")
                    time.sleep(3)

                else:
                    nomePaciente = input("Nome:")
                    enderecoPaciente = input("Endereço:")
                    cepPaciente = input("CEP:")
                    TelResidPaciente = input("Tel. Residencial:")
                    celularPaciente = input("Celular:")
                    dtNascPaciente = input("Data de Nascimento (YYYY-MM--DD:")
                    rgPaciente = input("RG:")
                    sexoPaciente = input("Sexo (M ou F):")

                    novoPaciente = paciente.Paciente(cpfPaciente=cpfPaciente, nomePaciente=nomePaciente,
                                                     enderecoPaciente=enderecoPaciente, cepPaciente=cepPaciente,
                                                     TelResidPaciente=TelResidPaciente, celularPaciente=celularPaciente,
                                                     dtNascPaciente=dtNascPaciente, rgPaciente=rgPaciente,
                                                     sexoPaciente=sexoPaciente)

                    pacienteDAO = pacienteDAO.PacienteDAO(conexao)
                    pacienteDAO.cadastrarPaciente(novoPaciente)

            case 2:
                # pyautogui.hotkey('ctrl', 'l')
                print("** Alteração de Pacientes **")
                cpfProcurado = input("\nDigite o CPF do paciente:")
                # pyautogui.hotkey('ctrl', 'l')
                pacienteDAO = pacienteDAO.PacienteDAO(conexao)
                pacienteDAO.editarPaciente(cpfProcurado, conexao)

            case 3:
                # pyautogui.hotkey('ctrl', 'l')
                print("** Consulta de Paciente **")
                cpfProcurado = input("\nDigite o CPF do paciente:")
                # pyautogui.hotkey('ctrl', 'l')
                pacienteDAO = pacienteDAO.PacienteDAO(conexao)
                pacienteDAO.consultarPaciente(cpfProcurado)

            case 4:

                print("** Excluir Paciente **")
                cpfProcurado = input("\nDigite o CPF do paciente:")
                pacienteDAO = pacienteDAO.PacienteDAO(conexao)
                pacienteDAO.excluirPaciente(cpfProcurado, conexao)

    elif opMenuPrincipal == 2:
        print("** ÁREA DE MÉDICOS**")
        print("1.Cadastrar\n2.Editar cadastro\n3.Consultar Cadastro\n4.Excluir Cadastro")
        opMenu = int(input("\nEscolha uma opção: "))

        match opMenu:
            case 1:

                cursor = conexao.conexao.cursor()

                print("**Cadastro De Médicos  **")
                crm = input("\nCRM:")
                sql = "SELECT CRM FROM MEDICOS WHERE CRM = '{}'".format(crm)
                cursor.execute(sql)
                resultado = cursor.fetchall()

                if len(resultado) != 0:
                    print("Registro já cadastrado!")
                    time.sleep(3)

                else:
                    nomeMedico = input("Nome:")
                    cpfMedico = input("\nCPF:")
                    especi_Medica = input("Especialidade Médica:")
                    Data_de_Admissao = input("Data de Admissão:")
                    rg = input("RG Médico:")
                    Data_de_Demissao = input("Data de Demissao :")

                    if not Data_de_Demissao:
                        statusMedico = "Ativo"


                    else:
                        statusMedico = "Inativo"

                    novoMedico = medico.Medico(cpfMedico=cpfMedico, nomeMedico=nomeMedico,
                                               crm=crm, especi_Medica=especi_Medica,
                                               Data_de_Admissao=Data_de_Admissao, rg=rg,
                                               Data_de_Demissao=Data_de_Demissao, statusMedico=statusMedico)

                    medicoDAO = medicoDAO.MedicoDAO(conexao)
                    medicoDAO.cadastrarMedico(novoMedico)

            case 2:
                print("**Editar Cadastro Médico**")
                crmProcurado = input("\nDigite o CRM do Médico:")
                medicoDAO = medicoDAO.MedicoDAO(conexao)
                medicoDAO.editarMedico(crmProcurado, conexao)

            case 3:
                print("** Consulta de Medico **")
                crmProcurado = input("\nDigite o CRM do Medico:")
                medicoDAO = medicoDAO.MedicoDAO(conexao)
                medicoDAO.consultarMedico(crmProcurado)

            case 4:
                print("** Excluir Médico **")
                crmProcurado = input("\nDigite o CRM do Médico:")
                medicoDAO = medicoDAO.MedicoDAO(conexao)
                medicoDAO.excluirMedico(crmProcurado, conexao)

    elif opMenuPrincipal == 3:
        print("** ÁREA DE CONSULTAS **")
        print("1. Marcar Consulta\n2. Editar Consulta\n3. Visualizar Consulta Marcada\n4. Desmarcar Consulta")
        opMenu = int(input("\nEscolha uma Opção: "))

        match opMenu:

            case 1:
                cursor = conexao.conexao.cursor()
                print("** Cadastro de Consultas **")
                crmMedico = input("\nCRM: ")
                sql = "SELECT id FROM medicos WHERE CRM = %s"
                cursor.execute(sql, (crmMedico,))
                resultado = cursor.fetchall()

                if len(resultado) == 0:
                    print("Médico não Encontrado!")
                    time.sleep(3)


                else:
                    idMedico = resultado[0][0]
                    cpfPaciente = input("CPF do Paciente: ")
                    sql = "SELECT id FROM pessoa WHERE cpf = %s"
                    cursor.execute(sql, (cpfPaciente,))
                    resultado = cursor.fetchall()

                    if len(resultado) == 0:
                        print("Paciente não Encontrado!")
                        time.sleep(3)


                    # implementar lógica para validar se médico está com status = Ativo

                    else:

                        idPaciente = resultado[0][0]
                        codConsulta = input("Código da Consulta: ")
                        dtConsulta = input("Data da Consulta (YYYY-MM-DD): ")
                        hrConsulta = input("Hora da Consulta (HH:MM:SS): ")
                        novaConsulta = classeConsulta.Consulta(idPaciente=idPaciente, idMedico=idMedico,
                                                               codConsulta=codConsulta, dtConsulta=dtConsulta,
                                                               hrConsulta=hrConsulta)

                        consultaDAO_instancia = classeConsultaDAO.ConsultaDAO(conexao)
                        consultaDAO_instancia.cadastrarConsulta(novaConsulta)
            case 2:
                pass


            case 3:
                pyautogui.hotkey('ctrl','l')
                print("** Visualização de Consultas **")

                opconsulta = int(input("\n1. Consultar por código\n2. Consultar por Médico\n3. Consultar por "
                                       "Paciente\n4. Listar todas as Consultas\n0. Voltar\n\nEscolha uma opção:"))

                if opconsulta ==1:
                    codConsulta = input("\nDigite o código da Consulta: ")
                    consultaDAO_instancia = classeConsultaDAO.ConsultaDAO(conexao)
                    consultaDAO_instancia.consultarPorCodigo(codConsulta)

                elif opconsulta == 2:
                     crmProcurado = input("\nDigite o CRM do médico: ")
                     consultaDAO_instancia = classeConsultaDAO.ConsultaDAO(conexao)
                     consultaDAO_instancia.consultarPorMedico(crmProcurado)

                elif opconsulta == 3:
                     cpfProcurado = input("\nDigite o CPF do Paciente: ")
                     consultaDAO_instancia = classeConsultaDAO.ConsultaDAO(conexao)
                     consultaDAO_instancia.consultarPorPaciente(cpfProcurado)

                elif opconsulta == 4:
                     consultaDAO_instancia = classeConsultaDAO.ConsultaDAO(conexao)
                     consultaDAO_instancia.visualizarTodasConsultas()

                elif opconsulta == 0:
                     pass

                else:
                    print("Opção Inválida!\n\nRetornando ao Menu Principal...")
                    time.sleep(3)

            case 4:
                print("** Desmarcar Consultas **")
                codConsulta = input("\n\nDigite o código da consulta: ")
                consultaDAO_instancia = classeConsultaDAO.ConsultaDAO(conexao)
                consultaDAO_instancia.excluirConsulta(codConsulta, conexao)