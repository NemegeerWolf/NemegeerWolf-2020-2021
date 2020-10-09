klinker = ["a", "e", "i", "o", "u"]


woord = input("geef een woord op: ")

new_woord = ""
letter_ingevuld = False

for symbool in woord:
    letter_ingevuld = False
    for letter in klinker:
        if symbool == letter:
            new_woord += "*"
            letter_ingevuld = True

    if letter_ingevuld == False:
         new_woord += symbool

print(f"woord met geschrapte klikkers is: {new_woord}")