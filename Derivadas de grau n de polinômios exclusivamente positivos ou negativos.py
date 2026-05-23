#Faz função recebe dois parâmetros, uma sendo um uma função polinomial e o outro sendo a quantidade de derivações que essa função vai receber.

#IDEIA: Input de grau máximo da função --> Quantindade de valores numéricos (os que multiplicam as incógnitas) que devem ser adicionados.
#Pode ter a ver com um valor while: Enquanto TCP<=GrauMáximo+1 --> Adiciona um valor numérico numa memória (n+1)
from math import sqrt
GM = int(input("Qual o grau máximo da sua função? "))
QD = int(input("Quantas vezes você quer derivar a função? "))
tcP = 0
# LISTAS:
NpEq = list()
NeEq = list()
FnDer = list()
FenDer = list()

# FUNÇÕES PERSONALIZADAS
def AdX(x):
    return "{}X^{}".format(x , Tcp)
def Der(x):
        return NpEq[x] * NeEq[x]
def El(x):
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
    FpxF = float(input("Qual o fator na posição {} da função? ".format(TCP)))
    NpEq.insert(TCP , FpxF)
    NeEq.insert(TCP , Tcp)
print(TCP , Tcp , NpEq , NeEq)
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