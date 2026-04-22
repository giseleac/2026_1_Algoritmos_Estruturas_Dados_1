from Pilha import Pilha
from autor import Autor
from livro import Livro

lifo = Pilha()
lifo.imprimir()

a1 = Autor( "Machado de Assis", 1938 )
a2 = Autor( "Érico Veríssimo", 1905 ) 

l1 = Livro( "Dom Casmurro", 288, a1)
l2 = Livro( "O tempo e o vento", 2832, a2)
l3 = Livro( "Viva a vida" )
l4 = Livro( "Memórias Póstumas de Brás Cubas", 85 , a1)

lifo.add( l1 )
lifo.add( l3 )
lifo.add( l2 )
lifo.remover()
lifo.add( l4 )

lifo.contLivrosPorAutor("Adalto")
lifo.contLivrosPorAutor("Machado de Assis")