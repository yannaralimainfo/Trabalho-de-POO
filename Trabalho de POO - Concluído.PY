medicos = [
    {
        "nome": "Eliabe",
        "cpf": "11111111111",
        "rg": "1111111",
        "crm": "1111111",
        "telefone": "(11) 11111-1111",
        "endereco": "Várzea Alegre",
        "sexo": "Masculino",
        "senha": "elifecha123"
    }
]
pacientes = [
    {
        "nome": "Afonso Neto",
        "cpf": "22222222222",
        "rg": "2222222",
        "telefone": "(22) 22222-2222",
        "endereco": "Granjeiro",
        "sexo": "Masculino",
        "convenio": "UNIMED"
    }
]

convenios = [
    {
        "nome": "UNIMED",
        "telefone": "(33) 33333-3333",
        "endereco": "Juazeiro do Norte",
        "cnpj": "333333333333",
        "planos": "Plano KYUA, Plano NNY"
    }
]

consultas = [
    {   
        "mediconome": "Eliabe",
        "pacientenome":"Afonso Neto",
        "data" : "21/06/2024",
        "horainicial" : "16:00",
        "horafinal" : "16:40",
        "descricao" : "Atendimento psiquiatrico"
    }
]

compromissos = [
    {
        "data": "22/06/2024",
        "horainicial": "8:00",
        "mediconome": "Eliabe",
        "pacientenome": "Afonso Neto",
        "horafinal": "11:00",
        "descricao": "Exames"
    }
]



def cadastrarMedicos():
        print("Iniciar cadastro de médico.")
        print("Insira o nome do médico: ")
        nome = input("")
       
        print("Insira o CPF do médico: ")
        cpf = input("")
        
        print("Insira o RG do médico: ")
        rg = input("")

        print("Insira o telefone do médico:")
        telefone = input("")
        
        print("Insira o endereço do médico :")
        endereco = input("")

        print("Insira o sexo do médico: ")
        sexo = input("")
        
        print("Insira o CRM do médico: ")
        crm = input("")
        
        print("Insira uma senha para o médico:")
        senha = input("")
        
        print("Deseja salvar as informações? Digite: (S) para sim e (N) para não.")
        salvar = input("").upper()
        if salvar == "S":
            print("Médico cadastrado com sucesso!")
            medicos.append({
                "nome": nome,
                "cpf": cpf,
                "rg": rg,
                "telefone": telefone,
                "endereco": endereco,
                "sexo": sexo,
                "crm": crm,
                "senha": senha
            })
            print(medicos)
        else:
            print("Operação cancelada!")
            
def buscarMedicos():
    print("Informe o nome ou CRM do médico que deseja buscar:")
    busm = input("")
    resultados = [medico for medico in medicos if busm.lower() == medico.get('nome', '').lower() or busm == medico.get('crm', '')]
    if resultados:
        for resultado in resultados:
            print(f"Nome: {resultado['nome']}, Telefone: {resultado['telefone']}, CRM: {resultado['crm']}")
    else:
        print("Nenhum médico encontrado.")
        
def alterarMedicos():
  
  print("Informe o CRM do médico que deseja alterar:")
  crm = input("")
  medico = next((medico for medico in medicos if medico['crm'] == crm), None)
  if medico:
        print(f"Analise as informações cadastradas do médico: {medico}")
        print("Forneça os novos dados (deixe em branco para manter o valor atual):")
        nome = input(f"Nome ({medico['nome']}): ") or medico['nome']
        cpf = input(f"CPF ({medico['cpf']}): ") or medico['cpf']
        rg = input(f"RG ({medico['rg']}): ") or medico['rg']
        telefone = input(f"Telefone ({medico['telefone']}): ") or medico['telefone']
        endereco = input(f"Endereço ({medico['endereco']}): ") or medico['endereco']
        sexo = input(f"Sexo ({medico['sexo']}): ") or medico['sexo']
        senha = input(f"Senha ({medico['senha']}): ") or medico['senha']
        
        print("Deseja salvar as informações? Digite: (S) para sim e (N) para não.")
        salvar = input("").upper()
        if salvar == "S":
            print("As informações do médico foram alteradas com sucesso!")
            
        medico.update({
            "nome": nome,
            "cpf": cpf,
            "rg": rg,
            "telefone": telefone,
            "endereco": endereco,
            "sexo": sexo,
            "senha": senha
        })
        print(medicos)

def cadastrarPacientes():

    print("Insira o nome do paciente:")
    nome = input()
    
    print("Insira o CPF do paciente:")
    cpf = input()
    
    print("Insira o RG do paciente:")
    rg = input()
    
    print("Insira o telefone do paciente: ")
    telefone = input()

    print("Insira o paciente do paciente: ")
    endereco = input()
    
    print("Insira o sexo do paciente: ")
    sexo = input()

    print("Insira o convenio do paciente: ")
    convenio = input()

    print("Deseja salvar as informações? Digite: S para sim e N para não.")
    salvar = input().upper()
    if salvar == "S":
        print("Paciente cadastrado com sucesso!")
        pacientes.append({
            "nome": nome,
            "cpf": cpf,
            "rg": rg,
            "telefone": telefone,
            "endereco": endereco,
            "sexo": sexo,
            "convenio": convenio
        })
        print(pacientes)
    else:
        print("Operação cancelada!")
        
def buscarPacientes():
    print("Informe o nome ou CPF do paciente que deseja buscar:")
    busp = input("")
    resultados = [paciente for paciente in pacientes if busp.lower() == paciente.get('nome', '').lower() or busp == paciente.get('cpf', '')]
    if resultados:
        for resultado in resultados:
            print(f"Nome: {resultado['nome']}, Telefone: {resultado['telefone']}, CPF: {resultado['cpf']}")
    else:
        print("Nenhum paciente encontrado.")
        
        
def alterarPacientes():

    print("Insira o CPF do paciente que deseja alterar:")
    cpf = input("")
    paciente = next((paciente for paciente in pacientes if paciente['cpf'] == cpf), None)
    if paciente:
        print(f"Dados atuais: {paciente}")
        print("Forneça os novos dados (deixe em branco para manter o valor atual):")
        nome = input(f"Nome ({paciente['nome']}): ") or paciente['nome']
        rg = input(f"RG ({paciente['rg']}): ") or paciente['rg']
        telefone = input(f"Telefone ({paciente['telefone']}): ") or paciente['telefone']
        endereco = input(f"Endereço ({paciente['endereco']}): ") or paciente['endereco']
        sexo = input(f"Sexo ({paciente['sexo']}): ") or paciente['sexo']
        convenio = input(f"Convênio ({paciente['convenio']}): ") or paciente['convenio']
        
        print("Deseja salvar as informações? Digite: (S) para sim e (N) para não.")
        salvar = input("").upper()
        if salvar == "S":
            print("As informações do paciente foram alteradas com sucesso!")
        paciente.update({
            "nome": nome,
            "rg": rg,
            "telefone": telefone,
            "endereco": endereco,
            "sexo": sexo,
            "convenio": convenio
        })
        
    else:
        print("Paciente não encontrado.")
        
        
def cadastrarConvenios():
        print("Insira o nome do convênio:")
        nome = input("")
        
        print("Insira o telefone do convênio:")
        telefone = input("")
        
        print("Insira o endereço do convênio:")
        endereco = input("")
        
        print("Insira o CNPJ do convênio:")
        cnpj = input("")

        print("Insira os planos do convênio:")
        planos = input("")
        
        print("Deseja salvar as informações? Digite: (S) para sim e (N) para não.")
        salvar = input("").upper()
        if salvar == "S":
            print("Convênio cadastrado com sucesso!")
            convenios.append({
                "nome": nome,
                "endereco": endereco,
                "telefone": telefone,
                "cnpj": cnpj,
                "planos": planos
            })
            print(convenios)
        else:
            print("Operação cancelada!")

def buscarConvenios():
    print("Insira o nome ou CNPJ do convênio que deseja buscar:")
    busc = input("")
    resultados = [convenio for convenio in convenios if busc.lower() == convenio.get('nome', '').lower() or busc == convenio.get('cnpj', '')]
    if resultados:
        for resultado in resultados:
            print(f"Nome: {resultado['nome']}, Telefone: {resultado['telefone']}, CNPJ: {resultado['cnpj']}")
    else:
        print("Nenhum convênio encontrado.")
        
def marcarCompromisso():
        mediconome = input("Insira o nome do médico: ")
        medicoencontrado = next((medico for medico in medicos if medico['nome'] == mediconome), None)
        if medicoencontrado:
            pacientenome = input("Informe o nome do paciente: ")
            pacienteencontrado = next((paciente for paciente in pacientes if paciente['nome'] == pacientenome), None)
            if pacienteencontrado:
                data = input("Insira a data do compromisso: ")
                horainicial = input("Insira a hora inicial do compromisso: ")
                horafinal = input("Insira a hora final do compromisso: ")
                descricao = input("Descreva o compromisso com o médico: ")
                
                print("Deseja salvar as informações? Digite: (S) para sim e (N) para não.")
                salvar = input("").upper()
                if salvar == "S":
                   print("Convênio cadastrado com sucesso!")
                consultas.append({
                    "data": data,
                    "horainicial": horainicial,
                    "horafinal": horafinal,
                    "mediconome": mediconome,
                    "pacientenome": pacientenome,
                    "descricao": descricao
                })

                print(f"Analise as informações da consulta agendada: {compromissos[-1]}")
            else:
                print("Paciente não encontrado.")
        else:
            print("Médico não encontrado.")

def marcarConsulta():
        mediconome = input("Insira o nome do médico: ")
        medicoencontrado = next((medico for medico in medicos if medico['nome'] == mediconome), None)
        if medicoencontrado:
            pacientenome = input("Informe o nome do paciente: ")
            pacienteencontrado = next((paciente for paciente in pacientes if paciente['nome'] == pacientenome), None)
            if pacienteencontrado:
                data = input("Insira a data da consulta: ")
                horainicial = input("Insira a hora inicial da consulta: ")
                horafinal = input("Insira a hora final da consulta: ")
                descricao = input("Descreva a consulta: ")
                
                print("Deseja salvar as informações? Digite: (S) para sim e (N) para não.")
                salvar = input("").upper()
                if salvar == "S":
                   print("Consulta cadastrada com sucesso!")
                consultas.append({
                    "data": data,
                    "horainicial": horainicial,
                    "horafinal": horafinal,
                    "mediconome": mediconome,
                    "pacientenome": pacientenome,
                    "descricao": descricao
                })

                print(f"Analise as informações da consulta agendada: {consultas[-1]}")
            else:
                print("Paciente não encontrado.")
        else:
            print("Médico não encontrado.")

def emitirRelatorio():
    print("Qual relatório você deseja emitir?")
    print("1 - Médicos cadastrados")
    print("2 - Pacientes cadastrados")
    print("3 - Convênios")
    print("4 - Consultas")
    print ("5 - Compromissos")
    
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        print("Médicos cadastrados:")
        for medico in medicos:
            print(f"Nome do médico: {medico['nome']}, CPF do médico: {medico['cpf']}, CRM do médico: {medico['crm']}, Telefone do médico: {medico['telefone']}")
            
    elif escolha == "2":
        print("Pacientes cadastrados:")
        for paciente in pacientes:
            print(f"Nome do paciente: {paciente['nome']}, CPF do paciente: {paciente['cpf']}, Telefone do paciente: {paciente['telefone']}")
            
    elif escolha == "3":
        print("Convênios:")
        for convenio in convenios:
            print(f"Nome do convênio: {convenio['nome']}, CNPJ do convênio: {convenio['cnpj']}, Telefone do convênio: {convenio['telefone']}")
            
    elif escolha == "4":
        print("Consultas:")
        for consulta in consultas:
            print(f"Nome do paciente: {consulta['pacientenome']}, Nome do médico: {consulta['mediconome']}, Data da consulta: {consulta['data']},  Hora inicial da consulta: {consulta['horainicial']},  Hora final da consulta: {consulta['horafinal']},  Descrição da consulta: {consulta['descricao']}")
    
    elif escolha == "5":
        print("Compromissos:")
        for compromisso in compromissos:
            print(f"Nome do paciente: {compromisso['pacientenome']}, Nome do médico: {compromisso['mediconome']}, Data do compromisso: {compromisso['data']},  Hora inicial do compromisso: {compromisso['horainicial']},  Hora final do compromisso: {compromisso['horafinal']},  Descrição do compromisso: {compromisso['descricao']}")       
        
a = True
while a:
   
   lang = input("1 - Cadastrar Médico\n"
                "2 - Cadastrar Paciente\n"
                "3 - Cadastrar Convênio\n"
                "4 - Buscar Médicos\n"
                "5 - Buscar Pacientes\n"
                "6 - Buscar Convênios\n"
                "7 - Alterar Medicos\n"
                "8 - Alterar Pacientes\n"
                "9 - Marcar Compromisso\n"
                "10 - Marcar Consulta\n"
                "11 - Emitir Relatorio\n"
                "12 - Encerrar Programa\n"
                "O que você deseja fazer?")
   match lang:
       
    case "1":
        cadastrarMedicos()
        
    case "2":
        cadastrarPacientes()

    case "3": 
        cadastrarConvenios()
        
    case "4":
        buscarMedicos()
        
    case "5":
        buscarPacientes()
        
    case "6":
        buscarConvenios()
      
    case "7":
        alterarMedicos()
        
    case "8":
        alterarPacientes()
        
    case "9":
        marcarCompromisso()
        
    case "10":
        marcarConsulta()
        
    case "11":
        emitirRelatorio()
                    
    case "12":
        a = False
        
    case _:
        print("Escolha uma opção válida")     