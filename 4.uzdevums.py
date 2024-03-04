def lasit_datni(fails):
    with open(fails, 'r') as f:
        saturs = f.read()
    return saturs
fails_nosaukums = input("Ievadīt nosaukumu: ")
content = lasit_datni(fails_nosaukums)
print(content)