import os
import time
respostas = {
    'sim': True,
    'não': False,
    's': True,
    'n': False,
    'nao': False
}


def email_caminho(emailtxt):
    with open(emailtxt, "r", encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        if linhas:
            return linhas[0].strip()
        return None


def senha_caminho(senhatxt):
    with open(senhatxt, "r", encoding='utf-8') as arquivo1:
        linhas = arquivo1.readlines()
        if linhas:
            return linhas[0].strip()
        return None


emailtxt = r"C:\\Users\\breno\\OneDrive\\Documentos\\PROJETOS 1° PERIODO\\APP AULA atualizado\\email.txt"
senhatxt = r"C:\\Users\\breno\\OneDrive\\Documentos\\PROJETOS 1° PERIODO\\APP AULA atualizado\\senha.txt"

email_txt = email_caminho(emailtxt)
senha_txt = senha_caminho(senhatxt)


def menu_perguntas(pergunta):  # função para as perguntas
    while True:

        print(pergunta)
        resposta = input("Digite sua resposta: ").strip().lower()

        if resposta in respostas:

            return respostas[resposta]
        else:

            print("Resposta inválida. Por favor, digite 'SIM/NÃO ou S/N':")


print("")
print("")
print("BEM-VINDO")
print("Max Study")
print("")
print("")
time.sleep(5)

resposta = menu_perguntas("\n\nVocê possui cadastro?'SIM/NÃO ou S/N':)")
while True:
    time.sleep(2)
    os.system("cls")
    if resposta == True:
        while True:
            print("\n\nLogin (utilize o seu E-MAIL para efetuar o login)")
            login = input()
            if login == email_txt:
                print("\nSenha")
                senha = input()
                while True:
                    if senha == senha_txt:
                        print("Login efetuado com sucesso!")
                        import pag_inicial
                        break
                    else:
                        print("\n\nSenha incorreta! Refaça o seu login.")
                        break
            else:
                print("\n\nLogin incorreto! Refaça o seu login.")
                break
    else:
        import cadastroUser  # importando os dados do módulo cadastroUser
