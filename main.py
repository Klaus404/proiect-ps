import pandas as pd
import csv
import chardet
import matplotlib.pyplot as plt

#Am creat o lista cu toti angajatii din compania eMAG
listaAngajati = [
    "Miruna Popescu",
    "Andrei Botez",
    "Ilinca Luca",
    "Teodor Enescu",
    "Camelia Ionescu",
    "Vlad Popa",
    "Ana-Maria Ivan",
    "Daria Dima",
    "Tudor Munteanu",
    "Ioana Gavrilă",
    "Andrei Tudose",
    "Maria-Magdalena Iordache",
    "Cosmin Dumitru",
    "Andreea Cîrstea",
    "Răzvan Balan",
    "Alina Radulescu",
    "Andrei Stan",
    "Ana Dumitrescu",
    "Mihai Cojocaru",
    "Roxana Stoica"
]

#Am adaugat un angajat nou in firma
listaAngajati.append("Corina Andreea")

#Afisam numarul curent de angajati
print(len(listaAngajati))
print("\n")


for angajat in listaAngajati:
    print(angajat)

print("\n")

listaAngajati.sort()

for angajat in listaAngajati:
    print(angajat)

print("\n")

#Am creat dictionare pentru fiecare vanzator
vanzator1 = {"nume": "Evomag", "tip": "Asociat", "rating": "3.4", "clasament": "13"}
vanzator2 = {"nume": "Altex", "tip": "Asociat", "rating": "4.4", "clasament": "5"}
vanzator3 = {"nume": "VAN COFFE", "tip": "Utilizator", "rating": "4.8", "clasament": "3"}
vanzator4 = {"nume": "La baiatu", "tip": "Utilizator", "rating": "3.2", "clasament": "14"}
vanzator5 = {"nume": "Electrolux", "tip": "Asociat", "rating": "2.8", "clasament": "17"}
vanzator6 = {"nume": "Cheap el", "tip": "Utilizator", "rating": "4", "clasament": "10"}
vanzator7 = {"nume": "Mircea SRL", "tip": "Utilizator", "rating": "4.1", "clasament": "8"}
vanzator8 = {"nume": "Emag", "tip": "Asociat", "rating": "4.9", "clasament": "2"}
vanzator9 = {"nume": "Side by side event", "tip": "Asociat", "rating": "5", "clasament": "1"}
vanzator10 = {"nume": "Anuvio", "tip": "Utilizator", "rating": "3.2", "clasament": "14"}
vanzator11 = {"nume": "Celltek", "tip": "Utilizator", "rating": "3.8", "clasament": "12"}
vanzator12 = {"nume": "Fotomania", "tip": "Asociat", "rating": "4.6", "clasament": "4"}
vanzator13 = {"nume": "Vma Plus", "tip": "Asociat", "rating": "4.4", "clasament": "5"}
vanzator14 = {"nume": "Go4fit", "tip": "Utilizator", "rating": "3.9", "clasament": "11"}
vanzator15 = {"nume": "Sola Switzerland", "tip": "Asociat", "rating": "3.2", "clasament": "14"}
vanzator16 = {"nume": "PADRINO DRINKS", "tip": "Utilizator", "rating": "4.1", "clasament": "8"}
vanzator17 = {"nume": "Bestlife", "tip": "Utilizator", "rating": "4.3", "clasament": "7"}


#Am folosit accesarea elementelor prin cheia "nume" pentru a printa angajatul1
print(vanzator1["nume"])

#Am afisat toate valorile din dictionarul primului angajat
print(vanzator1.values())
print("\n")


#Am creat un tuplu de produse oferite de eMAG
tupluProduse = (
    "Grill electric multifunctional Tefal Inicio Grill GC241D38, 2000W, Panini, inox",
    "Masina de spalat rufe Samsung WW90T554DAW/S7, 9 kg",
    "Rasnita de cafea Bosch TSM6A013B, 180 W, 75 g, cutit otel inoxidabil, negru",
    "Monitor gaming curbat LED VA Samsung - Samsung Odyssey 49\"",
    "Gin Whitley Neill Mango & Lime, 43%, 0.7 l",
    "Corp mobil Kring 3 Elements, 3 sertare, Sonoma",
    "Whisky Arran 10YO, Single Malt 46%, 0.7l",
    "Sistem Mesh Wi-Fi Mercusys Halo H30G(2-pack), AC1300, Dual-Band",
    "Soundbar Bose TV, Bluetooth 4.2, HDMI Arc, Negru",
    "Cartus hartie Polaroid pentru Polaroid OneStep 2/I-1",
    "Laptop Gaming Lenovo Legion 5 15IAH7 cu procesor Intel® Core™ i5-12500H",
    "Whisky Aberlour 12YO, Single Malt 40%, 0.7l",
    "Whisky Monkey Shoulder, Blended 40%, 0.7l",
    "Laptop Apple MacBook Pro 14 (2021) cu procesor Apple M1 Pro Space Grey",
    "Whisky Red Breast, 12YO, Irish 40%, 0.7l",
    "Set gantere reglabile FitTronic 20 kg FG20",
    "Boxe gaming A+ Kandaon, 2.0, Iluminare RGB",
    "Incarcator retea Apple, USB Type C, 20W, White",
    "Drona SG 906 PRO Max2, 4000m distanta de control, detector",
)

for produs in tupluProduse:
    print(produs)

#Am verificat ca incarcatorul Apple apare o singura data listat in produse
print("\n")
print("Numarul de incarcatoare este: " + str(tupluProduse.count("Incarcator retea Apple, USB Type C, 20W, White")))
print('\n')

with open('./Vanzari.csv') as csv_file:
    vanzariFisier = csv.reader(csv_file, delimiter=';')

    # Ignorarea primului rând cu denumirea coloanelor
    next(vanzariFisier)

    # Iterarea peste rândurile fișierului CSV si calculam veniturile din vanzari ale companiei emag
    for rand in vanzariFisier:
        venituri = int(rand[6]) * int(rand[7])

    #Afisam veniturile
    print("Veniturile toatale ale companiei sunt: " + str(venituri))


# Detectarea codării fișierului CSV
with open('Vanzari.csv', 'rb') as f:
    result = chardet.detect(f.read())

# Citirea fișierului CSV și stocarea într-un DataFrame
df = pd.read_csv('Vanzari.csv', delimiter=";", encoding=result['encoding'])

print(df)

df.set_index('Numar comanda', inplace=True)
#Accesez datele despre comanda numarul 4
print(df.loc[4])

print("\n")
#Afisez elementul din dataframe de pe pozitia [3, 2]
print(df.iloc[3, 2])
print("\n")

#Accesarea primului produs (șirul 0, toate coloanele):
prima_comanda = df.iloc[0, :]
#Afisarea lui
print("Prima comanda:")
print(prima_comanda)


#Modificarea datelor in pandas - Modificarea unei comenzi gresite

# Afișați DataFrame-ul original
print("DataFrame original:")
print(df)

# Modificați datele pentru comanda greșită (în acest caz, comanda cu numărul 8)
index_comanda_gresita = 8  # Indexul pentru comanda greșită
cod_client_nou = "4E 6F 75 20 43 6F 64"  # Noul cod de client
furnizor_nou = "Furnizor corect"  # Noul furnizor

# Actualizați coloanele "Cod Client" și "Furnizor"
df.at[index_comanda_gresita, 'Cod Client'] = cod_client_nou
df.at[index_comanda_gresita, 'Furnizor'] = furnizor_nou

# Afișați DataFrame-ul modificat
print("\nDataFrame modificat:")
print(df)

# Gruparea datelor după coloana 'Categorie'
grouped = df.groupby('UM')

# Calcularea sumei valorilor pe grup
valorVanzri = grouped.sum('Vanzari')
print("Suma valorilor pe grup:")
print(valorVanzri)

# Numărarea elementelor în fiecare grup
valoriNumarate = grouped.count()
print("\nNumărul de elemente în fiecare grup:")
print(valoriNumarate)

#Cream un grafic cu bare in care sa afisam vanzarile tuturor furnizorilor
#Setarea dimensiunilor și stilului diagramelor
plt.style.use('ggplot')
plt.figure(figsize=(10, 5))

# Crearea diagramelor cu bare
plt.bar(df['Furnizor'], df['Valoare'], color='b', width=0.4)

# Adăugarea etichetelor axelor și a titlului
plt.xlabel('Furnizor')
plt.ylabel('Valoare')
plt.title('Diagramă cu bare pentru categorii')

# Afișarea diagramelor
plt.show()

#Stergerea unei inregistrari
print("DataFrame original:")
print(df)

# Ștergerea înregistrării cu indexul 5, de exemplu
index_de_sters = 5
df = df.drop(index_de_sters)

print("\nDataFrame după ștergerea înregistrării:")
print(df)

#- prelucrarea seturilor de date cu merge / join;

# Crearea dataframe-ului cu informatii despre produsele comandate
produse_df = pd.DataFrame({
    'Numar comanda': [1, 3, 6, 7, 9, 12, 14, 16, 18, 20],
    'Produs': ['Laptop', 'Cafea', 'Televizor', 'Frigider', 'Smartphone', 'Aparat foto', 'Bicicleta', 'Bautura energizanta', 'Tableta', 'Lapte'],
    'Pret': [3000, 50, 4000, 2000, 1500, 1000, 300, 5, 2000, 5]
})

# Combina cele doua dataframe-uri bazat pe coloana comuna "Numar comanda"
comenzi_df = pd.merge(df, produse_df, on='Numar comanda')

# Afisarea dataframe-ului combinat
print(comenzi_df)
