class pilha_estatica:
    def __init__(self, tamanho):
        self.tam_maximo = tamanho
        self.vetor = [None] * tamanho
        self.quant = 0

    def show(self):
        if self.quant == 0:
            return
        for i in range(self.quant - 1, 0, -1):
            print(self.vetor[i], end=" ")
        print

    def push(self, valor):
        if self.quant >= self.tam_maximo:
            return
        self.vetor[self.quant] = valor
        self.quant += 1

    def pop(self):
        if self.quant == 0:
            return
        self.quant -= 1
        self.vetor[self.quant] = None

    def get_topo(self):
        return self.vetor[self.quant - 1]
    
    def esta_vazia(self):
        return self.quant == 0
    
    def esta_cheia(self):
        return self.quant == self.tam_maximo
    
    