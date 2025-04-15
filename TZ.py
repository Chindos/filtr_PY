import pandas as pd
import difflib

# Load file
file_name = input("Zadej název Excel souboru: ")
df = pd.read_excel(file_name)
veci = dict(zip(df.iloc[:, 0].astype(str).str.strip(), df.iloc[:, 1]))
znamy_veci = list(veci.keys())

# Compare
def porovnej_vstup(text_od_uzivatele, uroven=0.6):
    radky = text_od_uzivatele.strip().split("\n")
    vysledky = []
    for radek in radky:
        radek = radek.strip()
        podobne = difflib.get_close_matches(radek, znamy_veci, n=1, cutoff=uroven)
        if podobne:
            nalezene = podobne[0]
            objem = veci[nalezene]
            vysledky.append((radek, nalezene, objem))
        else:
             vysledky.append((radek, None, None))
    return vysledky

print("Napiš ty věci, co tam maj bejt, každej na řádku. Když už nic nenapíšeš, zmáčkni prázdnej enter.\n")

vstup = []
while True:
    radek = input()
    if radek.strip() == "":
        break
    vstup.append(radek)
text = "\n".join(vstup)
vysledky = porovnej_vstup(text)

print("\nTady máš výsledky, tak nějak:\n")
for zadano, nasel, objem in vysledky:
    if nasel:
            print(f"'{zadano}' => '{nasel}' => {objem} m³")
    else:
         print(f"'{zadano}' => nic nenalezeno, smůla 😕")
