import os
import time
import datetime
import codecs

respostas = {
    'sim': True,
    'não': False,
    's': True,
    'n': False,
    'nao': False
}


def menu_perguntas(pergunta):  # função para as perguntas
    os.system("cls")
    while True:
        print(pergunta)
        resposta = input("Digite sua resposta: ").strip().lower()

        if resposta in respostas:

            return respostas[resposta]
        else:
            print("Resposta inválida. Por favor, digite 'SIM/NÃO ou S/N':")


def menu_opcoes(pergunta, opcoes):

    os.system("cls")
    while True:
        print(pergunta)
        for i, opcao in enumerate(opcoes, start=1):
            print(f"{i}. {opcao}")

        escolha = input("Digite o número da opção: ")
        try:
            escolha = int(escolha)
            if 1 <= escolha <= len(opcoes):
                return opcoes[escolha - 1]
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")


def menu_perguntas_int(pergunta):
    os.system("cls")
    while True:
        try:  # try converte a reposta do usuário para um número inteiro
            resposta = int(input(pergunta))
            return resposta
        except ValueError:  # se o usuário digitar um caractere que esteja fora do esperado,
            # o programa apresenta um erro e retorna a pergunta
            print(
                "Resposta inválida. Por favor, insira um número INTEIRO(ex:'2').")


def menu_perguntas_float(pergunta):
    os.system("cls")
    while True:
        try:
            resposta = float(input(pergunta))
            return resposta
        except ValueError:
            print(
                "Resposta inválida. Por favor, insira um número INTEIRO ou DECIMAL (ex:'2' ou '2.5').")


def converter_hora():
    while True:
        hora = input("Digite a hora no formato HH:MM: ")

        try:
            datetime.datetime.strptime(hora, '%H:%M')
            break
        except ValueError:
            print("Formato de hora inválido. Use HH:MM.")


# Bloco de perguntas--------------------------------------------------------------------------------------------------------------------
estuda = "Você estuda atualmente em alguma instituíção de ensíno? Responda com 'SIM/NÃO ou S/N':"
reprovou = "Você já reprovou algum ano do ensino médio? Responda com 'SIM/NÃO ou S/N':"
responda = "De acordo com as suas respostas, responda:"
opcoes1 = ["Reprovou por falta;", "Abandonou os estudos;",
           "Problemas pessoais;", "Precisou trabalhar;", "Ajudar os pais."]
estuda_casa = "Você costuma estudar em casa? Responda com 'SIM/NÃO ou S/N':"
media_port = "Informe a média de língua PORTUGUESA:"
media_mat = "Informe a média de MATEMÁTICA (ex: '8.5' ou '8'):"
media_hist = "Informe a média de HISTÓRIA (ex: '8.5' ou '8'):"
media_bio = "Informe a média de BIOLOGIA (ex: '8.5' ou '8'):"
media_filo = "Informe a média de FILOSOFIA (ex: '8.5' ou '8'):"
media_qui = "Informe a média de QUÍMICA (ex: '8.5' ou '8'):"
media_arte = "Informe a média de ARTE (ex: '8.5' ou '8'):"
media_geo = "Informe a média de GEOGRAFIA (ex: '8.5' ou '8'):"
media_ing = "Informe a média de INGLÊS (ex: '8.5' ou '8'):"
dispositivo = "Você possui algum dispositivo?(Smartphone, Tablet ou Computador)"
opcoes3 = ["Smartphone;", "Tablet;", "Computador;",
           "Todas as opções.", "Nenhum dispositivo"]
compartilha_disp = "Você compartilha este dispositivo com alguém? SE SIM, responda com a quantidade de pessoas, SENÃO digite 0:"
internet = "Tem acesso a internet? Responda com 'SIM/NÃO ou S/N':"
opcoes5 = ["Financeiro;", "Localização;",
           "Não possui dispositivo com acesso a internet."]
tipo_inter = "Qual é o tipo de sua internet?"
opcoes2 = ["Dados móveis;", "Internet residencial;",
           "Dados móveis e internet residencial."]
responda2 = "De acordo com a sua resposta, responda:"
opcoes4 = ["Abandonou os estudos;", "Problemas pessoais;",
           "Você precisou trabalhar;", "Ajuda os pais."]
estudou_antes = "Você já estudou antes? Responda com 'SIM/NÃO ou S/N':"
opcoes6 = ["Não sabe como organizar os estudos;", "Não conhece nenhuma plataforma online de estudos;",
           "Não tem costume de organizar os estudos;", "Não gosta."]

# ----------------------------------------------------------------------------------------------------------------------------------------------------


def media_disciplinas_exa():
    os.system("cls")
    respostas = []
    print("Informe a média de suas disciplinas de EXATAS:")
    resposta12 = menu_perguntas_float(media_mat)
    respostas.append(f"Média de matemática: {resposta12}")
    print("Sua resposta:", resposta12)
    print("")

    resposta14 = menu_perguntas_float(media_bio)
    print("Sua resposta:", resposta14)
    respostas.append(f"Média de biologia: {resposta14}")
    print("")

    resposta16 = menu_perguntas_float(media_qui)
    print("Sua resposta:", resposta16)
    respostas.append(f"Média de química: {resposta16}")
    print("")

    resposta18 = menu_perguntas_float(media_geo)
    print("Sua resposta:", resposta18)
    respostas.append(f"Média de geografia: {resposta18}")
    print("")

    with codecs.open('respostas_media_exa.txt', 'w', 'utf-8') as exatas:
        for resposta in respostas:
            exatas.write(resposta + '\n')

    print("Respostas armazenadas com sucesso!")


# -----------------------------------------------------------------------------------


def media_disciplinas_huma():
    os.system("cls")
    respostas = []
    print("Informe a média de suas disciplinas de HUMANAS:")
    resposta11 = menu_perguntas_float(media_port)
    print("Sua resposta:", resposta11)
    respostas.append(f"Média de português: {resposta11}")
    print("")

    resposta13 = menu_perguntas_float(media_hist)
    print("Sua resposta:", resposta13)
    respostas.append(f"Média de história: {resposta13}")
    print("")

    resposta15 = menu_perguntas_float(media_filo)
    print("Sua resposta:", resposta15)
    respostas.append(f"Média de filosofia: {resposta15}")
    print("")

    resposta17 = menu_perguntas_float(media_arte)
    print("Sua resposta:", resposta17)
    respostas.append(f"Média de artes: {resposta17}")
    print("")

    resposta19 = menu_perguntas_float(media_ing)
    print("Sua resposta:", resposta19)
    respostas.append(f"Média de inglês: {resposta19}")
    print("")

    with codecs.open('respostas_media_huma.txt', 'w', 'utf-8') as humanas:  # 'w' para sobrescrever
        for resposta in respostas:
            humanas.write(resposta + '\n')

    print("Respostas armazenadas com sucesso!")


# ------------------------------------------------------------------------------------

def registrar_horarios():
    os.system("cls")  

    horarios = {}
    dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']

    for dia in dias_semana:
        while True:
            horario = input(f"Quanto tempo livre você tem no(a) {dia} (HH:MM): ")
            try:
                hora, minuto = map(int, horario.split(':'))
                if 0 <= hora <= 23 and 0 <= minuto <= 59:
                    break
                else:
                    print("Hora ou minuto inválido.")
            except ValueError:
                print("Formato de hora inválido. Use HH:MM.")

        horarios[dia] = f"{hora:02d}:{minuto:02d}" 

    with open('respostas_dias_semana.txt', 'w', encoding='utf-8') as arquivo:
        for dia, horario in horarios.items():
            arquivo.write(f"{dia}: {horario}\n")

# --------------------------------------------------------------------
while True:
    resposta = menu_perguntas(estuda)
    print("Sua resposta:", resposta)
    print("")

    if (resposta == True):  # No laço de decisão são chamadas as funções com as perguntas e respostas

        resposta1 = menu_perguntas(reprovou)
        print("Sua resposta:", resposta1)
        print("")

        while True:
            if (resposta1 == True):  # VOCE REPROVOU
                menu_opcoes(responda, opcoes1)
                print("")
                resposta3 = menu_perguntas(estuda_casa)
                print("Sua resposta:", resposta3)
                print("")

                while True:
                    if (resposta3 == True):
                        registrar_horarios()
                        media_disciplinas_exa()

                        media_disciplinas_huma()
                        menu_opcoes(dispositivo, opcoes3)
                        print("")

                        resposta21 = menu_perguntas_int(compartilha_disp)
                        print("Sua resposta:", resposta21)
                        print("")

                        resposta22 = menu_perguntas(internet)
                        print("Sua resposta:", resposta22)
                        print("")

                        while True:
                            if (resposta22 == True):
                                menu_opcoes(tipo_inter, opcoes2)
                                print("")
                                print(
                                    "Perfil criado com sucesso! Faça o seu login.")
                                import main
                                break
                            else:
                                menu_opcoes(responda, opcoes5)
                                print("")
                                print(
                                    "Perfil criado com sucesso! Faça o seu login.")
                                import main
                                break
                    else:
                        menu_opcoes(responda, opcoes6)
                        print("")
                        print(
                            "Perfil criado com sucesso! Faça o seu login.")
                        import main
                    break

            else:
                resposta3 = menu_perguntas(estuda_casa)
                print("Sua resposta:", resposta3)
                print("")

                while True:
                    if (resposta3 == True):
                        registrar_horarios()
                        media_disciplinas_exa()
                        media_disciplinas_huma()
                        menu_opcoes(dispositivo, opcoes3)
                        print("")
                        resposta21 = menu_perguntas_int(compartilha_disp)
                        print("Sua resposta:", resposta21)
                        print("")
                        resposta22 = menu_perguntas(internet)
                        print("Sua resposta:", resposta22)
                        print("")

                        while True:
                            if (resposta22 == True):
                                menu_opcoes(tipo_inter, opcoes2)
                                print("")
                                print(
                                    "Perfil criado com sucesso! Faça o seu login.")
                                import main
                                break
                            else:
                                menu_opcoes(responda, opcoes5)
                                print("")
                                print(
                                    "Perfil criado com sucesso! Faça o seu login.")
                                import main
                                break
                    else:
                        menu_opcoes(responda, opcoes6)
                        print("")
                        print(
                            "Perfil criado com sucesso! Faça o seu login.")
                        import main
                    break

    else:
        menu_opcoes(responda2, opcoes4)
        print("")
        resposta25 = menu_perguntas(estudou_antes)
        print("Sua resposta:", resposta25)
        print("")

        while True:
            if (resposta25 == True):
                menu_opcoes(responda, opcoes1)
                resposta3 = menu_perguntas(estuda_casa)
                print("Sua resposta:", resposta3)
                print("")

                while True:
                    if (resposta3 == True):
                        registrar_horarios()
                        media_disciplinas_exa()
                        media_disciplinas_huma()
                        menu_opcoes(dispositivo, opcoes3)
                        print("")
                        resposta21 = menu_perguntas_int(compartilha_disp)
                        print("Sua resposta:", resposta21)
                        print("")
                        resposta22 = menu_perguntas(internet)
                        print("Sua resposta:", resposta22)
                        print("")

                        while True:
                            if (resposta22 == True):
                                menu_opcoes(tipo_inter, opcoes2)
                                print("")
                                print(
                                    "Perfil criado com sucesso! Faça o seu login.")
                                import main
                                break
                            else:
                                menu_opcoes(responda, opcoes5)
                                print("")
                                print(
                                    "Perfil criado com sucesso! Faça o seu login.")
                                import main
                                break
                    else:
                        menu_opcoes(responda, opcoes6)
                        print("")
                        print(
                            "Perfil criado com sucesso! Faça o seu login.")
                        import main
                    break
            else:
                print("Perfil criado com sucesso! Faça o seu login.")
                import main
                break
