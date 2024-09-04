import unidecode
import os
import time

respostas = {
    'inicial': True,
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
            print("Resposta inválida. Por favor, digite 'Sim' ou 'Não'.")


def normalizar(texto):  # função para converter caracteres com acentos em textos simples. (texto)parâmetro
    return unidecode.unidecode(texto).lower()


def menu_perguntas(pergunta_1, resposta_certa):  # função para as perguntas
    os.system("cls")
    print(pergunta_1)
    # Solicita a resposta do usuário
    respostas = input("Digite sua resposta: ")
    # compara a resposta do usuário com a resposta certa e converte para o texto simples
    if normalizar(respostas) == normalizar(resposta_certa):
        print("Resposta correta!\n")
        return True
    else:
        print("Resposta incorreta.\n")
        return False


pergunta_1 = "Qual a disciplina você quer estudar? \n\n1-HISTÓRIA \n2-INGLÊS \n3-PORTUGUÊS \n4-FILOSOFIA \n5-ARTE \n\nDigite uma opção:"


def fazer_pergunta(pergunta, opcoes, resposta_correta):
    os.system("cls")
    print(pergunta)
    # uma lista para representar as opções das perguntas
    letras = ['A', 'B', 'C', 'D', 'E']
    # loop for utilizado para percorrer por cada opções e imprimir para o usuário as opções
    for i in range(len(opcoes)):
        print(f"{letras[i]}. {opcoes[i]}")

    # método upper utilizado para converter as strings em letras maiúsculas
    resposta = input("Escolha a opção correta (A/B/C/D/E): ").upper()

    if resposta in letras:  # verifica se a resposta é de acorodo com a lista de letras
        # comparação do indice da lista de respostas[0,1,2]
        os.system("cls")
        if resposta == letras[resposta_correta - 1]:
            print("Resposta correta!\n")
            return True
        else:
            print("Resposta incorreta.\n")
            return False
    else:
        print("Entrada inválida.\n")
        return False


def quiz():
    perguntas = [
        {
            "pergunta": "A Política do Café com Leite” e a Política dos Governadores são práticas políticas de qual período da República no Brasil",
            "opcoes": ["Era Vargas", "Primeira República", "Ditadura Militar", "Quarta República", "Nova República"],
            "resposta_correta": 2  # Alternativa B.
        },
        {
            "pergunta": "Programa de rádio criado durante a Era Vargas no qual eram propagandeados os feitos do governo:",
            "opcoes": ["Hora do Brasil", "Voz do Povo", "Trabalho no Brasil", "Povo do Brasil", "Vargas e o povo"],
            "resposta_correta": 1  # Alternativa A.
        }
    ]

    pontuacao = 0

    for pergunta in perguntas:
        if fazer_pergunta(pergunta["pergunta"], pergunta["opcoes"], pergunta["resposta_correta"]):
            pontuacao += 1

    print(f"Você acertou {pontuacao} de {len(perguntas)} perguntas.")


def quiz_1():
    perguntas = [
        {
            "pergunta": "1. (Mackenzie-2000) Assinale a alternativa que corretamente preenche as lacunas I, II e III das frases a seguir: \n\nHe __________(I) me a favor 2 months ago. \n\nThey __________(II) an attempt to escape. \n\nI __________(III) an important decision last night.",
            "opcoes": ["did – made – made", "made – did – made", "did – made – did", "made – made – made", "made – did – did"],
            "resposta_correta": 1  # Alternativa A.
        },
        {
            "pergunta": "(Marinha/2017) - Which option correctly completes the text below? The Rosetta Stone Egyptian hieroglyphic ________________ undeciphered until the 19th century. Members of Napoleon’s Egyptian expedition of 1799________________a black basalt stone, ______________ 114 x 72 cm, at Rashid (Rosetta). The stone ___________ with three different scripts: hieroglyphic, the derived demotic script,_________________ everyday purposes, and Greek. (...)",
            "opcoes": [" remained - discovered - measuring - was carved - used for", "remained - had discovered - measuring - carved - used to", "remained - had discovered - measuring - carved - used to", "had remained - discovered - measured - was carved - uses for", "could remain - discovered - measuring - would carve - uses for"],
            "resposta_correta": 1  # Alternativa A.
        }
    ]

    pontuacao = 0

    for pergunta in perguntas:
        if fazer_pergunta(pergunta["pergunta"], pergunta["opcoes"], pergunta["resposta_correta"]):
            pontuacao += 1

    print(f"Você acertou {pontuacao} de {len(perguntas)} perguntas.")


def quiz_2():
    perguntas = [
        {
            "pergunta": "MAR PORTUGUÊS\nÓ mar salgado, quanto do teu sal\nSão lágrimas de Portugal!\nPor te cruzarmos, quantas mães choraram,\nQuantos filhos em vão rezaram!\nQuantas noivas ficaram por casar\nPara que fosses nosso, ó mar!\nValeu a pena? Tudo vale a pena\nSe a alma não é pequena.\nQuem quer passar além do Bojador\nTem que passar além da dor.\nDeus ao mar o perigo e o abismo deu,\nMas nele é que espelhou o céu.\n\n\nEm relação aos versos 'Ó mar salgado, quanto do teu sal/ São lágrimas de Portugal', ocorrem, respectivamente, duas figuras de linguagem nomeadas:",
            "opcoes": ["Metáfora e onomatopeia.", "Catacrese e ironia.", "Anacoluto e antítese.", "Sinédoque e aliteração.", "Pleonasmo e metáfora."],
            "resposta_correta": 5  # Alternativa E.
        },
        {
            "pergunta": "Indique em quais alternativas foram usadas metáforas e em quais foram usadas comparações",
            "opcoes": ["Ele é simplesmente um deus grego.", "Ele é bonito.", " Suas palavras são doces da minha infância.", "Age como um burro!", "Age como um burro!"],
            "resposta_correta": 4  # Alternativa D.
        }
    ]

    pontuacao = 0

    for pergunta in perguntas:
        if fazer_pergunta(pergunta["pergunta"], pergunta["opcoes"], pergunta["resposta_correta"]):
            pontuacao += 1

    print(f"Você acertou {pontuacao} de {len(perguntas)} perguntas.")


def quiz_3():
    perguntas = [
        {
            "pergunta": "Para Aristóteles, o melhor regime político seria:",
            "opcoes": ["A democracia, onde todos poderiam opinar e participar das decisões tomadas.", "A monarquia, pois dessa maneira o comandante seria alguém que desde sua infância seria ensinado a como governar e assim estaria melhor preparado para tal cargo.", "O anarquismo, considerando a importância de se desenvolver uma sociedade sem classes e hierarquias.", "A aristocracia, pois segundo o filósofo, os aristocratas pensavam no bem comum e, portanto, seriam os mais aptos a comandarem um reino ou nação.", "Nenhuma."],
            "resposta_correta": 4  # Alternativa D.
        },
        {
            "pergunta": "Filósofo conhecido por sua teoria do contrato social, segundo a qual as pessoas renunciam a certos direitos naturais em troca de proteção e segurança por parte do Estado?",
            "opcoes": ["Karl Marx, ao afirmar que a constituição uma sociedade pautada em classes sociais acaba por ser a melhor forma de organização social.", "Friedrich Nietzsche, ao propor a ideia do “além-do-homem”.", " John Locke, quando defende que o direito a propriedade é algo inalienável, tal como a vida, liberdade e propriedade, e que o governo deve proteger esses direitos.", "Jean-Paul Sartre, existencialista, que apresentou a teoria de que a existência precede a essência.", "Nenhuma."],
            "resposta_correta": 3  # Alternativa C.
        }
    ]

    pontuacao = 0

    for pergunta in perguntas:
        if fazer_pergunta(pergunta["pergunta"], pergunta["opcoes"], pergunta["resposta_correta"]):
            pontuacao += 1

    print(f"Você acertou {pontuacao} de {len(perguntas)} perguntas.")


def quiz_4():
    perguntas = [
        {
            "pergunta": "A arte contemporânea no século XX caracterizou-se por uma explosão de diversidade e experimentação, desafiando convenções tradicionais. Diante desse contexto, qual movimento artístico do século XX foi marcado por representações simultâneas de diferentes perspectivas, como afirmado por Pablo Picasso?",
            "opcoes": ["Impressionismo", "Pop Art", "Cubismo", "Surrealismo", "Expressionismo Abstrato"],
            "resposta_correta": 3  # Alternativa C.
        },
        {
            "pergunta": "A origem da arte remonta aos primórdios da humanidade, sendo inicialmente evidenciada por pinturas rupestres e esculturas na Pré-História. Qual característica marcante da arte pré-histórica revela a capacidade dos seres humanos de se expressarem artisticamente?",
            "opcoes": ["Utilização intensiva de cores vibrantes.", "Representação abstrata de emoções.", "Uso de materiais modernos.", "Foco na simetria perfeita.", "Busca por representar o cotidiano e a relação com a natureza."],
            "resposta_correta": 5  # Alternativa E.
        }
    ]

    pontuacao = 0

    for pergunta in perguntas:
        if fazer_pergunta(pergunta["pergunta"], pergunta["opcoes"], pergunta["resposta_correta"]):
            pontuacao += 1

    print(f"Você acertou {pontuacao} de {len(perguntas)} perguntas.")


while True:
    resposta_certa1 = input(pergunta_1 + " ")
    resposta_certa1_normalizada = normalizar(resposta_certa1)

    if resposta_certa1_normalizada == "1":
        print("Assunto que você pode estudar:")
        link = "https://brasilescola.uol.com.br/historiab/brasil-republica.htm"
        print(f"Brasil República: {link}")
        print("")
        print("Após estudar o assunto, responda o QUIZ:")
        time.sleep(5)
        quiz()
        print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
        while True:

            final = input().lower()
            if final in ['inicial']:
                import pag_inicial
            elif final in ['sair']:
                import main
            elif final in ['continuar']:
                import notas
            else:
                print("Resposta inválida, tente novamente!")
                print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
            break

    elif resposta_certa1_normalizada == "2":
        print("Assunto que você pode estudar:")
        link = "https://mundoeducacao.uol.com.br/ingles/simple-past.htm"
        print(f"Simple Past: {link}")
        print("")
        print("Após estudar o assunto, responda o QUIZ:")
        time.sleep(5)
        quiz_1()
        print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
        while True:

            final = input().lower()
            if final in ['inicial']:
                import pag_inicial
            elif final in ['sair']:
                import main
            elif final in ['continuar']:
                import notas
            else:
                print("Resposta inválida, tente novamente!")
                print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
            break

    elif resposta_certa1_normalizada == "3":
        print("Assunto que você pode estudar:")
        link = "https://brasilescola.uol.com.br/gramatica/figuras-linguagem.htm"
        print(f"Figuras de Linguagem: {link}")
        print("")
        print("Após estudar o assunto, responda o QUIZ:")
        time.sleep(5)
        quiz_2()
        print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
        while True:

            final = input().lower()
            if final in ['inicial']:
                import pag_inicial
            elif final in ['sair']:
                import main
            elif final in ['continuar']:
                import notas
            else:
                print("Resposta inválida, tente novamente!")
                print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
            break

    elif resposta_certa1_normalizada == "4":
        print("Assunto que você pode estudar:")
        link = "https://brasilescola.uol.com.br/filosofia/filosofia-politica.htm"
        print(f"Filosofia Politica: {link}")
        print("")
        print("Após estudar o assunto, responda o QUIZ:")
        time.sleep(5)
        quiz_3()
        print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
        while True:
            final = input().lower()
            if final in ['inicial']:
                import pag_inicial
            elif final in ['sair']:
                import main
            elif final in ['continuar']:
                import notas
            else:
                print("Resposta inválida, tente novamente!")
                print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
            break

    elif resposta_certa1_normalizada == "5":
        print("Assunto que você pode estudar:")
        link = "https://brasilescola.uol.com.br/historiag/historia-da-arte.htm"
        print(f"História da Arte: {link}")
        print("")
        print("Após estudar o assunto, responda o QUIZ:")
        time.sleep(5)
        quiz_4()
        print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
        while True:

            final = input().lower()
            if final in ['inicial']:
                import pag_inicial
            elif final in ['sair']:
                import main
            elif final in ['continuar']:
                import notas
            else:
                print("Resposta inválida, tente novamente!")
                print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
            break
