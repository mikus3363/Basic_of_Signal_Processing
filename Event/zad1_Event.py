counter = 0
dict = {}
dict["one"] = "1"
dict["two"] = "2"
dict["three"] = "3"
dict["four"] = "4"
dict["five"] = "5"
dict["six"] = "6"
dict["seven"] = "7"
dict["eight"] = "8"
dict["nine"] = "9"

dictlp = {}
dictlp[1] = "one"
dictlp[2] = "two"
dictlp[3] = "three"
dictlp[4] = "four"
dictlp[5] = "five"
dictlp[6] = "six"
dictlp[7] = "seven"
dictlp[8] = "eight"
dictlp[9] = "nine"

for linia in open("zad1_data").readlines():
    flaga = True
    linia = linia.strip()
    liczbacala = ""
    liczbapierw = ""
    liczbaost = ""
    for i in range(0, len(linia), 1):
        if 48 <= ord(linia[i]) <= 57:
            liczbacala += linia[i]
            flaga = False
            break
        if ord(linia[i]) > 57:
            liczbapierw += linia[i]
            for k in range(1, 10, 1):
                if dictlp[k] in liczbapierw:
                    liczbacala += dict.get(dictlp[k])
                    flaga = False
                    break
                else:
                    continue
        if flaga == False:
            break

    flaga = True
    liczbapierw = ""

    for j in reversed(range(0,len(linia))):
        if 48 <= ord(linia[j]) <= 57:
            liczbacala+=linia[j]
            flaga = False
            break
        if ord(linia[j]) > 57:
            liczbaost+=linia[j]
            odwroc = liczbaost[::-1]
            for n in range(1, 10, 1):
                if dictlp[n] in odwroc:
                    liczbacala += dict.get(dictlp[n])
                    flaga = False
                    break
                else:
                    continue
        if flaga == False:
            break

    flaga = True
    liczbaost = ""
    print(liczbacala)

    counter += int(liczbacala)
print(counter)
