import math

print("Program liczy pierwiastki równania")
a = int(input("podaj pierwszą wartość a : "))
b = int(input("podaj drugą wartość b : "))
c = int(input("podaj trzecią wartość c : "))

print("równanie : ",a,"x^2 +",b,"x +",c)

delta = (b*b)-(4*a*c)
counter = True
while counter:
    if delta > 0:
        print("miejsca zerowe to : ",(-b - math.sqrt(delta)) / (2 * a)," oraz ",(-b + math.sqrt(delta)) / (2 * a))
    elif delta == 0:
        print("miejsce zerowe : ",(-b)/(2*a))
    else:
        print("Funkcja nie ma miejsc zerowych")
    zakoncz = int(input("0 Jeśli chcesz kontynułować, inna jak powtórzyć"))
    if zakoncz!=0:
        counter=False
        print("Program zakonczono")