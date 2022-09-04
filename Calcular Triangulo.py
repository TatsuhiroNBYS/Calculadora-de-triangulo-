from math import acos, degrees
import turtle as t


print("Digite os lados de um triângulo")
a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))

cond1= a+b>c
cond2= a+c>b
cond3= b+c>a

if cond1 and cond2 and cond3:
    print("Triângulo válido.")
else:
    print("Triângulo inválido.")
    exit()
maxi=max((a,b,c))

an= a/maxi
bn= b/maxi
cn= c/maxi

A=degrees(acos((b**2+c**2-a**2)/(2*b*c)))
B=degrees(acos((a**2+c**2-b**2)/(2*a*c)))
C=180-A-B
print(A,B,C)

t.fd(a)
t.lt(180-C)
t.fd(b)
t.lt(180-A)
t.fd(c)
t.lt(180-B)
