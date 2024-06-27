
dict={}
dict["gra"]=0
dict["zielony"]=0
dict["czerwony"]=0
dict["niebieski"]=0
dict["moc"]=0

mocall = 0
sumaiden=0

for linia in open("zad2_data").readlines():
    liczba=""
    linia = linia.strip()
    #dict["zielony"]+=1
    for i in range(0,len(linia),1):
        if ord(linia[i])==103:
            liczba+=linia[i-3]
            liczba+=linia[i-2]
            if(int(liczba)>dict.get("zielony")):
                dict["zielony"] = int(liczba)
            liczba=""
        if ord(linia[i])==98:
            liczba+=linia[i-3]
            liczba+=linia[i-2]
            if (int(liczba) > dict.get("niebieski")):
                dict["niebieski"] = int(liczba)
            liczba=""
        if ord(linia[i])==114 and ord(linia[i-1])!=103:
            liczba+=linia[i-3]
            liczba+=linia[i-2]
            if (int(liczba) > dict.get("czerwony")):
                dict["czerwony"] = int(liczba)
            liczba=""
    dict["gra"] += 1
    dict["moc"]=dict.get("czerwony")*dict.get("niebieski")*dict.get("zielony")
    print(dict)
    print(dict.get("moc"))
    mocall+=dict.get("moc")
    # if dict.get("zielony")<=13 and dict.get("czerwony")<=12 and dict.get("niebieski")<=14:
    #     sumaiden+=dict.get("gra")
    #     print(dict)
    #print(dict)
    dict["zielony"]=0
    dict["niebieski"]=0
    dict["czerwony"]=0

print(sumaiden)
print(mocall)