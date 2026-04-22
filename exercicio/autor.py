class Autor: #class Autor vai ser um objeto de livro. Uma subclass.

    def __init__(self, nome = "Sem nome", ano = 2020): #Se eu for colocar um valor default, sempre tem que ser do último indo para dentro(da direita para a esquerda) e nunca colocar um valor default no meio.
        self._nome = nome #um underline é fracamento protegido não deve ser acessado fora da classe.
        self.__ano = ano  #com 2 undeline é fortemente protegido(privado): O atributo não pode ser acessado diretamente fora da classe com o mesmo nome.

    def setNome(self, valor):
        if valor != "" and valor != "Adalto":
            self._nome = valor

    def getNome(self):
        return self._nome


    @property #Define o getter e transforma o método em atributo
    def ano(self):
        return self.__ano

    @ano.setter #Define o setter
    def ano(self, valor):
        if valor < 2026:
            self.__ano = valor             

    #Com o @property e o @ano.setter você protege o atributo sem mudar a forma de uso.

    def __str__(self):
        txt = "Autor: " + self._nome
        txt += " - Ano: " + str( self.__ano )
        return txt