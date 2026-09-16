num1 = int(input("Digite o 1° numero "))
num2 = int(input("Digite o 2° numero "))
operação = input("Você deseja Soma(+) ou Subtração(-)")
result = 0

if (operação == "-"):
  result = num1 - num2
else:
  result = num1 + num2
print(result)