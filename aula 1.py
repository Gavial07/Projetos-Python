# --------- Dia 1 de python - Estou treinando e relembrando
#ex1
"""
 print('Olá, Mundo!')
nome = input('Qual o seu nome? ')
print("muito prazer {}!".format(nome))
"""
# --------- .format facilita na hora de escrever o código

#ex2
"""
n1 = int(input("Me de um numero: "))
n2 = int(input("Me de mais um numero: "))
s = n1 + n2
print('A soma do', n1,'mais',n2,'dá:', s)
print('A soma do {} mais o {} dá: {}'.format(n1,n2,s))
"""
#ex3
#n = input('ola')
#print(n.is...) --------- é um identificador da variável
"""
n = input('escreva o que quiser: ')
print('Esses são todos os dados disso que você escreveu:')
print('Qual seu tipo?', type(n))
print('Ele é um numero?', n.isnumeric())
print('Ele é uma letra?', n.isalpha())
print('Ele tem números e letras?', n.isalnum())
print('É possivel escreve-lo?', n.isprintable())
print('Ele está em caixa baixa?', n.islower())
print('Ele está em caixa alta?', n.isupper())
print('Ele possui maiusculo e minusculo?', n.istitle())
print('Ele é um espaço?', n.isspace())
"""
#ex4
"""
n1 = int(input('Me de um numero inteiro:'))
sucess = int(n1 + 1)
antess = int(n1 - 1)
print('Seu numero é {} \nSeu sucessor é {} \nSeu antecessor é {}'.format(n1,sucess,antess))
"""
#ex5
"""
n1 = float(input('Me de um numero:'))
dobro = n1 * 2
triplo = n1 * 3
rq = n1 **(1/2)
print('Essa é o número escolhido: {} \nEsse é o dobro dele: {} \nEsse é o triplo dele: {} \nEsse é sua raiz quadrada aproximada: {:<.4}'.format(n1,dobro,triplo,rq))
"""
#ex6
"""
np = float(input('Coloque a nota de portugues: '))
nm = float(input('Coloque a nota de matemática: '))
med = (np + nm)/2
print('Essa é a média de suas notas:', med)
"""
#ex7
"""
metros = float(input('Me dê uma medida em metros: '))
print('Essa é sua medida em centimetros: {} \nEssa é sua medida em milimetros: {}'.format(metros*100,metros*1000))
"""
#ex8
"""
n = int(input('Me dê um numero inteiro: '))
print("Essa é a tabuada desse numero:")
print("1 x {} = {}".format(n,n*1))
print("2 x {} = {}".format(n,n*2))
print("3 x {} = {}".format(n,n*3))
print("4 x {} = {}".format(n,n*4))
print("5 x {} = {}".format(n,n*5))
print("6 x {} = {}".format(n,n*6))
print("7 x {} = {}".format(n,n*7))
print("8 x {} = {}".format(n,n*8))
print("9 x {} = {}".format(n,n*9))
print("10 x {} = {}".format(n,n*10))
"""
#ex9
"""
d = float(input('Quantos reais você possui no banco? '))
print('Essa é a quantidade de dolares que você pode comprar: {}'.format(d/5.4))
"""
#ex10
"""
pa = float(input('Quantos metros de altura sua parede tem? '))
pl = float(input('Quantos metros de largura sua parede tem? '))
area = pa * pl
tn = area/2
print('A area de sua parede é {} e a quantidade de tinta necessária sera de {} baldes'.format(area,tn))
"""
#ex11
"""
preco = float(input('Qual o preço deste produto? '))
print('Esse é o preço dele com 5% de desconto:', preco - (preco * 5/100))
"""
#ex12
"""
salario = float(input('Qual é o seu salário? '))
print('Esse será seu salário após a mudança de 15%: {:.2f} reais'.format(salario + (salario*15/100)))
"""
#ex13
"""
tempc = float(input('Qual a temperatura em graus Celsius? '))
print('A temperatura em Firenhait é de {}°'.format(tempc*9/5 + 32))
"""
#ex14
"""
#kmcar = float(input('Quantos quilometros foram percorridos pelo carro? '))
#diascar = int(input('Por quantos dias você alugou ele? '))
#pag = (kmcar * 0.15 + 60 * diascar)
#print('Esse é o valor necessário para pagar: {} reais'.format(pag))
"""
#ex15
"""
#import random
#import math
#ran = float(input("me de um numero quebrado: "))
#print('Esse é o seu numero: {:.3f}'.format(ran))
#print('Esse é o seu numero inteiro: {}'.format(math.floor(ran)))
"""
#ex16
"""
#import math
#ca = float(input("Me de o valor do cateto adjacente: "))
#co = float(input('Me de o valor do cateto oposto: '))
#h = math.sqrt(ca ** 2 + co ** 2)
#print('Esse é o valor da hipotenusa:', h)
"""
#ex17
"""
#import math
#a = float(input('Me diga um angulo: '))
#sen = math.sin(math.radians(a))
#cos = math.cos(math.radians(a))
#tan = math.tan(math.radians(a))
#print('Esse é o valor do angulo em seno {} \ncosseno {} \ntangente {}'.format(sen,cos,tan))
"""
#ex19-20
"""
#import random
#import math
#a = str(input('Qual o nome do aluno? ' ))
#b = str(input('Qual o nome do aluno? ' ))
#c = str(input('Qual o nome do aluno? ' ))
#d = str(input('Qual o nome do aluno? ' ))
#lista = [a,b,c,d]
#random.shuffle(lista)
#print('Essa será a ordem de apresentação:')
#print(lista)
"""
#ex21
#import pygame
#pygame.init()
