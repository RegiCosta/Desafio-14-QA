import csv

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

class BibliotecaPessoal:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        if not self.livros:
            print("Sua biblioteca está vazia.")
        else:
            print("Lista de livros na sua biblioteca:")
            for i, livro in enumerate(self.livros, start=1):
                print(f"{i}. Título: {livro.titulo}, Autor: {livro.autor}, Ano de Publicação: {livro.ano_publicacao}")

    def salvar_para_csv(self, nome_arquivo):
        with open(nome_arquivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Título', 'Autor', 'Ano de Publicação'])
            for livro in self.livros:
                writer.writerow([livro.titulo, livro.autor, livro.ano_publicacao])

    def carregar_de_csv(self, nome_arquivo):
        with open(nome_arquivo, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Ignora cabeçalho
            for linha in reader:
                titulo, autor, ano_publicacao = linha
                livro = Livro(titulo, autor, ano_publicacao)
                self.adicionar_livro(livro)

def main():
    nome_arquivo = "biblioteca.csv"
    biblioteca = BibliotecaPessoal()
    biblioteca.carregar_de_csv(nome_arquivo)

    while True:
        print("\nBem-vindo à sua biblioteca pessoal!")
        print("Escolha uma opção:")
        print("1. Adicionar um novo livro")
        print("2. Visualizar lista de livros")
        print("3. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o nome do autor: ")
            ano_publicacao = input("Digite o ano de publicação: ")
            livro = Livro(titulo, autor, ano_publicacao)
            biblioteca.adicionar_livro(livro)
            print("Livro adicionado com sucesso!")
            biblioteca.salvar_para_csv(nome_arquivo)
        elif opcao == "2":
            biblioteca.listar_livros()
        elif opcao == "3":
            print("Obrigado por usar a biblioteca pessoal. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
