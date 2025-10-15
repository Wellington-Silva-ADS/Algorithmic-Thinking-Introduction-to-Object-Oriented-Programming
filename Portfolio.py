import csv  # Biblioteca para gerar o arquivo CSV

print("Bem-vindo à R.M Imóveis - Sistema de Orçamento\n")

# Validação do tipo de imóvel
while True:
    tipo = input("Digite o tipo de imóvel (apartamento, casa, estudio): ").lower()
    if tipo in ["apartamento", "casa", "estudio"]:
        break
    else:
        print("Tipo inválido! Digite 'apartamento', 'casa' ou 'estudio'.\n")

# Validação do número de quartos — SOMENTE para apartamento ou casa
if tipo in ["apartamento", "casa"]:
    while True:
        try:
            quartos = int(input("Quantos quartos? (1 ou 2): "))
            if quartos in [1, 2]:
                break
            else:
                print("Informe apenas 1 ou 2 quartos.\n")
        except ValueError:
            print("Digite um número válido (1 ou 2).\n")
else:
    # Para estúdio, define automaticamente como 1 quarto
    quartos = 1

# Pergunta sobre crianças — SOMENTE para apartamentos
if tipo == "apartamento":
    while True:
        tem_criancas = input("Possui crianças? (s/n): ").lower()
        if tem_criancas in ["s", "n"]:
            break
        else:
            print("Responda apenas com 's' para sim ou 'n' para não.\n")
else:
    tem_criancas = "n"  # padrão neutro, sem efeito no cálculo

# Validação de vaga de garagem
while True:
    vaga = input("Deseja vaga de garagem/estacionamento? (s/n): ").lower()
    if vaga in ["s", "n"]:
        break
    else:
        print("Responda apenas com 's' ou 'n'.\n")

# Atribuição de valor base do imóvel
if tipo == "apartamento":
    aluguel = 700
elif tipo == "casa":
    aluguel = 900
elif tipo == "estudio":
    aluguel = 1200

# Acréscimos por número de quartos
if tipo == "apartamento" and quartos == 2:
    aluguel += 200
elif tipo == "casa" and quartos == 2:
    aluguel += 250

# Vagas de garagem ou estacionamento
if vaga == "s":
    if tipo in ["apartamento", "casa"]:
        aluguel += 300
    elif tipo == "estudio":
        while True:
            try:
                vagas_extra = int(input("Quantas vagas extras (além das 2 inclusas)? "))
                if vagas_extra >= 0:
                    aluguel += 250 + (vagas_extra * 60)
                    break
                else:
                    print("Digite um número maior ou igual a zero.\n")
            except ValueError:
                print("Digite um número válido.\n")

# Desconto para quem não tem crianças (apenas apartamentos)
if tipo == "apartamento" and tem_criancas == "n":
    desconto = aluguel * 0.05
    aluguel -= desconto

# Valor do contrato e forma de parcelamento
valor_contrato = 2000

while True:
    try:
        parcelas_contrato = int(input("Deseja dividir o contrato em quantas vezes? (1-5): "))
        if 1 <= parcelas_contrato <= 5:
            valor_parcela_contrato = valor_contrato / parcelas_contrato
            break
        else:
            print("Digite um número entre 1 e 5.\n")
    except ValueError:
        print("Digite um número válido.\n")

# Exibição do resultado final
print("\n ORÇAMENTO GERADO:")
print(f"Tipo de imóvel: {tipo.capitalize()}")
print(f"Quartos: {quartos}")
print(f"Valor do aluguel mensal: R$ {aluguel:.2f}")
print(f"Valor total do contrato: R$ {valor_contrato:.2f}")
print(f"Parcelado em {parcelas_contrato}x de R$ {valor_parcela_contrato:.2f}")

# Geração do arquivo CSV
with open("orcamento_imobiliario.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Parcela", "Valor (R$)"])
    for mes in range(1, 13):
        escritor.writerow([mes, f"{aluguel:.2f}"])

print("\n Arquivo 'orcamento_imobiliario.csv' gerado com sucesso!")
