class Fila_Estatica:
    def __init__(self, tamanho):
        self.tam = tamanho
        self.vetor = [None] * tamanho
        self.quant = 0

    def inserir(self, valor):
        if self.quant >= self.tam:
            return
        else:
            self.vetor[self.quant] = valor
            self.quant += 1

    def remover(self):
        if self.quant == 0:
            return
        else:
            for i in range(self.quant - 1):
                self.vetor[i] = self.vetor[i + 1]
            self.quant -= 1

    def ver_primeiro(self):
        return self.vetor[0]
    
    def esta_vazia(self):
        return self.quant == 0
    
    def esta_cheia(self):
        return self.quant == self.tam
    