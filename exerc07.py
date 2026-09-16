dis = input("Qual disciplina deseja saber a media? ")
nota1 = float(input("Qual a sua primeira nota? "))
nota2 = float(input("Agora a sua segunda nota? "))
nota3 = float(input("Agora a sua terceira nota? "))
nota4 = float(input("Agora a sua quarta nota? "))
result = 0

result = (nota1 + nota2 + nota3 + nota4) / 4

if (result >= 7):
  print (f"Aprovado!! Sua nota foi {result}")
else:
   print (f"Reprovado! Sua nota foi {result}")