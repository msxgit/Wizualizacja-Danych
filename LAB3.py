
import random

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