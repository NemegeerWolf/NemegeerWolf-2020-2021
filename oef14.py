naam = input("geeft uw naam op: ")
familienaam = input("geeft uw Familie op: ")
geboorte_datum = input("geeft uw geboorte datum op(dd-mm-yyyy): ")

def genereer_paswoord(naam, familienaam, geboorte_datum):
    paswoord = ""
    for i in range(0,3):
        paswoord += familienaam[i]
    for i in range(0,2):
        paswoord += naam[i]
    for i in range(3,5):
        paswoord += geboorte_datum[i]
    for i in range(8,10):
        paswoord += geboorte_datum[i]
    return paswoord

print(genereer_paswoord(naam, familienaam, geboorte_datum))