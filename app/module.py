def cadastrar_cliente(clientes):
    cpf = input("Digite seu CPF apenas numeros: ")

    for cliente in clientes:
        if cliente['cpf'] == cpf:
            return print("Erro! Esse CPF já está cadastrado")
    
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento: ")

    cliente = {
        'nome': nome,
        'cpf': cpf,
        'data_nascimento': data_nascimento
    }
    
    clientes.append(cliente)
    return

class Cliente():
    def __init__(self, nome, cpf, data_nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento


def main(): 
    clientes = []
    while True:
        opcao = input("Digite opcão: ")

        if opcao == 'A':
            cadastrar_cliente(clientes)
            #print(clientes)

        elif opcao == 'S': 
            break

    

main()

