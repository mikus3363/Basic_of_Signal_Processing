
for linia in open("palindromy").readlines():
    linia = linia.strip()
    if linia == linia[::-1]:
        print(linia + " palindromy")
    else:
        print(linia + " niepalindromy")
