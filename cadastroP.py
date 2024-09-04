import os
import time

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
            print("Resposta inválida. Por favor, digite 'SIM/NÃO ou S/N.")

def menu_opcoes(pergunta, opcoes):# função criada para exibir as opções das perguntas para o usuário
    os.system("cls")  # Limpa o terminal após cada execução

    while True:
        os.system("cls")
        print(pergunta)  # Exibe a pergunta para o usuário
        print("Escolha uma ou mais opções:")

        for i, opcao in enumerate(opcoes):
            print(f"{i + 1}. {opcao}")  # imprimi cada opção dos números começando do 1

        escolhas = input("Digite o número da(s) opção(ões) separadas por vírgula: ")

        # Converte as escolhas em índices, subtraindo 1 para ajustar ao índice da lista
        escolhas = [int(x) - 1 for x in escolhas.split(",")]

        # Verifica se todas as escolhas estão dentro do intervalo válido
        if all(0 <= i < len(opcoes) for i in escolhas):
            break  # Sai do loop se todas as escolhas forem válidas
        else:
            print("\n\nErro!!! Opção inválida. Tente novamente.")
            time.sleep(2)

     # Gera a lista das opções escolhidas
     # Converte as escolhas em índices, subtraindo 1 para ajustar ao índice da lista
     #Ou seja, toda lista em python ela começa no índice 0
    opcoes_escolhidas = [opcoes[i] for i in escolhas]
    print("Opções escolhida(s):", opcoes_escolhidas)
    return opcoes_escolhidas



def menu_perguntas_int(pergunta):
    os.system("cls")
    while True:
        try:  # try converte a reposta do usuário para um número inteiro
            resposta = int(input(pergunta))
            return resposta
        except ValueError:  # se o usuário digitar um caractere que esteja fora do esperado, 
            #o programa apresenta um erro e retorna a pergunta
            print(
                "Resposta inválida. Por favor, insira um número inteiro.")


def menu_perguntas_float(pergunta):
    os.system("cls")
    while True:
        try:
            resposta = float(input(pergunta))
            return resposta
        except ValueError:
            print(
                "Resposta inválida. Por favor, insira um número inteiro ou decimal ('2' ou '2.5').")


# Bloco de perguntas--------------------------------------------------------------------------------------------------------------------
estuda = "Você estuda atualmente em alguma instituíção de ensíno? Responda com 'SIM/NÃO ou S/N:"
reprovou = "Você já reprovou algum ano do ensino médio? Responda com 'SIM/NÃO:"
responda = "De acordo com as suas respostas, responda:"
opcoes1 = ["Reprovou por falta;", "Abandonou os estudos;",
           "Problemas pessoais;", "Precisou trabalhar;", "Ajudar os pais."]
estuda_casa = "Você costuma estudar em casa? Responda com 'SIM/NÃO ou S/N:"
tempo_seg = "Quanto tempo livre você tem na SEGUNDA:"
tempo_ter = "Quanto tempo livre você tem na TERÇA:"
tempo_quar = "Quanto tempo livre você tem na QUARTA:"
tempo_quin = "Quanto tempo livre você tem na QUINTA:"
tempo_sex = "Quanto tempo livre você tem na SEXTA:"
tempo_sab = "Quanto tempo livre você tem no SÁBADO:"
tempo_dom = "Quanto tempo livre você tem no DOMINGO:"
media_port = "Informe a média de língua PORTUGUESA:"
media_mat = "Informe a média de MATEMÁTICA:"
media_hist = "Informe a média de HISTÓRIA:"
media_bio = "Informe a média de BIOLOGIA:"
media_filo = "Informe a média de FILOSOFIA:"
media_qui = "Informe a média de QUÍMICA:"
media_arte = "Informe a média de ARTE:"
media_geo = "Informe a média de GEOGRAFIA:"
media_ing = "Informe a média de INGLÊS:"
dispositivo = "Você possui algum dispositivo?(Smartphone, Tablet ou Computador)"
opcoes3 = ["Smartphone;", "Tablet;", "Computador;",
           "Todas as opções.", "Nenhum dispositivo"]
compartilha_disp = "Você compartilha este dispositivo com alguém? SE SIM, responda com a quantidade de pessoas, SENÃO digite 0:"
internet = "Tem acesso a internet? Responda com 'SIM/NÃO ou S/N:"
opcoes5 = ["Financeiro;", "Localização;",
           "Não possui dispositivo com acesso a internet."]
tipo_inter = "Qual é o tipo de sua internet?"
opcoes2 = ["Dados móveis;", "Internet residencial;",
           "Dados móveis e internet residencial."]
responda2 = "De acordo com a sua resposta, responda:"
opcoes4 = ["Abandonou os estudos;", "Problemas pessoais;",
           "Você precisou trabalhar;", "Ajuda os pais."]
estudou_antes = "Você já estudou antes? Responda com 'SIM/NÃO:"
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

    with open('respostas_media_exa.txt', 'w') as exatas:
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

    with open('respostas_media_huma.txt', 'w') as humanas:  # 'w' para sobrescrever
        for resposta in respostas:
            humanas.write(resposta + '\n')

    print("Respostas armazenadas com sucesso!")


# ------------------------------------------------------------------------------------

def dias_semana():
    os.system("cls")
    respostas = []
    resposta4 = menu_perguntas_float(tempo_seg)
    print("Sua resposta:", resposta4)
    respostas.append(f"Tempo de estudo na segunda: {resposta4}")
    print("")

    resposta5 = menu_perguntas_float(tempo_ter)
    print("Sua resposta:", resposta5)
    respostas.append(f"Tempo de estudo na terça: {resposta5}")
    print("")

    resposta6 = menu_perguntas_float(tempo_quar)
    print("Sua resposta:", resposta6)
    respostas.append(f"Tempo de estudo na quarta: {resposta6}")
    print("")

    resposta7 = menu_perguntas_float(tempo_quin)
    print("Sua resposta:", resposta7)
    respostas.append(f"Tempo de estudo na quinta: {resposta7}")
    print("")

    resposta8 = menu_perguntas_float(tempo_sex)
    print("Sua resposta:", resposta8)
    respostas.append(f"Tempo de estudo na sexta: {resposta8}")
    print("")

    resposta9 = menu_perguntas_float(tempo_sab)
    print("Sua resposta:", resposta9)
    respostas.append(f"Tempo de estudo no sábado: {resposta9}")
    print("")

    resposta10 = menu_perguntas_float(tempo_dom)
    print("Sua resposta:", resposta10)
    respostas.append(f"Tempo de estudo no domingo: {resposta10}")
    print("")

    # Salvar as respostas em um arquivo de texto
    with open('respostas_dias_semana.txt', 'w') as semana_dias:  # 'w' para sobrescrever
        for resposta in respostas:
            semana_dias.write(resposta + '\n')


print("Respostas armazenadas com sucesso!")
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
                        dias_semana()

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
                        dias_semana()
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
                        dias_semana()
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
