def cadastrar_cliente(lista_clientes):
    cpf = int(input("Digite seu CPF apenas numeros: "))

    for cliente in lista_clientes:
        if cliente['cpf'] == cpf:
            return print("Erro! Esse CPF já está cadastrado")
    
    nome = str(input("Nome: "))
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")

    cliente = {
        'nome': nome,
        'cpf': cpf,
        'data_nascimento': data_nascimento
    }
    
    lista_clientes.append(cliente)
    return

def listar_clientes(lista_clientes):
    for cliente in lista_clientes:
        #print(cliente)
        print(f"Nome do cliente: {cliente['nome']} | CPF: {cliente['cpf']} | Data de nascimento: {cliente['data_nascimento']}")

class Cliente():
    def __init__(self, nome, cpf, data_nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento


def main(): 
    clientes = []
    while True:
        opcao = input("Digite opcão: ")

        if opcao == '1':
            cadastrar_cliente(clientes)

        if opcao == '2':
            listar_clientes(clientes)

        elif opcao == '9': 
            break

    

main()

