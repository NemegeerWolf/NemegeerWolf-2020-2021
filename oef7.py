getal1 = int(input("geef een startwaard "))
getal2 = int(input("geef een stapgrote "))
getal3 = int(input("geef het gewenste aantal af te printen getallen "))

def print_lijst_getallen(startwaarde, stapgrote, aantal):
    for i in range(0,aantal):
        
        print(startwaarde)
        startwaarde = startwaarde + stapgrote

print_lijst_getallen(getal1, getal2, getal3)
