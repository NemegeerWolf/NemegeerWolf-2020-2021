#import
import random

def genereer_paswoord(min_lengte, max_lengte):
    lengte = random.randrange(min_lengte,max_lengte+1)
    paswoord = ""
    for i in range(0,lengte):
        #moest in 2 worden gespitst om ander tekens er uit te houden.
        if(random.randint(0,2) == 0):
            #hooftletters
            paswoord += chr(random.randint(65,91))
        else:
            #kleine letters
            paswoord += chr(random.randint(97,123))
    return f"gekozen lengte: {lengte}\nUw paswoord is {paswoord}"

minimum_lengte = int(input("geef een minimum lengte van het paswoord op: "))
maximum_lengte = int(input("geef een maximum lengte van het paswoord op: "))

print(genereer_paswoord(minimum_lengte, maximum_lengte))
