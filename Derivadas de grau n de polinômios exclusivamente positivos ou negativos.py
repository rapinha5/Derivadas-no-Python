
from math import sqrt
GM = int(input("Qual o grau máximo da sua função? ")) #Grau Máximo da função (positivo ou negativo)
QD = int(input("Quantas vezes você quer derivar a função? ")) #Quantidade de derivadas da função
tcP = 0
# LISTAS:
NpEq = list() #Número puro da Equação
NeEq = list() #Número elevante da Equação
FnDer = list() #Função n Derivada
FenDer = list() #A parte que subtrai os elevados

# FUNÇÕES PERSONALIZADAS
def AdX(x): #Adicionadora de X (caso você queira adicionar X ao lado do valor puro, EX: [2.0 , 3.0] [2.0 , 1.0] --> 2X² 3X¹
    return "{}X^{}".format(x , Tcp)
def Der(x): #Derivação na parte das "bases"/números puros
        return NpEq[x] * NeEq[x]
def El(x): #A parte que subtrai em 1 a potência
        return NeEq[x] -1

TCP = 0
if GM >= 0:
    Tcp = GM+1
else: Tcp = GM-1
while TCP<=sqrt(GM*GM):
    TCP = TCP+1
    if GM >= 0:
         Tcp = Tcp-1
    else:
         Tcp = Tcp+1
    FpxF = float(input("Qual o fator na posição {} da função? ".format(TCP))) #Fator na posição x da Função
    NpEq.insert(TCP , FpxF)
    NeEq.insert(TCP , Tcp)
print(TCP , Tcp , NpEq , NeEq) #Só pra análise. Completamente descartável
TCP = 0
while TCP<sqrt(QD*QD):
    TCP=TCP+1
    tcP = 1
    for tcP in range(0 , len(NpEq)-1):
        FnDer.insert(tcP , Der(tcP))
        FenDer.insert(tcP , El(tcP))
        tcP = tcP +1
    NpEq = FnDer
    NeEq = FenDer
    FnDer = list()
    FenDer = list()
print(TCP , Tcp , NpEq , FnDer , NeEq, FenDer)
if NpEq == []:
     print ("Derivada é 0")
else:
     print ("Derivada é {} multiplicado por 'X' elevado a {}".format(NpEq , NeEq)) 
#OBS: Só funciona pra polinômios de grau exclusivamente positivos ou exclusivamente negativos.
