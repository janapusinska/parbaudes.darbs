def lasit_datni():
    datnes_nosaukums = input("Ievadīt nosaukumu:")
    try:
        with open(datnes_nosaukums, 'r') as sakitlis:
            saturs = sakitlis.read()
            print(saturs)
    except FileNotFoundError:
        print("Datne nav atrasta")
