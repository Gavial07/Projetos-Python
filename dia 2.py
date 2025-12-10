#Ex 22
"""
nome = str(input('Me de seu nome bebe: '))
ns = nome.split()
print('Seu nome em maiusculo {}'.format(nome.upper()))
print('Seu nome em minusculo {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome)))
print('Seu primeiro nome tem {} letras'.format(len(ns[0])))
"""

#Ex 23
"""
import random
num = str(random.randint(0,9999))
print("Esse é o numero: ", num)
print('Essa é o milhar: ', num[0])
print('Essa é a centena: ', num[1])
print('Essa é a dezena: ', num[2])
print('Essa é a unidade: ', num[3])
"""

#ex24
"""
nomec = str(input("Me de o nome de uma cidade: "))
nomemin = nomec.lower()
ns = nomemin.split()
if ns[0] == 'santo': print("Sua cidade começa com santo")
else: print('Sua cidade não começa com santo')
"""

#Ex25
"""
nome = str(input('Me de seu nome: '))
nomem = nome.lower()
if 'silva' in nomem: print('Seu nome possui silva')
else: print('Seu nome não possui silva')
"""

#Ex26
"""
frase = str(input('Escreva uma frase: '))
frase.rfind('a')
print('Sua frase possui {} letras a'.format(frase.count('a')))
print('A letra a aparece primeiramente em: {} caracter'.format(frase.find('a')))
print('A letra a aparece ultimamente em: {} caracter'.format(frase.rfind('a')))
"""

#Ex27
"""
nome = str(input('Escreva seu nome inteiro: '))
nm = nome.split()
print('Esse é o seu primeiro nome: ', nm[0])
print('Esse é o seu ultimo nome: ', nm[len(nm)-1])
"""
#Ex28
"""
import random
num = random.randint(0,5)
na = int(input('Qual o numero que o pc pensou, de 0 a 5? '))
print("O pc pensou no {} e você colocou {}".format(num,na))
if num == na: print('você acertou')
else: print('você errou')
"""
#Ex29
"""
km = float(input('Quantos km por hora seu carro está? '))
if km >= 80:
    multa = (km -80) * 7
    print('Você foi multado por velocidade terá que pagar: ', multa)
else:
    print('Você não foi multado')
"""
#Ex30
"""
n = int(input('Me diga um numero: '))
if n%2 == 0:
    print('Seu numero é par')
else: print('Seu numero é impar')
"""
#Ex31
"""
km = float(input('Me diga a distancia em km da sua viagem: '))
if km >= 201: print('você terá que me pagar: {} reais'.format(km * 0.45))
if km <= 200: print('você terá que me pagar: {} reais'.format(km * 0.5))
"""
#Ex32
"""
ano = int(input('me diga um ano:'))
if ano%4 == 0: print('seu ano é bissexto')
else: print('seu ano não é bissexto')
"""
#Ex33
"""
n1 = int(input('me de um numero: '))
n2 = int(input('me de um numero: '))
n3 = int(input('me de um numero: '))
maior = n1
if n2 > maior: maior = n2
if n3 > maior: maior = n3
menor = n1
if n2 < menor: menor = n2
if n3 < menor: menor = n3
print('Esse é o maior numero {} e esse é o menor {}'.format(maior, menor))
"""
#Ex34
"""
salario = float(input('Me de seu salario: '))
if salario <= 1250:
    sa = salario * 110/100
    print("Esse é o seu salario depois do aumento:", sa)
if salario >= 1250:
    sa = salario * 115/100
    print("Esse é o seu salario depois do aumento:", sa)
"""
#Ex35
"""
r1 = float(input('Me de uma medida para lado 1: '))
r2 = float(input('Me de uma medida para lado 2: '))
r3 = float(input('Me de uma medida para lado 3: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1: print('Suas medidas formam um triangulo')
else: print('Suas medidas não formam um triangulo')
"""
