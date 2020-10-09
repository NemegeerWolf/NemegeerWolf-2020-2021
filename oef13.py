string1 = input("geef een woord: ")
string2 = input("geef een ander woord: ")

def swap(string1, string2):
    new_string1 = ""
    new_string2 = ""

    for letterPositie in range(0,int(len(string1)),1):
        if letterPositie%2 == 0:
            new_string2 += string1[letterPositie]
        else:
            new_string2 += string2[letterPositie]

    for letterPositie in range(0, len(string2),1):
        if letterPositie%2 == 0:
            new_string1 += string2[letterPositie]
        else:
            new_string1 += string1[letterPositie]

    return (new_string1 + " " + new_string2)

print(swap(string1,string2))