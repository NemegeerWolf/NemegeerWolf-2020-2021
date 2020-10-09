klinker = ["a", "e", "i", "o", "u"]
aantal_klinkers = 0;

woord = input("geef een woord op: ")

for symbool in woord:
    for letter in klinker:
        if symbool == letter:
            aantal_klinkers += 1

print(f"Aantal klinkers: {aantal_klinkers}\nAantal medeklinkers: {len(woord) - aantal_klinkers}")
