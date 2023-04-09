# ENTRADA(S)
altura = float(input("Digite a altura da caixa d' água que tem a forma de um paralelepípedo retângulo em metros:"))
largura = float(input("Digite a largura da mesma caixa:"))
profundidade = float(input("Digite a profundidade da mesma caixa:"))

# PROCESSAMENTO
volume = altura * largura * profundidade
capacidade_L = volume * 1000

# SAÍDA
print(f"A capacidade em litros é de: {capacidade_L}L")