import os
import chardet
import time
import statistics
import re

# Caminho do arquivo de texto com os horários


def calcular_mediana_horarios(caminho_txt):
    """
    Calcula a mediana de horários em um arquivo TXT, tratando diversos formatos.

    Args:
        caminho_txt (str): Caminho completo para o arquivo TXT.

    Returns:
        str: Mediana dos horários no formato HH:MM ou None em caso de erro.
    """

    horarios_em_minutos = []
    try:
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

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_txt}' não foi encontrado.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Exemplo de uso
caminho_do_arquivo = r"C:\\Users\\breno\\OneDrive\\Documentos\\PROJETOS 1° PERIODO\\APP AULA atualizado\\respostas_dias_semana.txt"
mediana = calcular_mediana_horarios(caminho_do_arquivo)
print(f"A mediana dos horários é: {mediana} minutos ou hora")

#caminho_txt = r"C:\\Users\\breno\\OneDrive\\Documentos\\PROJETOS 1° PERIODO\\APP AULA atualizado\\respostas_dias_semana.txt"


time.sleep(10)
   

# ---------------------------------------------------------------------------------------------------------------------


def med_exatas(caminho_txt1):
    os.system("cls")
    # Detectando a codificação do arquivo
    with open(caminho_txt1, 'rb') as arquivo1:
        resultado = chardet.detect(arquivo1.read())
        encoding = resultado['encoding']

    # Lendo o arquivo com a codificação correta
    with open(caminho_txt1, "r", encoding=encoding) as arquivo1:
        linhas = arquivo1.readlines()

    soma_notas1 = 0
    contagem_notas1 = 0

    for linha in linhas:
        linha = linha.strip()
        print(linha, "\n")
        try:
            # Extraindo a nota da linha e convertendo para float
            nota = float(linha.split(': ')[1])
            soma_notas1 += nota
            contagem_notas1 += 1
        except (IndexError, ValueError):
            print(f"Erro ao processar a linha: {linha}")
            continue

    # Calculando a média
    if contagem_notas1 > 0:
        media1 = soma_notas1 / contagem_notas1
    else:
        media1 = 0

    print("\nSoma das notas de exatas:", soma_notas1)
    print("Média das notas de exatas:", media1, "\n\n")

    return media1


# ------------------------------------------------------------------------------------------------------------------
def med_humanas(caminho_txt2):
    os.system("cls")
    # Detectando a codificação do arquivo
    with open(caminho_txt2, 'rb') as arquivo2:
        resultado = chardet.detect(arquivo2.read())
        encoding = resultado['encoding']

    # Lendo o arquivo com a codificação correta
    with open(caminho_txt2, "r", encoding=encoding) as arquivo2:
        linhas = arquivo2.readlines()

    soma_notas2 = 0
    contagem_notas2 = 0

    for linha in linhas:
        linha = linha.strip()
        print(linha, "\n")

        try:
            # Extraindo a nota da linha e convertendo para float
            nota = float(linha.split(': ')[1])
            soma_notas2 += nota
            contagem_notas2 += 1
        except (IndexError, ValueError):
            print(f"Erro ao processar a linha: {linha}")
            continue

    # Calculando a média
    if contagem_notas2 > 0:
        media2 = soma_notas2 / contagem_notas2
    else:
        media2 = 0

    print("\nSoma das notas de humanas:", soma_notas2)
    print("Média das notas de humanas:", media2, "\n\n")

    return media2


def menu_opcoes(pergunta, opcoes):
    os.system("cls")
    # Implementação do menu_opcoes com opções numeradas a partir de 1
    print(pergunta)
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}. {opcao}")
    escolha = int(input("Escolha uma opção: "))
    return escolha


caminho_txt1 = r"C:\\Users\\breno\\OneDrive\\Documentos\\PROJETOS 1° PERIODO\\APP AULA atualizado\\respostas_media_exa.txt"
caminho_txt2 = r"C:\\Users\\breno\\OneDrive\\Documentos\\PROJETOS 1° PERIODO\\APP AULA atualizado\\respostas_media_huma.txt"
pergunta = "Escolha uma opção:"
opcoes = ["Visualizar notas de EXATAS;", "Visualizar notas de HUMANAS;",
          "Visualizar TUDO;", "Voltar para PÁGINA INICIAL;", "SAIR"]


media_exatas = med_exatas(caminho_txt1)
media_humanas = med_humanas(caminho_txt2)

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
