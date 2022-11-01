#Zad 1
for i in range(1, 31, 1):
  print(i, "Dzień listopada")

#Zad 2
for i in range(1, 200, 2):
  i = i**2
  print(i)

#Zad 3
for i in range (1000, 10000, 1):
  if i%379 == 0:
    print(i)

#Zad 4
for i in range (100, 1000, 1):
  if i%5 == 0 or i%6 == 0:
    print(i, "Nie podzielne przez 11")
  if i%5 == 0 or i%6 == 0 or i%11 == 0:
    print(i, "Podzielne przez 11")

#Zad 5
nliczb = int(input("Ile liczb chcesz wprowadzić? " ))
a = 0
for i in range (1, nliczb + 1):
  n = int(input("Wprowadź liczbę: "))
  a = a + n
print("Suma liczb to ", a)

#Zad 6
k = int(input("Podaj liczbę k: "))
x = 0
for i in range(0,2*k,2):
  x += i
print("Wynik to:",x)

#Zad 7
m = int(input("Podaj liczbę m: "))
mcount = 0
x = 0
for i in range(10 ,100):
  if i%2 != 0 and mcount < m and i < 100:
    mcount = mcount+1
    x += i
print(x)

#Zad8
W = int(input("Wprowadź kwotę wejściową: "))
L = int(input("Podaj okres inwestycji: "))
a = 0
suma = W
for i in range(0, L*12):
  c = suma * 0.06 * (1/12)
  suma = suma + c
print(round(suma,2))

#Zad9
n = int(input("Podaj liczbę n: "))
a = 0
for i in range(21, n + 1, 100):
  a = a + i
print(a)

#Zad 10
import math
for i in range (1, 1000):
  if i%10 == math.sqrt(i):
    print(i)
  elif i%100 == math.sqrt(i):
    print(i)
