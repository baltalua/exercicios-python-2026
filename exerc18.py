valor = int(input("Insira o valor do seu deposito: "))
juros = int(input("insira a taxa de juros: "))
rend = (juros / 100)*valor
valorF = rend + valor

print(f"O rendimento é  {rend} e o valor depois do rendimento ´r {valorF}")