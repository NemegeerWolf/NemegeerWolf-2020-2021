
# variabelen
aantal_groenten = 0
aantal_fruit = 0
aantal_drank = 0

kost_groenten = 0
kost_fruit = 0
kost_drank = 0

aantal_producten = 0


# code
aantal_producten = int(input("aantal producten: "))

for i in range(0, aantal_producten):
    categorie = input("Wat is de categorie? [G: Groente, F: Fruit, D: Drank]: ")
    costprijs = float(input("Wat is de kostprijs van het product: "))
    if str.lower(categorie) == "g":
        aantal_groenten += 1
        kost_groenten += costprijs
    elif str.lower(categorie) == "f":
            aantal_fruit += 1
            kost_fruit += costprijs
    elif str.lower(categorie) == "d":
            aantal_drank += 1
            kost_drank += costprijs

if not aantal_groenten == 0:
    print(f"\n{aantal_groenten:.0f} producten zitten in de categorie Groenten\nTotale kostprijs: {kost_groenten:.2f} \nGemiddelde prijs per product: {kost_groenten/aantal_groenten:.2f}")
if not aantal_fruit == 0:
    print(f"\n{aantal_fruit:.0f} producten zitten in de categorie Fruit\nTotale kostprijs: {kost_fruit:.2f}\nGemiddelde prijs per product: {kost_fruit/aantal_fruit:.2f}")
if not aantal_drank == 0:
    print(f"\n{aantal_drank:.0f} producten zitten in de categorie Groenten\nTotale kostprijs: {kost_drank:.2f} \nGemiddelde prijs per product: {kost_drank/aantal_drank:.2f}")

