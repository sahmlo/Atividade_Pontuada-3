import os
os.system("clear")

matricula = int(input("Informe sua matrícula: "))
senha = int(input("Digite sua senha: "))
salario = float(input("Digite seu salário: "))
escolher_vt = input("Deseja receber o vale-transporte (S/N): ").lower()
valor_vr = float(input("Informe o valor do vale refeição: "))
dependentes = int(input("Informe a quantidade de dependentes: "))

def calcular_inss(salario):
    if salario <= 1320.00:
        desconto_inss = salario * 0.075
    elif 1320.01 <= salario <= 2571.29:
        desconto_inss = salario * 0.09
    elif 2571.30 <= salario <= 3856.94:
        desconto_inss = salario * 0.12
    elif 3856.95 <= salario <= 7507.49:
        desconto_inss = salario * 0.14
    else:
        desconto_inss = 7507.49 * 0.14
    return desconto_inss

def calcular_irrf(salario, dependentes):
    deducao_dependente = 189.59
    inss = calcular_inss(salario)
    salario_base = salario - inss - (dependentes * deducao_dependente)

    if salario_base <= 2112.00:
        desconto_irrf = 0
    if 2112.01 <= salario_base <= 2826.65:
        desconto_irrf = (salario_base * 0.075) 
    if 2826.66 <= salario_base <= 3751.05:
        desconto_irrf = (salario_base * 0.15)
    if 3751.06 <= salario_base <= 4664.68:
        desconto_irrf = (salario_base * 0.225) 
    if salario_base > 4664.68:
        desconto_irrf = (salario_base * 0.275)
    return desconto_irrf

def calcular_vale_transporte(salario, escolher_vt):
    if escolher_vt == "s":
        return salario * 0.06
    else:
        return 0

def calcular_vale_refeicao(valor_vr):
    return valor_vr * 0.20

def calcular_plano_saude(dependentes):
    desconto_dependente = 150
    return dependentes * desconto_dependente

inss = calcular_inss(salario)
irrf = calcular_irrf(salario, dependentes)
vt = calcular_vale_transporte(salario, escolher_vt)
vr = calcular_vale_refeicao(valor_vr)
plano_saude = calcular_plano_saude(dependentes)

desconto_salario = inss + irrf + vt + vr + plano_saude
salario_liquido = salario - desconto_salario

print("\nFolha de Pagamento")
print(f"\nDesconto do INSS: R$ {inss:.2f}")
print(f"Desconto do IRRF: R$ {irrf:.2f}")
print(f"Desconto do Vale Transporte: R$ {vt:.2f}")
print(f"Desconto do Plano de Saúde: R$ {plano_saude:.2f}")
print(f"Desconto do Vale Alimentação: R$ {vr:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")