import os  # biblioteca OS que limpa o terminal a cada
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
            print("Resposta inválida. Por favor, digite 'SIM/NÃO ou S/N:.")


tamanho_min = 5
tamanho_max = 50
tamanho_min1 = 8
tamanho_max1 = 13
tamanho_min2 = 4
tamanho_max2 = 8


while True:
    nome_completo = input("Nome completo: ")
    # função len retorna a quantidade de caracteres
    # função len percore por todos os caracteres  e é feita a comparação com o tamanho max. e min.
    if tamanho_min <= len(nome_completo) <= tamanho_max:
        print("Resposta válida!")
        break
    else:  # F string é uma função
        print(f"ERRO!!! O texto deve ter entre {
              tamanho_min} e {tamanho_max} caracteres.")
os.system("cls")
while True:
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    if tamanho_min1 <= len(data_nascimento) <= tamanho_max1:
        print("Resposta válida!")
        break
    else:
        print(f"ERRO!!! O texto deve ter entre {
              tamanho_min1} e {tamanho_max1} caracteres.")
os.system("cls")

while True:
    email = input("E-mail:")
    if tamanho_min <= len(email) <= tamanho_max:
        print("Resposta válida!")
        break
    else:
        print(f"ERRO!!! O texto deve ter entre {
              tamanho_min} e {tamanho_max} caracteres.")
os.system("cls")

while True:
    telefone = input("Telefone  ou celular(99-9999-9999): ")
    if tamanho_min1 <= len(telefone) <= tamanho_max1:
        print("Resposta válida!")
        break
    else:
        print(f"ERRO!!! O texto deve ter entre {tamanho_min1} e {
              tamanho_max1} caracteres.")
os.system("cls")
while True:
    senha = input("Crie uma senha, min. 4 e max. 8 caracteres: ")
    if tamanho_min2 <= len(senha) <= tamanho_max2:
        print("Resposta válida!")
        break
    else:
        print(f"ERRO!!! O texto deve ter entre {tamanho_min2} e {
              tamanho_max2} caracteres.")
os.system("cls")
while True:
    senha1 = input("Digite novamente sua senha:")
    if tamanho_min2 <= len(senha1) <= tamanho_max2:
        print("Resposta válida!")
        break
    else:
        print(f"ERRO!!! O texto deve ter entre {tamanho_min2} e {
              tamanho_max2} caracteres.")
os.system("cls")

while (senha != senha1):  # validação de senhas
    senha1 = input("Senhas não conferem, digite novamente: ")
    if senha1 != "":
        print("Senha: ", senha1)
    else:
        break
os.system("cls")

with open('email.txt', 'w') as emailtxt:
    for resposta in email:
        emailtxt.write(resposta)

with open('senha.txt', 'w') as senhatxt:
    for resposta in senha1:
        senhatxt.write(resposta)

print("")
print("")
print("Suas informações estão corretas? Senão, atualize.")
print("")
print("")
print("Nome completo: ", nome_completo)
print("Data de nascimento: ", data_nascimento)
print("E-mail: ", email)
print("Telefone ou celular: ", telefone)
print("Senha: ", senha1)
print("")
print("")
print("Aguarde 5 segundos...")
time.sleep(5)
os.system("cls")


while True:
    print("Digite (1) se deseja alterar ou (2) para finalizar.")
    cadastro = input("Digite sua escolha: ").strip().lower()
    if cadastro in ['1']:  # verificando se a cadastro está prsente na lista [atualizar]

        opcoes = input(
            "Digite o número da opção que deseja alterar: \n\n1-NOME COMPLETO; \n2-DATA DE NASCIMENTO; \n3-E-MAIL; \n4-TELEFONE; \n5-SENHA.\n")
        while True:
            if opcoes == '1':
                while True:
                    nome_completo = input("Nome completo: ")
                    if tamanho_min <= len(nome_completo) <= tamanho_max:
                        print("Resposta válida!")
                        break
                    else:
                        print(f"O texto deve ter entre {
                            tamanho_min} e {tamanho_max} caracteres.")
                        os.system("cls")
                break
            elif opcoes == '2':
                while True:
                    data_nascimento = input(
                        "Data de nascimento (DD/MM/AAAA): ")
                    if tamanho_min1 <= len(data_nascimento) <= tamanho_max1:
                        print("Resposta válida!")
                        break
                    else:
                        print(f"O texto deve ter entre {
                            tamanho_min1} e {tamanho_max1} caracteres.")
                        os.system("cls")
                break
            elif opcoes == '3':
                while True:
                    email = input("E-mail:")
                    if tamanho_min <= len(email) <= tamanho_max:
                        print("Resposta válida!")
                        break
                    else:
                        print(f"O texto deve ter entre {
                            tamanho_min} e {tamanho_max} caracteres.")
                        os.system("cls")
                break
            elif opcoes == '4':
                while True:
                    telefone = input("Telefone  ou celular(99-9999-9999): ")
                    if tamanho_min1 <= len(telefone) <= tamanho_max1:
                        print("Resposta válida!")
                        break
                    else:
                        print(f"O texto deve ter entre {tamanho_min1} e {
                            tamanho_max1} caracteres.")
                        os.system("cls")
                break
            elif opcoes == '5':
                while True:
                    senha = input(
                        "Crie uma senha, min. 4 e max. 8 caracteres: ")
                    if tamanho_min2 <= len(senha) <= tamanho_max2:
                        print("Resposta válida!")
                        break
                    else:
                        print(f"O texto deve ter entre {tamanho_min2} e {
                            tamanho_max2} caracteres.")
                        os.system("cls")
                    break
                while True:
                    senha1 = input("Digite novamente sua senha:")
                    if tamanho_min2 <= len(senha1) <= tamanho_max2:
                        print("Resposta válida!")
                        break
                    else:
                        print(f"O texto deve ter entre {tamanho_min2} e {
                            tamanho_max2} caracteres.")
                        os.system("cls")
                    break

                while (senha != senha1):  # validação de senhas
                    senha1 = input("Senhas não conferem, digite novamente: ")
                    if senha1 != "":
                        print("Senha: ", senha1)
                    else:
                     break
                    os.system("cls")
            else:
                print("Opção incorreta! Tente novamente.")
            break
        with open('email.txt', 'w') as emailtxt:
            for resposta in email:
                emailtxt.write(resposta)

        with open('senha.txt', 'w') as senhatxt:
            for resposta in senha1:
                senhatxt.write(resposta)

    elif cadastro in ['2']:
        print("")
        print("")
        print("Nome completo: ", nome_completo)
        print("Data de nascimento: ", data_nascimento)
        print("E-mail: ", email)
        print("Telefone ou celular: ", telefone)
        print("Senha: ", senha1)
        print("Cadastro concluído com sucesso!")

        cadastro_p = menu_perguntas("Você é professor(a)? SIM/NÃO")
        while True:
            if cadastro_p == True:
                print("Cadastro concluído com sucesso!")
                import main
                break
            else:
                cadastro = menu_perguntas(
                    "Você quer personalizar o seu cadastro? 'SIM/NÃO ou S/N:")
                while cadastro == True:
                    import cadastroP
                else:
                    import main
        break

    else:
        print("Resposta inválida, tente novamente!")
        print("Digite (1) se deseja alterar ou (2) para finalizar.")
        os.system("cls")
