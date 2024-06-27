
tab = []
counter = 0
for linia in open("zad3_data"):
    linia = linia.strip()
    tab+=linia

flaga = False
liczba=""
for i in range(0,len(tab),1):

    if 0<=i<=139:
        if 48 <= ord(tab[i]) <= 57:
            if (48 > ord(tab[i + 1]) or ord(tab[i + 1]) > 57) and (48 > ord(tab[i - 1]) or ord(tab[i - 1]) > 57):
                if tab[i - 1] != "." or tab[i + 139] != "." or tab[i + 140] != "." or tab[i + 141] != "." or tab[i + 1] != ".":
                    flaga = True
                liczba += tab[i]
                if flaga:
                    counter += int(liczba)
                    flaga = False
                    liczba = ""
                else:
                    flaga = False
                    liczba = ""
            if (48 <= ord(tab[i + 1]) <= 57) and (48 > ord(tab[i - 1]) or ord(tab[i - 1]) > 57):
                if tab[i - 1] != "." or tab[i + 139] != "." or tab[i + 140] != "." or tab[i + 141] != "." :
                    flaga = True
                liczba += tab[i]
            if (48 <= ord(tab[i + 1]) <= 57) and (48 <= ord(tab[i - 1]) <= 57):
                if tab[i + 140] != ".":
                    flaga = True
                liczba += tab[i]
            if (48 > ord(tab[i + 1]) or ord(tab[i + 1]) > 57) and 48 <= ord(tab[i - 1]) <= 57:
                if tab[i + 139] != "." or tab[i + 140] != "." or tab[i + 141] != "." or tab[i + 1] != ".":
                    flaga = True
                liczba += tab[i]
                if flaga:
                    counter += int(liczba)
                    flaga = False
                    liczba = ""
                else:
                    flaga = False
                    liczba = ""

    if len(tab)-140<=i<=len(tab):
        if 48 <= ord(tab[i]) <= 57:
            if (48 > ord(tab[i + 1]) or ord(tab[i + 1]) > 57) and (48 > ord(tab[i - 1]) or ord(tab[i - 1]) > 57):
                if tab[i - 1] != "." or tab[i - 141] != "." or tab[i - 140] != "." or tab[i - 139] != "." or tab[i + 1] != ".":
                    flaga = True
                liczba += tab[i]
                if flaga:
                    counter += int(liczba)
                    flaga = False
                    liczba = ""
                else:
                    flaga = False
                    liczba = ""
            if 48 <= ord(tab[i + 1]) <= 57 and (48 > ord(tab[i - 1]) or ord(tab[i - 1]) > 57):
                if tab[i - 1] != "." or tab[i - 139] != "." or tab[i - 140] != "." or tab[i - 141] != ".":
                    flaga = True
                liczba += tab[i]
            if 48 <= ord(tab[i + 1]) <= 57 and 48 <= ord(tab[i - 1]) <= 57:
                if tab[i - 140] != ".":
                    flaga = True
                liczba += tab[i]
            if (48 > ord(tab[i + 1]) or ord(tab[i + 1]) > 57) and 48 <= ord(tab[i - 1]) <= 57:
                if tab[i - 141] != "." or tab[i - 140] != "." or tab[i - 139] != "." or tab[i + 1] != ".":
                    flaga = True
                liczba += tab[i]
                if flaga:
                    counter += int(liczba)
                    flaga = False
                    liczba = ""
                else:
                    flaga = False
                    liczba = ""
    if 139<i<len(tab)-140:
        if 48 <= ord(tab[i]) <= 57:
            if (48 > ord(tab[i+1]) or ord(tab[i+1]) > 57) and (48 > ord(tab[i-1]) or ord(tab[i-1]) > 57):
                if tab[i-1]!="." or tab[i-141]!="." or tab[i-140]!="." or tab[i-139]!="." or tab[i+139]!="." or tab[i+140]!="." or tab[i+141]!="." or tab[i+1]!=".":
                    flaga = True
                liczba+=tab[i]
                if flaga:
                    counter += int(liczba)
                    flaga = False
                    liczba = ""
                else:
                    flaga = False
                    liczba = ""
            if 48 <= ord(tab[i+1]) <= 57 and (48 > ord(tab[i-1]) or ord(tab[i-1]) > 57):
                if tab[i - 1] != "." or tab[i - 139] != "." or tab[i - 140] != "." or tab[i - 141] != "." or tab[i + 139] != "." or tab[i + 140] != "." or tab[i + 141] != ".":
                    flaga = True
                liczba += tab[i]
            if 48 <= ord(tab[i+1]) <= 57 and 48 <= ord(tab[i-1]) <= 57:
                if tab[i - 140] != "." or tab[i + 140] != ".":
                    flaga = True
                liczba += tab[i]
            if (48 > ord(tab[i+1]) or ord(tab[i+1]) > 57) and 48 <= ord(tab[i-1]) <= 57:
                if tab[i-141]!="." or tab[i-140]!="." or tab[i-139]!="." or tab[i+139]!="." or tab[i+140]!="." or tab[i+141]!="." or tab[i+1]!=".":
                    flaga = True
                liczba+=tab[i]
                if flaga:
                    counter += int(liczba)
                    flaga = False
                    liczba = ""
                else:
                    flaga = False
                    liczba = ""
print(counter)