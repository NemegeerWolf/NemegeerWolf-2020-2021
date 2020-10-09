
def is_schrikkeljaar(jaar):
    if jaar % 4 == 0  and (not jaar % 100 == 0 or jaar%400 == 0):
        return True
    else:
        return False

begin_jaar = int(input("geef een begin jaar: "))
eind_jaar = int(input("geef een eind jaar: "))

for jaar in range(begin_jaar, eind_jaar+1):
    if is_schrikkeljaar(jaar):
        print(jaar, " is een schrikkeljaar")
    