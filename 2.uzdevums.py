import csv

datnes_nosaukums = input("Ievadīt nosaukumu: ")

try:
    with open(datnes_nosaukums, newline='', encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile)
        for rinda in csv_reader:
            print(rinda)
except FileNotFoundError:
    print(f"Fails ar nosaukumu {datnes_nosaukums} nav atrasts")
except StopIteration:
    print("Fails ir tukšs")
except Exception as e:
    print(f"Notikusi kļūda: {e}")