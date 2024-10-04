from datetime import datetime
from re import sub

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
        return f"Cliente: {self.nome} | CPF: ***{self.cpf[4:11]}** | Data de Nascimento: {self.data_nascimento}" # ***.{str(self.cpf)[4:11]}-**

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
            return f"Quarto {self.numero}: Indisponível" # até {data_saida}"

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
    try:    
        cpf = sub(r'\D', '', input("Digite seu CPF (apenas numeros): "))

        if len(cpf) != 11:
            return print("Digite um CPF válido!")
        
        cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

        for cliente in lista_clientes:
            if cliente.cpf == cpf:
                return print("\nErro! Esse CPF já está cadastrado")
            
        nome = str(input("Nome: "))
        data_nascimento = datetime.strptime(str(input("Data de nascimento (dd/mm/aaaa): ")), '%d/%m/%Y').date()
        data_nascimento = data_nascimento.strftime('%d/%m/%Y')
        cliente = Cliente(nome=nome, data_nascimento=data_nascimento, cpf=cpf)

    except ValueError:
        print("Por favor, insira valores válidos!")
        return
    
    lista_clientes.append(cliente)
    return

def listar_clientes(lista_clientes):
    if len(lista_clientes) == 0:
            return print("--Nenhum cliente cadastrado--")
    
    for cliente in lista_clientes:
        return print(cliente.__repr__())

def menu():
    opcoes = """
----MENU----
[1] Fazer cadastro
[2] Listar clientes
[3] Fazer reserva

[9] Sair

Digite sua opção: """
    return int(input(opcoes))

def escolher_quarto(lista_quartos, lista_clientes, lista_reservas):
    print("-----QUARTOS------\n")
    i = 0
    for quarto in lista_quartos:
        print(f"{lista_quartos[i].mostrar_disponibilidade()}", end=" ")
        for reserva in lista_reservas:
            if reserva.quarto == quarto:
                print(f"até {reserva.data_saida}")
        i+=1
        print('\n')
    print('------------------')

    quarto_escolhido = str(input("Digite o número do quarto que deseja se hospedar: "))
    data_entrada = datetime.strptime(str(input("Digite a data do check-in (DD/MM/AAAA): ")), '%d/%m/%Y').date()
    data_saida = datetime.strptime(str(input("Digite a data do check-out (DD/MM/AAAA): ")), '%d/%m/%Y').date()
    data_entrada = data_entrada.strftime('%d/%m/%Y')
    data_saida = data_saida.strftime('%d/%m/%Y')

    for quarto in lista_quartos:
        if quarto_escolhido == quarto.numero and quarto.disponibilidade == True:
            nova_reserva = Reserva(quarto, data_entrada, data_saida)
            lista_reservas.append(nova_reserva)
            return nova_reserva.reservar(quarto, lista_clientes)
            # return quarto.fazer_reserva(quarto, lista_clientes)
    
    return print("\nQuarto indisponível!")

def main(): 
    clientes = [] # Alterar para banco de dados
    reservas = []
    quartos = [Quarto("1", True), Quarto("2", True), Quarto("3", True)] # Disponível?

    while True:
        opcao = menu()

        if opcao == 1:
                cadastrar_cliente(clientes)

        if opcao == 2:
            listar_clientes(clientes)

        if opcao == 3:
            escolher_quarto(quartos, clientes, reservas)
                    
        
        elif opcao == 9: 
            break

main()

