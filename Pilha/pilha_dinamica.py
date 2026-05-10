class No:
    def __init__(self, valor, proximo):
        self.prox = proximo
        self.info = valor
        
class Pilha_dinamica:
    def __init__(self):
        self.prim = None
        self.quant = 0

    def show(self):
        aux = self.prim
        while aux != None:
            print(aux.info, end=" ")
            aux = aux.prox
        print

    def push(self, valor):
        novo = No(valor, self.prim)
        self.prim = novo 
        self.quant += 1

    def pop(self):
        if self.quant == 0:
            return
        self.prim = self.prim.prox
        self.quant -= 1

    def get_topo(self):
        if self.quant == 0: return
        return self.prim.info
    
    def esta_vazia(self):
        return self.quant == 0
    