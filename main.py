import chardet
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
            print("Resposta inválida. Por favor, digite 'SIM/NÃO ou S/N.")


print("")
print("")
print("Bem-vindo")
print("Max Study")
print("")
print("")


resposta = menu_perguntas("Você possui cadastro?'SIM/NÃO ou S/N)")
while True:
    if resposta == True:
        while True:
            print("Login")
            login = input()
            if login == email_txt:
                print("Senha")
                senha = input()
                while True:
                    if senha == senha_txt:
                        print("Login efetuado com sucesso!")
                        import pag_inicial
                        break
                    else:
                        print("Senha incorreta! Tente novamente.") 
                        break
            else:
                print("Login incorreto! Tente novamente.")      
                break      
    else:
        import cadastroUser  # importando os dados do módulo cadastroUser
