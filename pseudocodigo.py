
#Exemplo
#Abaixo vemos o exemplo de um programa que faz a leitura de dez numeros e calcula a media dos numeros positivos:

"""
INICIO
VARIAVEIS
S,C,I,A,MD:Real;
S = 0;
C = 0;
PARA I de 1 ATE 10 FACA PASSO 1
    Escreva "Digite um numero: ";
    LEIA A;
    SE A >= 0 ENTAO
         S = S + A;
         C = C + 1;
    FIM SE;
FIM PARA;
MD = S / C;
ESCREVER ("A media e: ", MD);
FIM
"""


import time

S = 0
C = 0
A = None
MD = None


for i in range(0,10,1):
	A = raw_input("Digite um numero ")
	print("O numero eh, %s." % A)
	if A >= 0:
		S = float(S) + int(A)
		C = float(C) + 1
MD = S / C
print("A media eh %s" %MD)
