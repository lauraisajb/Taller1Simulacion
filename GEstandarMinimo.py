import numpy as np

x=int (input("Por favor ingresa la semilla: "))
print("")

a=int (input("Por favor ingresa el multiplicador: "))
print("")

m=int (input("Por favor ingresa el modulo: "))
print("")

q=np.floor(m/a)
q=int(q)

r=m%a
Rn=[]
Almacen=[x]
while True: 
    Xn1= (a*x)%m
    
    if Xn1 in Almacen:
        break
    else: 
        Almacen.append(Xn1)
        x=Xn1
        rn=x/m
        Rn.append(rn)

print(Almacen)
print(Rn)