dati_ievads=input("Ievadīt vārdu un uzvārdu:")
with open('lietotajs.txt','w',encoding='utf8') as file:
    file.write(dati_ievads)