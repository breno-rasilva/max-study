import os
import chardet
import time
import statistics
import re
import codecs

# Caminho do arquivo de texto com os horários


def calcular_mediana_horarios(caminho_txt):

    horarios_em_minutos = []

    with open(caminho_txt, "r") as arquivo:
            for linha_num, linha in enumerate(arquivo, start=1):
                linha = linha.strip()
                # Expressão regular mais flexível para permitir diferentes formatos
                match = re.match(r"^\w+:?\s*(\d{1,2}):(\d{2})$", linha)
                if not match:
                    raise ValueError(f"Formato de horário inválido na linha {linha_num}: {linha}")
                hora, minuto = map(int, match.groups())
                horarios_em_minutos.append(hora * 60 + minuto)

                mediana_minutos = statistics.median(horarios_em_minutos)
                horas = mediana_minutos // 60
                minutos = mediana_minutos % 60
                return f"{horas:02d}:{minutos:02d}"

   

# Exemplo de uso
caminho_do_arquivo = r"C:\\Users\\breno\\OneDrive\\Documentos\\PROJETOS 1° PERIODO\\APP AULA atualizado\\respostas_dias_semana.txt"
mediana = calcular_mediana_horarios(caminho_do_arquivo)
print("\nDe acordo com sua resposta no cadastro, obteve-se o seguinte resultado.")
print(f"\nO tempo médio que você deve estudar todos os dias: {mediana}")
print("\n\nAGUARDE! VOCÊ SERÁ REDIRECIONADO...\n\n")


#caminho_txt = r"C:\\Users\\breno\\OneDrive\\Documentos\\PROJETOS 1° PERIODO\\APP AULA atualizado\\respostas_dias_semana.txt"


time.sleep(10)
   

# ---------------------------------------------------------------------------------------------------------------------


def med_exatas(caminho_txt1):
    os.system("cls")
    notas = []
    with codecs.open(caminho_txt1, 'r', encoding='utf-8') as arquivo1:
        for linha in arquivo1:
            disciplina, nota_str = linha.strip().split(': ')
            nota = float(nota_str)
            notas.append((disciplina, nota))

    media_exatas = sum(nota for _, nota in notas) / len(notas)
    # Arredondando a média para uma casa decimal
    media_arredondada = round(media_exatas, 1)

    print("\nNotas:")
    for disciplina, nota in notas:
        print(f"{disciplina}: {nota}")
    print(f"\nMédia das notas: {media_arredondada}")

    return media_exatas

caminho_txt1 = r"C:\\Users\\breno\\OneDrive\\Documentos\\PROJETOS 1° PERIODO\\APP AULA atualizado\\respostas_media_exa.txt"
media_exatas = med_exatas(caminho_txt1)
print(f"A média final é: {media_exatas}")
# ------------------------------------------------------------------------------------------------------------------
def med_humanas(caminho_txt2):
    os.system("cls")
    notas = []
    with codecs.open(caminho_txt2, 'r', encoding='utf-8') as arquivo2:
        for linha in arquivo2:
            disciplina, nota_str = linha.strip().split(': ')
            nota = float(nota_str)
            notas.append((disciplina, nota))

    media_humanas = sum(nota for _, nota in notas) / len(notas)
    # Arredondando a média para uma casa decimal
    media_arredondada = round(media_humanas, 1)

    print("\nNotas:")
    for disciplina, nota in notas:
        print(f"{disciplina}: {nota}")
    print(f"\nMédia das notas: {media_arredondada}")

    return media_humanas

caminho_txt2 = r"C:\\Users\\breno\\OneDrive\\Documentos\\PROJETOS 1° PERIODO\\APP AULA atualizado\\respostas_media_huma.txt"
media_humanas = med_humanas(caminho_txt2)
print(f"A média final é: {media_humanas}")


#------------------------------------------------------------------------------------------------------------------------------------------------------------
def menu_opcoes(pergunta, opcoes):
    os.system("cls")
    print(pergunta)
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}. {opcao}")
    escolha = int(input("Escolha uma opção: "))
    return escolha


'''caminho_txt1 = r"C:\\Users\\breno\\OneDrive\\Documentos\\PROJETOS 1° PERIODO\\APP AULA atualizado\\respostas_media_exa.txt"
caminho_txt2 = r"C:\\Users\\breno\\OneDrive\\Documentos\\PROJETOS 1° PERIODO\\APP AULA atualizado\\respostas_media_huma.txt"'''
pergunta = "Escolha uma opção:"
opcoes = ["Visualizar notas de EXATAS;", "Visualizar notas de HUMANAS;",
          "Visualizar TUDO;", "Voltar para PÁGINA INICIAL;", "SAIR"]


'''media_exatas = med_exatas(caminho_txt1)
media_humanas = med_humanas(caminho_txt2)'''

while True:
    escolha = menu_opcoes(pergunta, opcoes)
    if escolha == 1:
        med_exatas(caminho_txt1)
        while True:  # Comparação das médias

            if (media_exatas < media_humanas):
                print(
                    "\n\nVocê será redirecionado para a página de estudos de EXATAS!!!")
                print("\n\nVocê precisa de dedicar mais a esta área")
                time.sleep(5)
                import quiz_exatas
            elif (media_exatas > media_humanas):
                med_humanas(caminho_txt2)
                time.sleep(5)
                print(
                    "\n\nVocê será redirecionado para a página de estudos de HUMANAS!!!")
                time.sleep(5)
                import quiz_humanas
                break
            else:
                med_exatas(caminho_txt1)
                time.sleep(3)
                med_humanas(caminho_txt2)
                time.sleep(3)
                os.system("cls")
                print(
                    "\n\nAs médias de EXATAS e HUMANAS são iguais.\n\nEscolha uma opção:")
                decisao = input(
                    "1-Para estudar exatas; \n2-Para estudar humanas.\n")
                while True:
                    if (decisao == '1'):
                            print(
                                "\n\nVocê será redirecionado para a página de estudos de EXATAS!!! \n\nAGUARDE!!!")
                            time.sleep(5)
                            import quiz_exatas
                            break
                    elif (decisao == '2'):
                            print(
                                "\n\nVocê será redirecionado para a página de estudos de HUMANAS!!!")
                            print("AGUARDE!!!")
                            time.sleep(5)
                            import quiz_humanas
                            break
                    else:
                            print("\nOpção inválida, tente novamente.")
                            time.sleep(1)
                            break
            break
               
    elif escolha == 2:
        med_humanas(caminho_txt2)
        time.sleep(5)
        while True:
            if (media_humanas < media_exatas):
                print(
                    "\n\nVocê será redirecionado para a página de estudos de HUMANAS!!!")
                print("Você precisa de dedicar mais a esta área")
                time.sleep(10)
                import quiz_humanas
                break
            elif (media_humanas > media_exatas):
                print(
                    "\n\nVocê será redirecionado para a página de estudos de HUMANAS!!!")
                time.sleep(5)
                import quiz_humanas
                break
            else:
                med_exatas(caminho_txt1)
                time.sleep(3)
                med_humanas(caminho_txt2)
                time.sleep(3)
                print(
                    "\n\nAs médias de EXATAS e HUMANAS são iguais.\n\nEscolha uma opção:")
                decisao = input(
                    "1-Para estudar exatas; \n2-Para estudar humanas.")
                while True:
                    if (decisao == '1'):
                            print(
                                "\n\nVocê será redirecionado para a página de estudos de EXATAS!!! \n\nAGUARDE!!!")
                            time.sleep(10)
                            import quiz_exatas
                            break
                    elif (decisao == '2'):
                            print(
                                "\n\nVocê será redirecionado para a página de estudos de HUMANAS!!!")
                            time.sleep(5)
                            import quiz_humanas
                            break
                    else:
                            print("\nOpção inválida, tente novamente.")
                            time.sleep(1)
                            break
            break
                

    elif escolha == 3:
        med_exatas(caminho_txt1)
        time.sleep(5)
        med_humanas(caminho_txt2)
        time.sleep(5)
        while True:
            if (media_humanas < media_exatas):
                print(
                    "\n\nVocê será redirecionado para a página de estudos de HUMANAS!!!\n\nAGUARDE!!!")
                time.sleep(10)
                import quiz_humanas
                break
            elif (media_exatas < media_humanas):
                print(
                    "\n\nVocê será redirecionado para a página de estudos de EXATAS!!! \n\nAGUARDE!!!")
                time.sleep(10)
                import quiz_exatas
                break
            else:
                med_exatas(caminho_txt1)
                time.sleep(3)
                med_humanas(caminho_txt2)
                time.sleep(3)
                print("\n\nAs médias são iguais.\n\nEscolha uma opção?.")
                decisao = input(
                    "1-Para estudar exatas; \n2-Para estudar humanas.\n")
                while True:
                    if (decisao == '1'):
                            print(
                                "\n\nVocê será redirecionado para a página de estudos de EXATAS!!! \n\nAGUARDE!!!")
                            time.sleep(10)
                            import quiz_exatas
                            break
                    elif (decisao == '2'):
                            print(
                                "\n\nVocê será redirecionado para a página de estudos de HUMANAS!!!")
                            print("AGUARDE!!!")
                            time.sleep(5)
                            import quiz_humanas
                            break
                    else:
                            print("\nOpção inválida, tente novamente.")
                            time.sleep(1)
                            break
            break
    
    elif escolha == 4:
        print("\n\nVocê será redirecionado para página inicial.\n\n")
        time.sleep(2)
        import pag_inicial
        break

    elif escolha == 5:
        print("\n\nVocê está saindo do aplicativo...\n\n")
        time.sleep(2)
        import main
        break

    else:
        # time.sleep(2)
        print("\n\nOpção inválida! Tente novamente.")
        time.sleep(2)
