
import random
import math as m

# # Zad 1 

# A = [ 1/x for x in range(1,11)]
# print(A)
# B = [ 2**x for x in range(0,11)]
# print(B)
# C = [ x for x in range(0,200) if x % 4 == 0]
# print(C)

# # Zad 2

# random.seed(1)
# ListMatrix = [[random.randint(1,15),random.randint(1,15),random.randint(1,15),random.randint(1,15)] for x in range(4)]
# ListMatrixDia = [ListMatrix[x][x] for x in range(4)]
# print(ListMatrix)
# print(ListMatrixDia)

# # Zad 3

# Lista = {"Banan": "kg", "Ser": "kg", "Cebula": "sztuki", "Szynka": "dkg"}
# Nowa = [value for key,value in Lista.items()]
# print(Nowa)

# # Zad 4

# def monotonicznosc(a):
#     if a>0:
#         return "Funkcja rosnaca"
#     elif a==0:
#         return "Funkcja stala"
#     else:
#         return "Funkcja malejaca"

# print(monotonicznosc(0,3))

# # Zad 5

# def Lines(a1,a2):
#     if(a1==a2):
#         return "Równoległe"
#     if(a1*a2==-1):
#         return "Prostopadłe"

# print(Lines(1,-1))

# # Zad 6

# def Radius(x=3,y=2,a=0,b=0):
#     return m.sqrt((x-a)**2+(y-b)**2)

# print(Radius(3,10))

# # Zad 7

# def Pitago(a=3,b=4):
#     return m.sqrt(a**2+b**2)

# print(Pitago())

# # Zad 8

# def ciag(a1=1,r=1,ile=10):
#     suma = 0
#     for i in range(0,ile):
#       suma += a1+r*i
#     return suma
# print(ciag())

# # Zad 9

# # symbol * oznacza dowolną ilość argumentów przechowywanych w krotce
# def ciag(* liczby):
#     # jeżeli nie ma argumentów to
#     if len(liczby) == 0:
#         return 0.0
#     else:
#         suma = liczby[0]
#     # sumujemy elementy ciągu
#     for i in range(1,len(liczby)):
#         suma *= liczby[i]
#     # zwracamy wartość sumy
#     return suma

# # wywołanie gdy brak argumentów
# print(ciag())
# # podajemy argumenty
# print(ciag(1,2,3,4,5,6,7,8))

# # Zad 10

# def Produkty(** rzeczy):
#     Nowa = [value for key,value in rzeczy.items()]
#     sum = 0
#     for element in Nowa:
#         sum += element
#     return sum

# print(Produkty(czekolada=4, baton=10, banan=3))

# Zad 11

import dni_tygodnia as dni

print(dni.NrDoDnia(3))
print(dni.KtoryDzien(13))