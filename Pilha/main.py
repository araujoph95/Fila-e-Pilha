import Pilha_estatica

estacionamento = Pilha_estatica.pilha_estatica(10)
estacionamento_auxiliar = Pilha_estatica.pilha_estatica(10)

def processar_entrada(placa):
    if estacionamento.esta_cheia():
        print("O carro partiu sem entrar.")
    else:
        estacionamento.push({"placa": placa, "manobras": 0})
        print("Veículo entrou com sucesso.")

def processar_saida(placa):
    while not estacionamento.esta_vazia() and estacionamento.get_topo()["placa"] != placa:
        carro_bloqueio = estacionamento.get_topo()
        carro_bloqueio["manobras"] += 1
        estacionamento.pop()
        estacionamento_auxiliar.push(carro_bloqueio)
        print(f"Veículo {carro_bloqueio['placa']} manobrado para a rua.")

    if not estacionamento.esta_vazia():
        carro_cliente = estacionamento.get_topo()
        estacionamento.pop()
        print(f"Veículo saindo: {carro_cliente['placa']}. Manobras: {carro_cliente['manobras']}.")
    else:
        print(f"Veículo {placa} não encontrado.")

    while not estacionamento_auxiliar.esta_vazia():
        carro_retorno = estacionamento_auxiliar.get_topo()
        estacionamento.push(carro_retorno)
        estacionamento_auxiliar.pop()
        


print("--- Estacionamento Rua Direita (Palmas) ---")
print("Comandos: E [placa] para Entrada, S [placa] para Saída, F para Sair.")

while True:
    linha = input("Digite a operação: ").split()
    
    if not linha:
        continue
        
    comando = linha[0].upper()
    
    if comando == 'F':
        print("Encerrando programa...")
        break
        
    if len(linha) < 2:
        print("Erro: Digite a placa após o comando.")
        continue
    print()
        
    placa = linha[1]

    if comando == 'E':
        processar_entrada(placa)
    elif comando == 'S':
        processar_saida(placa)
    else:
        print("Comando inválido! Use E ou S.")
    
    print()


