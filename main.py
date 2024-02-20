import math


# Récupération des coefficients

a = float(input("Print a : "))
b = float(input("Print b : "))
c = float(input("Print c : "))

#Calcul du déterminant

det = b**2 - 4*a*c

#Conditions du déterminants et affichage des solutions en fonction de ceux-ci
if det > 0 : 
   X1 = ( -b + math.sqrt(det)) / ( 2*a )
   X2 = ( -b - math.sqrt(det)) / ( 2*a )
   print(f"Les solutions sont {X1} et {X2}.Merci d'avoir sollicité l'aide de Kunji!")
elif det == 0 :
    X0= -b / 2*a
    print(f"La solution unique est {X0}.Merci d'avoir sollicité l'aide de Kunji!")
   
else:
    print("Il n'y a pas de solutions réelles.Merci d'avoir sollicité l'aide de Kunji!")
 