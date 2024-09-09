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



def menu_opcoes(pergunta, opcoes):
    os.system("cls")
    print(pergunta)
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}. {opcao}")
    escolha = int(input("Escolha uma opção: "))
    return escolha


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

    if resposta in letras:  
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
    os.system("cls")
    perguntas = [
        {
            "pergunta": "(UFBA) 35 estudantes estrangeiros vieram ao Brasil. 16 visitaram Manaus; 16, S. \nPaulo e 11, Salvador. Desses estudantes, 5 visitaram Manaus e Salvador e, desses 5, 3 visitaram também São Paulo. \nO número de estudantes que visitaram Manaus ou São Paulo foi:",
            "opcoes": ["29", "24", "11", "8", "30"],
            "resposta_correta": 1  # Alternativa A.
        },
        {
            "pergunta": "(UFSE) Os senhores A, B e C concorriam à liderança de certo partido político. \nPara escolher o líder, cada eleitor votou apenas em dois candidatos de sua preferência. \nHouve 100 votos para A e B, 80 votos para B e C e 20 votos para A e C. Em consequência:",
            "opcoes": ["venceu A, com 120 votos", "venceu A, com 140 votos", "A e B empataram em primeiro lugar", "venceu B, com 140 votos", "venceu B, com 180 votos"],
            "resposta_correta": 5  # Alternativa E.
        }
    ]
    pontuacao = 0 
    for pergunta in perguntas:  
        if fazer_pergunta(pergunta["pergunta"], pergunta["opcoes"], pergunta["resposta_correta"]):
            pontuacao += 1
    print(f"\n\nVocê acertou {pontuacao} de {len(perguntas)} perguntas.\n\n")


def quiz_1():
    os.system("cls")
    perguntas = [
        {
            "pergunta": "A ecologia é uma parte da biologia que estuda a relação dos organismos com o meio que os cerca. \nOs organismos interagem entre si e com todas as partes não vivas do ambiente, tais como solo, água, \ntemperatura e umidade. Essas partes não vivas são chamadas de:",
            "opcoes": ["Fatores abióticos.", "Fatores bióticos.", "Biosfera.", "Nicho ecológico.", "Ecossistema."],
            "resposta_correta": 1  # Alternativa A.
        },
        {
            "pergunta": "(UEPB) Considerando a poluição de um ecossistema aquático por produtos clorados, a exemplo de DDT, \no componente biótico da cadeia que deverá apresentar maior concentração do produto será:",
            "opcoes": ["O fitoplâncton", "O zooplâncton", "Os peixes planctófagos", "Os peixes carnívoros", "As aves piscívoras"],
            "resposta_correta": 5  # Alternativa E.
        }
    ]

    pontuacao = 0

    for pergunta in perguntas:
        os.system("cls")
        if fazer_pergunta(pergunta["pergunta"], pergunta["opcoes"], pergunta["resposta_correta"]):
            pontuacao += 1

    print(f"\n\nVocê acertou {pontuacao} de {len(perguntas)} perguntas.\n\n")


def quiz_2():
    perguntas = [
        {
            "pergunta": "(UESPI) Os representantes dos compostos dessa função orgânica são oxigenados. Têm caráter relativamente ácido, porém, menos ácido que os ácidos carboxílicos. Em geral, eles são pouco solúveis ou insolúveis em água, mas os seus sais são bem mais solúveis. Alguns são utilizados como desinfetantes e na produção de resinas. As características apontadas anteriormente estão associadas à função:",
            "opcoes": ["Álcool.", "Aldeído.", "Cetona.", "Éter.", "Fenol."],
            "resposta_correta": 5  # Alternativa E.
        },
        {
            "pergunta": "Qual das afirmativas a seguir sobre funções orgânicas está incorreta?",
            "opcoes": ["Todo hidrocarboneto possui apenas carbono e hidrogênio.", "Os haletos orgânicos são derivados da substituição de um ou mais hidrogênios por átomos de halogênios.", "Os aldeídos possuem o grupo carbonila entre dois átomos de carbono.", "Tanto as cetonas quanto os aldeídos possuem o grupo carbonila.", "As aminas são derivadas da amônia pela substituição de um, dois ou três hidrogênios por cadeias carbônicas."],
            "resposta_correta": 3  # Alternativa C.
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
            "pergunta": "Pernambuco é um Estado que se estende de maneira alongada (de Leste a Oeste), no Nordeste brasileiro. Assinale a alternativa que contém o nome dos Estados que fazem divisa com Pernambuco.",
            "opcoes": ["Rio Grande do Norte, Sergipe, Bahia, Paraíba e Ceará", "Bahia, Alagoas, Piauí, Ceará e Paraíba", "Ceará, Piauí, Maranhão, Sergipe, Rio Grande do Norte e Tocantins", "Paraíba, Piauí, Maranhão e Alagoas", "Bahia, Alagoas, Paraíba e Sergipe"],
            "resposta_correta": 2  # Alternativa B.
        },
        {
            "pergunta": "Pernambuco é uma unidade federativa do Brasil. Sendo assim, o estado integra uma das cinco Regiões do país. Portanto, marque a alternativa que indica corretamente a Região que abriga o estado de Pernambuco.",
            "opcoes": ["Sul", "Norte", "Nordeste", "Centro-Oeste", "Sudeste"],
            "resposta_correta": 3  # Alternativa C.
        }
    ]

    pontuacao = 0

    for pergunta in perguntas:
        if fazer_pergunta(pergunta["pergunta"], pergunta["opcoes"], pergunta["resposta_correta"]):
            pontuacao += 1

    print(f"Você acertou {pontuacao} de {len(perguntas)} perguntas.")


# -----------------------------------------------------------------------------------------------------
while True:
    os.system("cls")
    pergunta = "Escolha uma opção:"
    opcoes = ["Matemática;", "Biologia;",
          "Química;", "Geografia;"]
    escolha = menu_opcoes(pergunta, opcoes)

    if escolha == 1:
        print("\n\nAssunto que você pode estudar:")
        link = "https://www.todamateria.com.br/conjuntos-numericos/"
        print(f"Conjuntos Numéricos: {link}")
        print("")
        print("\n\nApós estudar o assunto, responda o QUIZ:\n\n")
        time.sleep(5)
        quiz()
        print("Digite '1' para voltar para página inicial  \n\nDigite '2' para sair do aplicativo \n\nDigite '3' para permanecer na pagina de estudos")
        while True:

            final = input().lower()
            if final in ['1']:
                import pag_inicial
            elif final in ['2']:
                import main
            elif final in ['3']:
                import notas
            else:
                print("\n\nResposta inválida, tente novamente!\n\n")
                print("Digite 'INICIAL' para voltar para página inicial  \n\nDigite 'SAIR' para sair do aplicativo \n\nDigite 'CONTINUAR' para permanecer na pagina de estudos")
            break
    elif escolha == 2:
        os.system("cls")
        print("\n\nAssunto que você pode estudar:")
        link = "https://mundoeducacao.uol.com.br/biologia/ecologia.htm"
        print(f"Ecologia: {link}")
        print("")
        print("Após estudar o assunto, responda o QUIZ:")
        time.sleep(5)
        quiz_1()
        print("Digite 'INICIAL' para voltar para página inicial  \n\nDigite 'SAIR' para sair do aplicativo \n\nDigite 'CONTINUAR' para permanecer na pagina de estudos")
        while True:

            final = input().lower()
            if final in ['1']:
                import pag_inicial
            elif final in ['2']:
                import main
            elif final in ['3']:
                import notas
            else:
                print("Resposta inválida, tente novamente!")
                print("Digite '1' para voltar para página INICIAL  \nDigite '2' para SAIR do aplicativo \nDigite '3' para PERMANECER na pagina de estudos")
            break
    elif escolha == 3:
        print("\n\nAssunto que você pode estudar:")
        link = "https://brasilescola.uol.com.br/quimica/quimica-organica.htm"
        print(f"Química Orgânica: {link}")
        print("")
        print("Após estudar o assunto, responda o QUIZ:")
        time.sleep(5)
        quiz_2()
        print("Digite '1' para voltar para página INICIAL  \nDigite '2' para SAIR do aplicativo \nDigite '3' para PERMANECER na pagina de estudos")
        while True:

            final = input().lower()
            if final in ['1']:
                import pag_inicial
            elif final in ['2']:
                import main
            elif final in ['3']:
                import notas
            else:
                print("Resposta inválida, tente novamente!")
                print("Digite '1' para voltar para página INICIAL  \nDigite '2' para SAIR do aplicativo \nDigite '3' para PERMANECER na pagina de estudos")
            break

    elif escolha == 4:
        print("\n\nAssunto que você pode estudar:")
        link = "https://www.suapesquisa.com/geografia/pernambuco.htm"
        print(f"Geografia de Pernambuco: {link}")
        print("")
        print("Após estudar o assunto, responda o QUIZ:")
        time.sleep(5)
        quiz_3()
        print("Digite '1' para voltar para página INICIAL  \nDigite '2' para SAIR do aplicativo \nDigite '3' para PERMANECER na pagina de estudos")
        while True:

            final = input().lower()
            if final in ['1']:
                import pag_inicial
            elif final in ['2']:
                import main
            elif final in ['3']:
                import notas
            else:
                print("Resposta inválida, tente novamente!")
                print("Digite '1' para voltar para página INICIAL  \nDigite '2' para SAIR do aplicativo \nDigite '3' para PERMANECER na pagina de estudos")
            break

    else:
        os.system("cls")
        print("\n\nDisciplina não cadastrada!\n\n")
        print("Digite '1' para voltar para página INICIAL  \nDigite '2' para SAIR do aplicativo \nDigite '3' para PERMANECER na pagina de estudos")
        while True:

            final = input().lower()
            if final in ['1']:
                import pag_inicial
            elif final in ['2']:
                import main
            elif final in ['3']:
                import notas
            else:
                print("\n\nResposta inválida, tente novamente!\n\n")
                print("Digite '1' para voltar para página INICIAL  \nDigite '2' para SAIR do aplicativo \nDigite '3' para PERMANECER na pagina de estudos")
