import sys
# zadanie 1
tekst = input("Twój tekst: \n")
print(f'Ilosc spacji: {tekst.count(" ")}')
print("Podaj liczbe pierwsza:")
a = sys.stdin.readline()
print("Podaj liczbe druga:")
b = sys.stdin.readline()
sys.stdout.write(f"{int(a)*int(b)}")
