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
    def __init__(self, nome, cpf, data_nascimento):
        super().__init__(nome, cpf, data_nascimento)

    def checar_disponiveis(self):
        pass

class Quarto():
    def __init__(self, numero,disponibilidade):
        self.__disponibilidade = disponibilidade
        self.__numero = numero
    
    @property
    def disponibilidade(self):
        return self.__disponibilidade

    @property
    def numero(self):
        return self.__numero
    
    @disponibilidade.setter
    def alterar_disponibilidade(self, nova_disponibilidade):
        self.__disponibilidade = nova_disponibilidade

    def mostrar_disponibilidade(self):
        if self.disponibilidade == True:
            return f"Quarto {self.numero}: Disponível"
        else:
            return f"Quarto {self.numero}: Indisponível"

class Reserva(Quarto):
    def __init__(self, numero, disponibilidade):
        super().__init__(numero, disponibilidade)

    def fazer_reserva(self):
        pass

def main(): 
    clientes = [] # Alterar para banco de dados
    quartos = [Quarto("1", True), Quarto("2", False), Quarto("3", False)] # Disponível?

    while True:
        opcao = input("Digite opcão: ")

        if opcao == '1':
            cadastrar_cliente(clientes)

        if opcao == '2':
            listar_clientes(clientes)

        if opcao == '3':

            print("-----QUARTOS------")
            i = 0
            for quarto in quartos:
                print(quartos[i].mostrar_disponibilidade())            
                i+=1
            print('------------------')

            quarto_escolhido = str((input("Digite o número do quarto que deseja se hospedar: ")))

            for quarto in quartos:
                if quarto_escolhido == quarto.numero and quarto.disponibilidade == True:
                    cpf = int(input("Informe seu CPF para completar a reserva: "))
                    for cliente in clientes:
                        if cliente.cpf == cpf:
                            quarto.alterar_disponibilidade = False
                            print(f"{cliente.nome}, obrigado por contar conosco!\n--Reserva completada!--\n{quarto.disponibilidade} ")
                    
            
        elif opcao == '9': 
            break

main()

