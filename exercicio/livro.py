from autor import Autor
# FUAQ implementa uma pilha de livro.
# Cada livro deverá conter o título, a quantidade de página e 
# o autor, sendo que o autor deverá conter nome, 
# e ano de nascimento.
# Implemente um método para adicionar livros na pilha,
# um método para imprimir a pilha de livros,
# um método para remover um livro da pilha 
# e um método que o usuário informa o nome do autor e 
# lhe é informado quantos livros tem na pilha com este autor




class Livro:

    def __init__(self, titulo, paginas = 0, autor = Autor()):
        self.titulo = titulo
        self.paginas = paginas
        self.autor = autor
        self.prox = None

    def __str__(self):
        txt = "\nTítulo: " + self.titulo
        txt += "\nPáginas: " + str ( self.paginas ) 
        txt += "\n" + str( self.autor )
        return txt  