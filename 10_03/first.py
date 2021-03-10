# Zad 6

for i in range(51):
    if i % 5 == 0:
        print(i)

# Zad 7

x = input("Podaj liczby odzielone spacjami: ")
x = x.split()
for i in x:
    print(int(i)**2)

# Zad 8

lista = []
while(len(lista)<10):
    y = input("Podaj liczbe: ")
    lista.append(y)
print(lista)

#Zad 9

sum=0
z = input("Podaj liczbe: )
z = int(z)
while(z>0):
    sum+=z%10
    z=z//10
print(sum)