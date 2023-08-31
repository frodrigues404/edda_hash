import csv

class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class AgendaHeroes:
    def __init__(self):
        self.tabela = [[] for _ in range(26)] # 26 letras do alfabeto 

    def calcular_indice(self, letra):
        return ord(letra.upper()) - ord('A') # Realiza a subtração do valor da letra na tabela ASCII pelo valor da letra A, assim os índices ficam entre 0 e 25

    def adicionar_contato(self, contato):
        indice = self.calcular_indice(contato.nome[0])
        self.tabela[indice].append(contato)

    def buscar_contato_por_nome(self, nome):
        indice = self.calcular_indice(nome[0])
        for contato in self.tabela[indice]:
            if contato.nome == nome:
                return contato
        return None

    def listar_contatos_por_letra(self, letra):
        indice = self.calcular_indice(letra)
        contatos = []
        for contato in self.tabela[indice]:
            contatos.append(contato)
        return contatos

    def remover_contato(self, nome):
        indice = self.calcular_indice(nome[0])
        for contato in self.tabela[indice]:
            if contato.nome == nome:
                self.tabela[indice].remove(contato)
                return True
        return False

    def importar_contatos(self, arquivo_csv):
        with open("agenda.csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    contato = Contato(row[0], row[1])
                    self.adicionar_contato(contato)

def menu_interativo():
    agenda = AgendaHeroes()
    agenda.importar_contatos('agenda.csv')

    while True:
        print("\nMenu:")
        print("1. Adicionar Contato")
        print("2. Buscar Contato por Nome")
        print("3. Listar Contatos por Letra")
        print("4. Remover Contato")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome do contato: ")
            telefone = input("Telefone do contato: ")
            contato = Contato(nome, telefone)
            agenda.adicionar_contato(contato)
            print("Contato adicionado com sucesso!")

        elif escolha == '2':
            nome = input("Digite o nome do contato que deseja buscar: ")
            contato = agenda.buscar_contato_por_nome(nome)
            if contato:
                print(f"Nome: {contato.nome}, Telefone: {contato.telefone}")
            else:
                print("Contato não encontrado.")

        elif escolha == '3':
            letra = input("Digite a letra para listar os contatos: ")
            contatos = agenda.listar_contatos_por_letra(letra)
            if contatos:
                for contato in contatos:
                    print(f"Nome: {contato.nome}, Telefone: {contato.telefone}")
            else:
                print("Nenhum contato encontrado com essa letra.")

        elif escolha == '4':
            nome = input("Digite o nome do contato que deseja remover: ")
            if agenda.remover_contato(nome):
                print("Contato removido com sucesso!")
            else:
                print("Contato não encontrado.")

        elif escolha == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_interativo()
