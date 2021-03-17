import random
# # Zad 6

# for i in range(51):
#     if i % 5 == 0:
#         print(i)

# # Zad 7

# x = input("Podaj liczby odzielone spacjami: ")
# x = x.split()
# for i in x:
#     print(int(i)**2)

# # Zad 8

# lista = []
# while(len(lista)<10):
#     y = input("Podaj liczbe: ")
#     lista.append(y)
# print(lista)

# # Zad 9

# sum=0
# z = input("Podaj liczbe: )
# z = int(z)
# while(z>0):
#     sum+=z%10
#     z=z//10
# print(sum)

# # Zad 10

# z = input("Podaj liczbe: ")
# z = int(z)
# n = 0
# while(n<=z):
#     for i in range(n):
#         print("A", end="")
#     print()
#     n += 1

# # Zad 11

# n = input("Podaj liczbe: ")
# n = int(n)
# for a1 in range(1, (n+1)//2 + 1): 
#     for a2 in range((n+1)//2 - a1):
#         print(" ", end = "")
#     for a3 in range((a1*2)-1):
#         print("o", end = "")
#     print()

# for a1 in range((n+1)//2 + 1, n + 1): 
#     for a2 in range(a1 - (n+1)//2):
#         print(" ", end = "")
#     for a3 in range((n+1 - a1)*2 - 1):
#         print("o", end = "")
#     print()

# # Zad 12

# for w in range(1,11):
#     for h in range(1,11):
#         print(str(w*h)+" ",end="")
#         if w*h<10:
#             print(" ",end="")
#     print()

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