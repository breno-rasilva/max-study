import unidecode

respostas = {
    'inicial': True,
    'não': False,
    's': True,
    'n': False,
    'nao': False
}


def menu_perguntas(pergunta):  # função para as perguntas
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


pergunta_1 = "Qual a disciplina você quer estudar?"


def fazer_pergunta(pergunta, opcoes, resposta_correta):
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
        if resposta == letras[resposta_correta - 1]:
            print("Resposta correta!\n")
            return True
        else:
            print("Resposta incorreta.\n")
            return False
    else:
        print("Entrada inválida.\n")
        return False


def quiz_1():
    perguntas = [
        {
            "pergunta": "(UFBA) 35 estudantes estrangeiros vieram ao Brasil. 16 visitaram Manaus; 16, S. Paulo e 11, Salvador. Desses estudantes, 5 visitaram Manaus e Salvador e, desses 5, 3 visitaram também São Paulo. O número de estudantes que visitaram Manaus ou São Paulo foi:",
            "opcoes": ["29", "24", "11", "8", "30"],
            "resposta_correta": 1  # Alternativa A.
        },
        {
            "pergunta": "(UFSE) Os senhores A, B e C concorriam à liderança de certo partido político. Para escolher o líder, cada eleitor votou apenas em dois candidatos de sua preferência. Houve 100 votos para A e B, 80 votos para B e C e 20 votos para A e C. Em consequência:",
            "opcoes": ["venceu A, com 120 votos", "venceu A, com 140 votos", "A e B empataram em primeiro lugar", "venceu B, com 140 votos", "venceu B, com 180 votos"],
            "resposta_correta": 5  # Alternativa E.
        }
    ]

    pontuacao = 0  # pontuação inicial em zero

    for pergunta in perguntas:  # repete a pergunta na lista de perguntas
        # função para de pergunta ao usuário se resposta verdadeira ele retorna True e False caso contrário
        if fazer_pergunta(pergunta["pergunta"], pergunta["opcoes"], pergunta["resposta_correta"]):
            pontuacao += 1

    # imprimi para o usuário quantas respostas ele acertou
    print(f"Você acertou {pontuacao} de {len(perguntas)} perguntas.")


def quiz_2():
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


def quiz_4():
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


def quiz_5():
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


def quiz_6():
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


def quiz_7():
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


def quiz_8():
    perguntas = [
        {
            "pergunta": "A ecologia é uma parte da biologia que estuda a relação dos organismos com o meio que os cerca. Os organismos interagem entre si e com todas as partes não vivas do ambiente, tais como solo, água, temperatura e umidade. Essas partes não vivas são chamadas de:",
            "opcoes": ["Fatores abióticos.", "Fatores bióticos.", "Biosfera.", "Nicho ecológico.", "Ecossistema."],
            "resposta_correta": 1  # Alternativa A.
        },
        {
            "pergunta": "(UEPB) Considerando a poluição de um ecossistema aquático por produtos clorados, a exemplo de DDT, o componente biótico da cadeia que deverá apresentar maior concentração do produto será",
            "opcoes": ["O fitoplâncton", "O zooplâncton", "Os peixes planctófagos", "Os peixes carnívoros", "As aves piscívoras"],
            "resposta_correta": 5  # Alternativa E.
        }
    ]

    pontuacao = 0

    for pergunta in perguntas:
        if fazer_pergunta(pergunta["pergunta"], pergunta["opcoes"], pergunta["resposta_correta"]):
            pontuacao += 1

    print(f"Você acertou {pontuacao} de {len(perguntas)} perguntas.")


def quiz_9():
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


# final = str

while True:
    resposta_certa1 = input(pergunta_1 + " ")
    resposta_certa1_normalizada = normalizar(resposta_certa1)

    if resposta_certa1_normalizada == "matematica":
        print("Assunto que você pode estudar:")
        link = "https://www.todamateria.com.br/conjuntos-numericos/"
        print(f"Conjuntos Numéricos: {link}")
        print("")
        print("Após estudar o assunto, responda o QUIZ:")
        quiz_1()
        print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
        while True:

            final = input().lower()
            if final in ['inicial']:
                import pag_inicial
            elif final in ['sair']:
                import main
            elif final in ['continuar']:
                import estudos
            else:
                print("Resposta inválida, tente novamente!")
                print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
            break
    elif resposta_certa1_normalizada == "historia":
        print("Assunto que você pode estudar:")
        link = "https://brasilescola.uol.com.br/historiab/brasil-republica.htm"
        print(f"Brasil República: {link}")
        print("")
        print("Após estudar o assunto, responda o QUIZ:")
        quiz_2()
        print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
        while True:

            final = input().lower()
            if final in ['inicial']:
                import pag_inicial
            elif final in ['sair']:
                import main
            elif final in ['continuar']:
                import estudos
            else:
                print("Resposta inválida, tente novamente!")
                print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
            break
    elif resposta_certa1_normalizada == "geografia":
        print("Assunto que você pode estudar:")
        link = "https://www.suapesquisa.com/geografia/pernambuco.htm"
        print(f"Geografia de Pernambuco: {link}")
        print("")
        print("Após estudar o assunto, responda o QUIZ:")
        quiz_3()
        print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
        while True:

            final = input().lower()
            if final in ['inicial']:
                import pag_inicial
            elif final in ['sair']:
                import main
            elif final in ['continuar']:
                import estudos
            else:
                print("Resposta inválida, tente novamente!")
                print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
            break
    elif resposta_certa1_normalizada == "ingles":
        print("Assunto que você pode estudar:")
        link = "https://mundoeducacao.uol.com.br/ingles/simple-past.htm"
        print(f"Simple Past: {link}")
        print("")
        print("Após estudar o assunto, responda o QUIZ:")
        quiz_4()
        print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
        while True:

            final = input().lower()
            if final in ['inicial']:
                import pag_inicial
            elif final in ['sair']:
                import main
            elif final in ['continuar']:
                import estudos
            else:
                print("Resposta inválida, tente novamente!")
                print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
            break
    elif resposta_certa1_normalizada == "lingua portuguesa":
        print("Assunto que você pode estudar:")
        link = "https://brasilescola.uol.com.br/gramatica/figuras-linguagem.htm"
        print(f"Figuras de Linguagem: {link}")
        print("")
        print("Após estudar o assunto, responda o QUIZ:")
        quiz_5()
        print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
        while True:

            final = input().lower()
            if final in ['inicial']:
                import pag_inicial
            elif final in ['sair']:
                import main
            elif final in ['continuar']:
                import estudos
            else:
                print("Resposta inválida, tente novamente!")
                print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
            break
    elif resposta_certa1_normalizada == "filosofia":
        print("Assunto que você pode estudar:")
        link = "https://brasilescola.uol.com.br/filosofia/filosofia-politica.htm"
        print(f"Filosofia Politica: {link}")
        print("")
        print("Após estudar o assunto, responda o QUIZ:")
        quiz_6()
        print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
        while True:
            final = input().lower()
            if final in ['inicial']:
                import pag_inicial
            elif final in ['sair']:
                import main
            elif final in ['continuar']:
                import estudos
            else:
                print("Resposta inválida, tente novamente!")
                print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
            break
    elif resposta_certa1_normalizada == "quimica":
        print("Assunto que você pode estudar:")
        link = "https://brasilescola.uol.com.br/quimica/quimica-organica.htm"
        print(f"Química Orgânica: {link}")
        print("")
        print("Após estudar o assunto, responda o QUIZ:")
        quiz_7()
        print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
        while True:

            final = input().lower()
            if final in ['inicial']:
                import pag_inicial
            elif final in ['sair']:
                import main
            elif final in ['continuar']:
                import estudos
            else:
                print("Resposta inválida, tente novamente!")
                print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
            break
    elif resposta_certa1_normalizada == "biologia":
        print("Assunto que você pode estudar:")
        link = "https://mundoeducacao.uol.com.br/biologia/ecologia.htm"
        print(f"Ecologia: {link}")
        print("")
        print("Após estudar o assunto, responda o QUIZ:")
        quiz_8()
        print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
        while True:

            final = input().lower()
            if final in ['inicial']:
                import pag_inicial
            elif final in ['sair']:
                import main
            elif final in ['continuar']:
                import estudos
            else:
                print("Resposta inválida, tente novamente!")
                print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
            break
    elif resposta_certa1_normalizada == "arte":
        print("Assunto que você pode estudar:")
        link = "https://brasilescola.uol.com.br/historiag/historia-da-arte.htm"
        print(f"História da Arte: {link}")
        print("")
        print("Após estudar o assunto, responda o QUIZ:")
        quiz_9()
        print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
        while True:

            final = input().lower()
            if final in ['inicial']:
                import pag_inicial
            elif final in ['sair']:
                import main
            elif final in ['continuar']:
                import estudos
            else:
                print("Resposta inválida, tente novamente!")
                print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
            break
    else:
        print("Disciplina não cadastrada!")
        print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
        while True:

            final = input().lower()
            if final in ['inicial']:
                import pag_inicial
            elif final in ['sair']:
                import main
            elif final in ['continuar']:
                import estudos
            else:
                print("Resposta inválida, tente novamente!")
                print("Digite 'INICIAL' para voltar para página inicial  \nDigite 'SAIR' para sair do aplicativo \nDigite 'CONTINUAR' para permanecer na pagina de estudos")
