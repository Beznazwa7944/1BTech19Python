#Zad1
a = int(input("Wpisz 1 Liczbę: "))
b = int(input("Wpisz 2 Liczbę: "))
if (a+b)%2 == 0:
  print("TAK")
else:
  print("NIE")

#Zad2
import math
a = int(input("Wpisz 1 Liczbę: "))
g = int(input("Wpisz 2 Liczbę: "))
if (a+g)/2 > math.sqrt(a*g):
  print("TAK")
else:
  print("NIE")

#Zad3
k = int(input("Wpisz 1 Liczbę: "))
m = int(input("Wpisz 2 Liczbę: "))
l = int(input("Wpisz 3 Liczbę: "))
if k==l:
  print("TAK")
  print(k, l)
elif k==m:
  print("TAK")
  print(k, m)
elif l==m:
  print("TAK")
  print(m, l)
else:
  print("NIE")

#Zad4
a = int(input("Wpisz 1 Liczbę: "))
b = int(input("Wpisz 2 Liczbę: "))
c = int(input("Wpisz 3 Liczbę: "))
d = int(input("Wpisz 4 Liczbę: "))
print(min(a,b,c,d))

#Zad5
a = int(input("Bok 1: "))
b = int(input("Bok 2: "))
c = int(input("Bok 3: "))
if a<(b+c) and a>(b-c) and b<(a+c) and b>(a-c) and c<(a+b) and c>(a-b):
  print("TAK")
else:
  print("NIE")

#Zad6
a = int(input("Bok 1: "))
b = int(input("Bok 2: "))
c = int(input("Bok 3: "))

if c < (a+b) and c**2 < (a**2+b**2):
  print("Ostrokątny")
elif c < (a+b) and c**2 == (a**2+b**2):
  print("Prostokątny")
elif c < (a+b) and c**2 > (a**2+b**2):
  print("Rozwartokątny")