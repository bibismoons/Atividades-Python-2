valor_da_hora_aula = float(input("Digite o valor da hora-aula:"))
numero_de_aulas_dadas_no_mes = int(input("Digite a quantidade de aulas dadas no mês:"))
percentual_de_desconto_do_INSS = float(input("Digite o percentual de desconto do INSS:"))

salario_bruto = valor_da_hora_aula * numero_de_aulas_dadas_no_mes 
desconto_INSS = salario_bruto * (percentual_de_desconto_do_INSS/100)
salario_liquido = salario_bruto - desconto_INSS

print(f"O salário líquido de um professor é de: R${salario_liquido:.2f}")