class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo

class Fila_Dinamica:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def inserir(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            novo = No(valor, None)
            self.ult.prox = novo
            self.ult = novo
        self.quant += 1

    def remover(self):
        if self.quant == 0:
            return
        if self.quant == 1:
            self.prim = self.ult = None
        else: 
            self.prim = self.prim.prox
        self.quant -= 1

    def ver_primeiro(self):
        if self.quant == 0:
            return
        return self.prim.info
    
    def esta_vazia(self):
        return self.quant == 0
    
    def show(self):
        if self.quant == 0:
            return
        aux = self.prim
        while aux != None:
            print(aux.info, end=' ')
            aux = aux.prox
        print()