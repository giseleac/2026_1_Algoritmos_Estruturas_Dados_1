<<<<<<< HEAD
from No import No

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self,valor):
        nodo = No(valor)
        if self.inicio is None:
            self.inicio = nodo
            self.fim = nodo
        else:
            self.fim.prox = nodo 
        self.fim = nodo 
        self.imprimir() 

    def imprimir(self):
        print("----------------------------") 
        print("Fila - Fifo")
        if self.inicio is None:
            print("Fila Vazia!") 
        else:
            aux = self.inicio
            txt = ""
            while aux:
                txt += aux.dado + " - "
                aux = aux.prox  
            print(txt)

    def remover(self):
        if self.inicio is not None:
            self.inicio = self.inicio.prox
            if self.inicio is None:
                self.fim = None 
            print("Elemento removido!")                           
=======
from No import No

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self,valor):
        nodo = No(valor)
        if self.inicio is None:
            self.inicio = nodo
            self.fim = nodo
        else:
            self.fim.prox = nodo 
        self.fim = nodo 
        self.imprimir() 

    def imprimir(self):
        print("----------------------------") 
        print("Fila - Fifo")
        if self.inicio is None:
            print("Fila Vazia!") 
        else:
            aux = self.inicio
            txt = ""
            while aux:
                txt += aux.dado + " - "
                aux = aux.prox  
            print(txt)

    def remover(self):
        if self.inicio is not None:
            self.inicio = self.inicio.prox
            if self.inicio is None:
                self.fim = None 
            print("Elemento removido!")                           
>>>>>>> ad64d8c20954833b3b992bf5f201ccaa5d429ae9
        self.imprimir()        