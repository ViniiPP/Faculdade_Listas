print('MENU DE OPÇÕES')
print("1 - Tamanho da lista")
print("2 - Inserir nomes")
print("3 - Pesquisar nome")
print("4 - Excluir nome da lista")
print("5 - Exibir listas")
print("6 - Sair")

nomes = []

def definir_tamanho():
    tamanho = int(input("Digite o tamanho da lista de nomes: "))
    for i in range(tamanho):
        nomes.append(None)

def inserir_nomes():
    for i in range(len(nomes)):
        nome = input("Informe o nome {}: ".format(i+1))
        nomes[i] = nome

def pesquisar_nome():
    nome_pesquisado = input("Digite o nome que deseja pesquisar: ")
    if nome_pesquisado in nomes:
        print("Nome localizado.")
    else:
        print(nome_pesquisado, "Nome não econtrado")
        
def excluir_nome():
    nome_excluir = input("Digite o nome a ser excluído da lista: ")
    if nome_excluir in nomes:
        nomes.remove(nome_excluir)
        print(nome_excluir, "foi removido da lista")
    else:
        print(nome_excluir, "não foi encontrado na lista")

while True:
    print("-" * 60)
    
    opcao = int(input("Informe a opção que deseja executar: "))

    if opcao == 6:
        print("Programa encerrado")
        break
    elif opcao == 1:
        definir_tamanho()
    elif opcao == 2:
        inserir_nomes()
    elif opcao == 3:
        pesquisar_nome()
    elif opcao == 4:
        excluir_nome()
    elif opcao == 5:
        for nome in nomes:
            print('[',nome,']')
    else:
        print("Opção inválida, tente novamente")
