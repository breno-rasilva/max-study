import os  #biblioteca OS que limpa o terminal a cada

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
            print("Resposta inválida. Por favor, digite 'SIM/NÃO ou S/N:.")


print("")
print("\nPágina inicial")
print("")
print("\nEscolha uma opção:")
print("")


while True:
    print("Área de estudos: Digite (1) \nSair do aplicativo: Digite (2)")
    pergunta = input()
    os.system("cls")
    pergunta = pergunta.lower()
    if pergunta in ['1']:
        import notas
    elif pergunta in ['2']:
        import main
    else:
        print("\n\nAlternativa inválida! Tente novamente.\n\n")
    
