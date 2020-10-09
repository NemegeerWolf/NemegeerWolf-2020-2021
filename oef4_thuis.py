email_adress = input("geef een  howest email adres op: ")

def controleer_emailadres(email_adress):
    
    punt1_geweest = False
    apenstaartje_geweest = False
    student_punt_howest_geschreven = False
    punt2_geweest = False

    index = 0;
    for symbool in email_adress:
        
        if symbool == ".":
            if punt1_geweest == False:
                punt1_geweest = True
            
                

        if symbool == "@":
            if punt1_geweest == True:
                apenstaartje_geweest = True
                
                if str.lower(email_adress[index+1:]) == "student.howest.be":
                    return "dit email adres is juist"
                else:
                    return "het adres voor een student van howest is 'student.howest.be'"

            else: 
                return "er moet een punt tussen je voor en achternaam"
        index += 1
        


print(controleer_emailadres(email_adress))
