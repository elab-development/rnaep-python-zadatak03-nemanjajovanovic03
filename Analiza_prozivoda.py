import random
import math

proizvodi = [
    "Laptop",
    "Mis",
    "Tastatura",
    "Monitor",
    "Slusalice",
    "Web kamera",
    "USB flash",
    "Stampac"
]

cene = {
    "Laptop": 950.99,
    "Mis": 19.99,
    "Tastatura": 49.99,
    "Monitor": 199.99,
    "Slusalice": 89.99,
    "Web kamera": 59.99,
    "USB flash": 14.99,
    "Stampac": 129.99
}

# 1. Prikaz svih proizvoda i cena
print("Svi proizvodi i njihove cene:")
for proizvod, cena in cene.items():
    print(f"{proizvod} - {cena:.2f} €")

print()

# 2. Unos budzeta i ispis proizvoda koje korisnik moze da priusti
budzet = float(input("Unesite svoj budzet u evrima: "))

print("\nProizvodi koje mozete da priustite:")
ima_proizvoda = False

for proizvod, cena in cene.items():
    if cena <= budzet:
        print(f"{proizvod} - {cena:.2f} €")
        ima_proizvoda = True

if not ima_proizvoda:
    print("Nazalost, nijedan proizvod nije u okviru vaseg budzeta.")

print()

# 3. Funkcija koja vraca najskuplji proizvod
def najskuplji_proizvod(recnik_cena):
    return max(recnik_cena, key=recnik_cena.get)

najskuplji = najskuplji_proizvod(cene)
print(f"Najskuplji proizvod je: {najskuplji} - {cene[najskuplji]:.2f} €")

print()

# 4. Koriscenje random modula
nasumican_proizvod = random.choice(proizvodi)
print(f"Korisniku je privukao paznju proizvod: {nasumican_proizvod}")

print()

# 5. Koriscenje math modula - prosecna cena
zbir_cena = sum(cene.values())
prosek = zbir_cena / len(cene)

prosecna_cena = math.floor(prosek * 100 + 0.5) / 100
print(f"Prosecna cena svih proizvoda je: {prosecna_cena:.2f} €")

print()

# 6. Broj prodatih komada svakog proizvoda
prodati_komadi = [5, 20, 12, 7, 10, 8, 25, 4]

ukupan_prihod = 0
for proizvod, kolicina in zip(proizvodi, prodati_komadi):
    ukupan_prihod += cene[proizvod] * kolicina

print(f"Ukupan prihod od prodaje je: {ukupan_prihod:.2f} €")

print()

# 7. Dodavanje novog proizvoda
novi_proizvod = "Tablet"
nova_cena = 299.99

proizvodi.append(novi_proizvod)
cene[novi_proizvod] = nova_cena

print("Azurirana lista proizvoda:")
for proizvod in proizvodi:
    print(proizvod)

print()

# 8. Sortiranje proizvoda po ceni
sortirani_proizvodi = sorted(cene.items(), key=lambda x: x[1])

print("Proizvodi sortirani od najjeftinijeg ka najskupljem:")
for proizvod, cena in sortirani_proizvodi:
    print(f"{proizvod} - {cena:.2f} €")