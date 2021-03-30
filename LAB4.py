# # Zad 1

# plik = open("liczby4.txt", "w")
# for i in range(200):
#     if i % 4 == 0:
#         plik.write(str(i)+"\n")
# plik.close()

# # Zad 2

# plik = open("liczby4.txt","r")
# wiersze = plik.readlines()
# print(wiersze)

# # Zad 3
# plik = open("tekst.txt","w")

# tekst = input("Podaj tekst do pliku: ")
# plik.write(tekst+"\n")
# plik.close()

# plik = open("tekst.txt","r")
# print(plik.readline())
# plik.close()

# # Zad 4

# class NaZakupy:
#     def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed

#     def WyswietlProdukt(self):
#         print("Nazwa Produktu: " + self.nazwa_produktu)
#         print("Ilosc Produktu: " + str(self.ilosc))
#         print("Jednostka Produktu: " + self.jednostka_miary)
#         print("Cena Produktu: " + str(self.cena_jed))

#     def ile_produktu(self):
#         print(str(self.ilosc) + " " + self.jednostka_miary)

#     def ile_kosztuje(self):
#         return self.ilosc*self.cena_jed

# Zad 6

# class Slowa():

#     slowo1 = "kajak"
#     slowo2 = "fajak"

#     def sprawdz_czy_palindrom(self,Slowo):
#        return Slowo == Slowo[::-1]
    
#     def sprawdz_czy_metagramy(self,slowo1,slowo2):
#         x = 0
#         for i in range (len(slowo1)):
#             if slowo1[i] != slowo2[i]:
#                 x+=1

#         if x > 1:
#             return False
#         else:
#             return True

#     def sprawdz_czy_anagramy(self,slowo1,slowo2):
#         if sorted(slowo1) == sorted(slowo2):
#             return True
#         else:
#             return False
    
#     def wyswietl_wyrazy(self):
#         print(self.slowo1)
#         print(self.slowo2)

# ob = Slowa()

# print(ob.sprawdz_czy_palindrom(ob.slowo1))
# print(ob.sprawdz_czy_metagramy(ob.slowo1,ob.slowo2))
# print(ob.sprawdz_czy_anagramy(ob.slowo1,ob.slowo2))
# ob.wyswietl_wyrazy()

# NoweZakupy = NaZakupy("Banan",4,"szt",2.99)
# NoweZakupy.WyswietlProdukt()
# NoweZakupy.ile_produktu()
# print(NoweZakupy.ile_kosztuje())

# # Zad 7

# class Robot:

#     def __init__(self,x,y,krok):
#         self.x = x
#         self.y = y
#         self.krok = krok

#     def idz_w_gore(self,ile_krokow):
#         self.x+=ile_krokow*self.krok

#     def idz_w_dol(self,ile_krokow):
#         self.x-=ile_krokow*self.krok

#     def idz_w_prawo(self,ile_krokow):
#         self.y+=ile_krokow*self.krok

#     def idz_w_lewo(self,ile_krokow):
#         self.y-=ile_krokow*self.krok
        
#     def pokaz_gdzie_jestes(self):
#         print("X: " + str(self.x))
#         print("Y: " + str(self.y))

#     def __del__(self):
#         print("Auto Destrukcja!")

# NowyRobot = Robot(0,0,1)
# NowyRobot.idz_w_prawo(1)
# NowyRobot.idz_w_prawo(1)
# NowyRobot.idz_w_dol(1)
# NowyRobot.idz_w_dol(1)
# NowyRobot.pokaz_gdzie_jestes()
