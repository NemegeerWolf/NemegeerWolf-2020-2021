import random

getal = random.randrange(1, 21)
gok = 0;
aantalGoks = 0;
while not getal == gok:
    aantalGoks+= 1
    gok = int(input("doe een gok tussen 1 en 20"))
    if gok == getal:
        print("Progiciat. U heb het gevonden \tU gokte",aantalGoks )
    elif getal > gok:
        print("fout, getal is Groter")
    else:
        print("fout, getal is Kleiner")
        
