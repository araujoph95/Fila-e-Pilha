from Fila_dinamica import Fila_Dinamica

class Fila_prioridade:
    def __init__(self):
        self.fila1 = Fila_Dinamica()
        self.fila2 = Fila_Dinamica()
        self.fila3 = Fila_Dinamica()
        self.fila4 = Fila_Dinamica()

    def inserir(self, valor, prioridade):
        if prioridade == 4:
            self.fila4.inserir(valor)
        elif prioridade == 3:
            self.fila3.inserir(valor)
        elif prioridade == 2:
            self.fila2.inserir(valor)
        elif prioridade == 1:
            self.fila1.inserir(valor)

    def remover(self):
        if not self.fila4.esta_vazia():
            self.fila4.remover()
        elif not self.fila3.esta_vazia():
            self.fila3.remover()
        elif not self.fila2.esta_vazia():
            self.fila2.remover()
        elif not self.fila1.esta_vazia():
            self.fila1.remover()

    def esta_vazia(self):
        return self.fila1.esta_vazia() and self.fila2.esta_vazia() and self.fila3.esta_vazia() and self.fila4.esta_vazia()
    
    def show(self):
        self.fila4.show()
        self.fila3.show()
        self.fila2.show()
        self.fila1.show()