#Zad 1
n = int(input())

if n % 3 == 0:
  print("TAK")
else:
  print("NIE")

#Zad 2
a = int(input())
if a>=100 and a<1000 and  a % 17 == 0:
  print("TAK")
else:
  print("NIE")

#Zad3
a = int(input("Wpisz wiek: " ))
if a >= 18:
  print("Dostałeś zezwolenie na na zobaczenie tej wiadomości użytkowniku!")
else:
  print("Złamałeś zasady licencji!")

#Zad4

Waga = int(input("Podaj wagę ciężarówki (Tony): " ))
if Waga <= 20:
  print("Dostęp zezwolony")
else:
  print("Nie możesz wjechać")

#Zad 5
a = int(input("podaj 1 liczbę: " ))
b = int(input("podaj 2 liczbę: " ))
c = int(input("podaj 3 liczbę: " ))

if a>b and b<c:
  print("Tak")
else:
  print("Nie")

#Zad 6
p = int(input("p: "))
a = int(input("a: "))
if (a**p-a) % p == 0:
  print("Spełnia MTF")
else:
  print("Nie")

#Zad 7
p = int(input("Punkt Startu na osi: " ))
k = int(input("Punkt Mety na osi: " ))
s = int(input("Długość skoku: " ))
if (s*3)+p >= k:
  print("TAK")
else:
  print("NIE")
