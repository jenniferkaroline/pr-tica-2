def maior(a, b):
  if a > b:
    print(a)
  else:
    print(b)

a = int(input("me dê um número: "))
b = int(input("me dê um segundo número: "))
maior(a, b)

numero = int(input("me dê um número: "))
if numero > 0:
  print("positivo! ")
if numero < 0:
  print("negativo! ")
if numero == 0:
  print("neutro! ")

sexo = input("qual o seu gênero? ")
if sexo == "F":
  print("feminino! ")
if sexo == "M":
  print("masculino! ")
else:
  print("não binário! ")

L = ['a','e','i','o','u','A','E','I','O','U']
letra = input("digite uma letra: ")
if letra in L:
  print("vogal! ")
else:
  print("consoante! ")

turno = input("em que turno você estuda? ")
if turno == "M":
  print("bom dia, boa aula! ")
if turno == "V":
  print("boa tarde, boa aula! ")
if turno == "N":
  print("boa noite, boa aula! ")
else:
  print("valor inválido... ")



