# # Zad 1

# class Material:
#     def __init__(self, rodzaj, dlugosc, szerokosc):
#         self.rodzaj=rodzaj 
#         self.dlugosc=dlugosc
#         self.szerokosc=szerokosc

#     def wyswietl_nazwe(self):
#         print(__class__.__name__)

# class Ubrania(Material):
#     rozmiar=34 
#     kolor="Czerwony"
#     dla_kogo="Meski"
#     def wyswietl_dane(self):
#         print("Rozmiar: " + str(self.rozmiar))
#         print("Kolor: " + str(self.kolor))
#         print("Dla kogo: " + str(self.dla_kogo))

# class Sweter(Ubrania):
#     rodzaj_swetra = "Rozpinany"
#     def wyswietl_dane(self):
#         print("Rodzaj swetra: " + self.rodzaj_swetra)




# NowySweter = Sweter("Bawelna",23,40)
# NowySweter.wyswietl_dane()
# NowySweter.wyswietl_nazwe()
# # Ubranie = Ubrania(34,"Czerwony","Meska")
# # Ubranie.wyswietl_dane()

# # Nowa = Material("bawelna",5,8)
# # Nowa.wyswietl_nazwe()

# # # Zad 2

# class Ksztalty:
#     # definicja konstruktora
#     def __init__(self, x, y):
#         # deklarujemy atrybuty
#         # self wskazuje że chodzi o zmienne właśnie definiowanej klasy
#         self.x=x 
#         self.y=y
#         self.opis = "To będzie klasa dla ogólnych kształtów"

#     def pole(self):
#         return self.x * self.y

#     def obwod(self):
#         return 2 * self.x + 2 * self.y

#     def dodaj_opis(self, text):
#         self.opis = text

#     def skalowanie(self, czynnik):
#         self.x = self.x * czynnik
#         self.x = self.y * czynnik


# class Kwadrat(Ksztalty):

#     def __init__(self, x):
#         self.x = x
#         self.y = x

#     def __add__(self, other):
#         return Kwadrat(self.x + other.x)
#     def __ge__(self, other):
#         return Kwadrat(self.x)

# # NowyKwadrat = Kwadrat(5)+Kwadrat(5)
# # print(NowyKwadrat.x)

# # Zad 3 

# KwadPorow = Kwadrat(4)>=Kwadrat(2)
# print(KwadPorow.x)

# # Zad 4

# class Point:
#     counter = []

#     def __init__(self, x=0, y=0):
#         """Konstruktor punktu."""
#         self.x = x
#         self.y = y

#     def update(self, n):
#         self.counter.append(n)

# p1 = Point(0,0)
# p2 = Point(1,1)
# p3 = Point(5,2)
# p4 = Point(0,1)

# print(p1.counter)
# p1.update(1)
# print(p3.counter)
# p2.counter.append(2)
# print(p2.counter)
# p1.counter[0]=2
# print(p1.counter)
# p1.update(4)
# print(p2.counter)

# # Zad 5

# class Osoba:

#     def __init__(self, imie, nazwisko):
#         self.imie = imie
#         self.nazwisko = nazwisko

#     def przedstaw_sie(self):
#         return "{} {}".format(self.imie, self.nazwisko)


# class Pracownik(Osoba):

#     def __init__(self, imie, nazwisko, pensja):
#         Osoba.__init__(self, imie, nazwisko)
#         # lub
#         # super().__init__(imie, nazwisko)
#         self.pensja = pensja

#     def przedstaw_sie(self):
#         return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


# class Menadzer(Pracownik):

#     def przedstaw_sie(self):
#         return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


# jozek = Pracownik("Józek", "Bajka", 2000)
# adrian = Menadzer("Adrian", "Mikulski", 12000)

# print(jozek.przedstaw_sie())
# print(adrian.przedstaw_sie())
# print(isinstance(jozek, Menadzer))
# print(isinstance(jozek, Pracownik))
# print(isinstance(jozek, Osoba))

# print(issubclass(Menadzer, Osoba))
# print(issubclass(Menadzer,Pracownik))

# # Zad 6

# class Wspak:
#     """Iterator zwracający wartości w odwróconym porządku"""
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]

# Tablica = [1,2,3,4,5,6,7,8,9,0]

# for i in Wspak(Tablica):
#     print(i)

# # Zad 7

# class Patrzyste:
#     def __init__(self, data):
#         self.data = data
#         self.index = -2

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.index += 2
#         if self.index >= len(self.data)-1:
#             raise StopIteration
#         return self.data[self.index]

# Tablica = "Testowy Tekst"

# # Zad 8


# class Samogloski:

#     def __init__(self, data):

#         self.result = [] 
#         self.data = data
#         self.index = -1
#         if(not isinstance(self.data,str)):
#             print("The object isnt string!")
#         else:
#             for letter in data:
#                 if letter in 'aeiouy':
#                     self.result.append(letter)
#     def __iter__(self):

#             return self

#     def __next__(self):
#         self.index += 1
#         if self.index > len(self.result)-1:
#             raise StopIteration
#         return self.result[self.index]

# Test2 = 2348
# Test = "The quick brown fox jumped over lazy dog"
# for i in Samogloski(Test):
#     print(i)
# for i in Samogloski(Test2):
#     print(i)
