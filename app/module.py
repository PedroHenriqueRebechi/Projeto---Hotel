def cadastrar_cliente(lista_clientes):
    cpf = int(input("Digite seu CPF apenas numeros: "))

    for cliente in lista_clientes:
        if cliente.cpf == cpf:
            return print("Erro! Esse CPF já está cadastrado")
        
    nome = str(input("Nome: "))
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    
    cliente = Cliente(nome=nome, data_nascimento=data_nascimento, cpf=cpf)
    
    lista_clientes.append(cliente)
    return

def listar_clientes(lista_clientes):
    for cliente in lista_clientes:
        print(cliente.__repr__())

class Cliente():
    def __init__(self, nome, cpf, data_nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def data_nascimento(self):
        return self.__data_nascimento
    
    def __repr__(self):
        return f"Cliente: {self.nome} | CPF: {self.cpf} | Data de Nascimento: {self.data_nascimento}"
    
    """def entrar_conta(self, lista_clientes):
        login = int(input("Digite seu CPF: "))

        for cliente in lista_clientes:
            if cliente.cpf != login:
                return print("Erro! Esse CPF não está cadastrado")
        
        return """
    
class Verifica(Cliente):
    pass


def main(): 
    clientes = [] # Alterar para banco de dados
    while True:
        opcao = input("Digite opcão: ")

        if opcao == '1':
            cadastrar_cliente(clientes)

        if opcao == '2':
            listar_clientes(clientes)

        elif opcao == '9': 
            break

main()

