valor_sapatos = float(input("Digite um valor para um par de sapatos em reais:"))
desconto = float(input("Digite uma porcentagem de desconto:"))

preco_final_com_desconto_aplicado_em_reais = valor_sapatos * (1 - desconto/100)

print(f"O preço do par de sapatos com desconto aplicado é de: R${preco_final_com_desconto_aplicado_em_reais:.2f}")
