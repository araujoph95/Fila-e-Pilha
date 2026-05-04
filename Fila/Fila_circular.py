class Fila_Circular:
    def __init__(self, tamanho):
        self.tam = tamanho
        self.vetor = [None] * tamanho
        self.quant = 0
        self.inicio = 0
        self.fim = -1


    def inserir(self, valor):
        if self.quant >= self.tam:
            return
        self.fim = (self.fim + 1) % self.tam
        self.vetor[self.fim] = valor
        self.quant += 1
    
    def remover(self):
        if self.quant == 0:
            return
        self.vetor[self.inicio] = None
        self.inicio = (self.inicio + 1) % self.tam
        self.quant -= 1

    def show(self):
        if self.quant == 0:
            return
        for i in range(self.quant):
            print(self.vetor[(self.inicio + i) % self.tam], end=' ')
        print()

    def esta_vazia(self):
        return self.quant == 0
    
    def esta_cheia(self):
        return self.quant == self.tam
    
    def ver_primeiro(self):
        return self.vetor[self.inicio]
    