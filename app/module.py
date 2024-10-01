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
        return f"Cliente: {self.nome} | CPF: ***.{self.cpf[4:11]}-** | Data de Nascimento: {self.data_nascimento}"

class Quarto():
    def __init__(self, numero,disponibilidade, preco=100):
        self.__disponibilidade = disponibilidade
        self.numero = numero
        self.preco = preco
    
    @property
    def disponibilidade(self):
        return self.__disponibilidade

    @disponibilidade.setter
    def alterar_disponibilidade(self, nova_disponibilidade):
        self.__disponibilidade = nova_disponibilidade

    def mostrar_disponibilidade(self):
        if self.disponibilidade == True:
            return f"Quarto {self.numero}: Disponível"
        else:
            return f"Quarto {self.numero}: Indisponível"

class Reserva(Quarto):
    def __init__(self, quarto, data_entrada, data_saida):
        self.quarto = quarto
        self.data_entrada = data_entrada
        self.data_saida = data_saida

    def reservar(self, quarto, clientes):
        cpf = str(input("Informe seu CPF para completar a reserva: "))

        if len(clientes) == 0:
            return print(f"\nO seu CPF não está cadastrado no nosso sistema")
        
        for cliente in clientes:
            if cliente.cpf == cpf:
                quarto.alterar_disponibilidade = False
                print(f"\n{cliente.nome}, obrigado por contar conosco!\n--Reserva completada!--")
            else:
                print(f'O seu CPF não está cadastrado no nosso sistema')
        return


def cadastrar_cliente(lista_clientes):
    cpf = str(input("Digite seu CPF: "))

    for cliente in lista_clientes:
        if cliente.cpf == cpf:
            return print("\nErro! Esse CPF já está cadastrado")
        
    nome = str(input("Nome: "))
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    
    cliente = Cliente(nome=nome, data_nascimento=data_nascimento, cpf=cpf)
    
    lista_clientes.append(cliente)
    return

def listar_clientes(lista_clientes):
    for cliente in lista_clientes:
        print(cliente.__repr__())

def menu():
    opcoes = """
----MENU----
[1] Fazer cadastro
[2] Listar clientes
[3] Fazer reserva

[9] Sair

Digite sua opção: """
    return int(input(opcoes))

def escolher_quarto(lista_quartos, lista_clientes):
    print("-----QUARTOS------")
    i = 0
    for quarto in lista_quartos:
        print(lista_quartos[i].mostrar_disponibilidade())            
        i+=1
    print('------------------')

    quarto_escolhido = str(input("Digite o número do quarto que deseja se hospedar: "))
    data_entrada = str(input("Digite a data do check-in: "))
    data_saida = str(input("Digite a data do check-out: "))

    for quarto in lista_quartos:
        if quarto_escolhido == quarto.numero and quarto.disponibilidade == True:
            nova_reserva = Reserva(quarto, data_entrada, data_saida)
            return nova_reserva.reservar(quarto, lista_clientes)
            # return quarto.fazer_reserva(quarto, lista_clientes)
    
    return print("\nQuarto indisponível!")

def main(): 
    clientes = [] # Alterar para banco de dados
    quartos = [Quarto("1", True), Quarto("2", True), Quarto("3", True)] # Disponível?

    while True:
        opcao = menu()

        if opcao == 1:
            cadastrar_cliente(clientes)

        if opcao == 2:
            listar_clientes(clientes)

        if opcao == 3:
            escolher_quarto(quartos, clientes)
                    
        
        elif opcao == 9: 
            break

main()

