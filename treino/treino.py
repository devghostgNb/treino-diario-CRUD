lista = []

def adicionar_contato(contato):
    lista.append(contato)
    print("Contato criado com sucesso!")

def listar():
    if not lista:
        print("Lista vazia")
        return

    print("\nLista de contatos:")
    for i, nome in enumerate(lista, start=1):
        print(f"{i} - {nome}")

def atualizar_contato(indice, novo_nome):
    if not lista:
        print("Lista vazia")
        return

    if 0 <= indice < len(lista):
        lista[indice] = novo_nome
        print("Contato atualizado com sucesso!")
    else:
        print("Contato inválido")

    print("\nLista atualizada")
    for i, nome in enumerate(lista, start=1):
        print(f"{i} - {nome}")

def remover_contato(indice):
    if not lista:
        print("Lista vazia")
        return
    if 0 <= indice < len(lista):
        removido = lista.pop(indice)
        print(f"Contato {removido} deletado com sucesso!")
    else:
        print("Contato inválido")

    print("\nLista atualizada")
    for i, nome in enumerate(lista, start=1):
        print(f"{i} - {nome}")


while True:
    print("\n1. Adicionar contatos")
    print("2. Ver contatos")
    print("3. Editar contatos")
    print("4. Deletar contatos")
    print("5. Sair")

    try:
        escolha = int(input("Digite a opção que desejar:"))

        if escolha == 1:
            nome = input("Digite o nome do contato:")
            adicionar_contato(nome)
        elif escolha == 2:
            listar()
        elif escolha == 3:
            if not lista:
                print("Lista vazia")
                continue
            listar()
            indice = int(input("Digite o indice que deseja editar:")) - 1
            novo_nome = input("Novo nome: ")
            atualizar_contato(indice, novo_nome)
        elif escolha == 4:
            if not lista:
                print("Lista vazia")
                continue
            listar()
            indice = int(input("digite o indice que deseja deletar:")) - 1
            remover_contato(indice)
        elif escolha == 5:
            print("Programa finalizado!")
            break
        else:
            print("Escolha inválida!")
    except ValueError:
        print("Digite um número válido!")




