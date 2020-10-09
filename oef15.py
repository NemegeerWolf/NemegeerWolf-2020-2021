email_adress = input("geef een correct howest email adres op: ")

def zoek_naam_in_email_adrs(email_adress):
    familienaam = ""
    punt_geweest = False;
    naam = ""
    naam_klaar = False;
    for symbool in email_adress:
        if symbool == "@":
            return f"De familienaam is{familienaam} en de voornaam is {naam}."
        elif symbool == ".":
            naam_klaar = True
            punt_geweest = True
            familienaam += " "
        else:
            if naam_klaar == False:
                if naam == "":
                    naam += str.upper(symbool) 
                else :
                    naam += symbool
            else:
                if punt_geweest == True:
                    punt_geweest = False
                    familienaam += str.upper(symbool) 
                else :
                    familienaam += symbool

print(zoek_naam_in_email_adrs(email_adress))
