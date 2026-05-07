import Fila_prioridades

fila = Fila_prioridades.Fila_prioridade()
print("=== TESTE DE INSERÇÃO ===")


fila.inserir("pessoa1", 1)
fila.inserir("idoso1", 4)
fila.inserir("deficiente1", 2)
fila.inserir("grávida1", 3)
fila.inserir("idoso2", 4)


print("Estado inicial das filas (Prioridade 4 para 1):")
fila.show()
print("-" * 40)
print("\n=== TESTE DE REMOÇÃO HIERÁRQUICA ===")


for i in range(1, 5):
    print(f"Remoção nº {i}:")
    fila.remover()
    fila.show()
    print("---")

print("\n=== VERIFICAR SE ESTÁ VAZIA ===")
if fila.esta_vazia():
    print("A fila está vazia.")
else:
    print(f"A fila ainda contém elementos. Status atual:")
    fila.show()


print("\nLimpando o restante da fila...")
while not fila.esta_vazia():
    fila.remover()

print(f"Fila finalizada. Está vazia? {fila.esta_vazia()}")