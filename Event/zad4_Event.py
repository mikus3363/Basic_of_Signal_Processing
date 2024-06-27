

tab=[]
counterall = 0
for linia in open("zad4_data").readlines():
    counter = 0
    linia = linia.strip()
    kartka,wyniki = linia.split(":")
    wygrane,moje = wyniki.split("|")
    liczbymoje = moje.split()
    liczbywygrane = wygrane.split()

    for i in range(0,len(liczbymoje)):
        if liczbymoje[i] in liczbywygrane:
            if counter == 0:
                counter = 1
            else:
                counter = counter*2
    counterall+=counter
    counter=0
print(counterall)
