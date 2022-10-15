#Zad1
a = int(input("Wpisz 1 Liczbę: "))
b = int(input("Wpisz 2 Liczbę: "))
if (a+b)%2 == 0:
  print("TAK")
else:
  print("NIE")

#Zad2
import math
a = int(input())
g = int(input())
if (a+g)/2 > math.sqrt(a*g):
  print("TAK")
else:
  print("NIE")

#Zad3
k = int(input())
m = int(input())
l = int(input())
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
a = int(input("1: "))
b = int(input("2: "))
c = int(input("3: "))
d = int(input("4: "))
print(min(a,b,c,d))

#Zad5
a = int(input())
b = int(input())
c = int(input())
if a<(b+c) and a>(b-c) and b<(a+c) and b>(a-c) and c<(a+b) and c>(a-b):
  print("TAK")
else:
  print("NIE")

#Zad6
a = int(input())
b = int(input())
c = int(input())

if c < (a+b) and c**2 < (a**2+b**2):
  print("Ostrokątny")
elif c < (a+b) and c**2 == (a**2+b**2):
  print("Prostokątny")
elif c < (a+b) and c**2 > (a**2+b**2):
  print("Rozwartokątny")