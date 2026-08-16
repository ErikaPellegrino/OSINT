
import pandas as pd
import requests

# 1. Scarichiamo i dati dall'API
url = "https://opensky-network.org/api/states/all"
print("1. Scaricamento dati in corso...")
risposta = requests.get(url)
dati = risposta.json()
lista_aerei = dati["states"]

# 2. Definiamo i nomi delle colonne
nomi_colonne = [
    "icao24",
    "callsign",
    "paese_origine",
    "time_position",
    "last_contact",
    "longitudine",
    "latitudine",
    "baro_altitude",
    "on_ground",
    "velocita_ms",
    "true_track",
    "vertical_rate",
    "sensors",
    "geo_altitude",
    "squawk",
    "spi",
    "position_source",
]

# 3. Creiamo la tabella iniziale e selezioni colonne utili
df_aerei = pd.DataFrame(lista_aerei, columns=nomi_colonne)
colonne_utili = [
    "icao24",
    "callsign",
    "paese_origine",
    "longitudine",
    "latitudine",
    "geo_altitude",
    "velocita_ms",
]
df_aerei = df_aerei[colonne_utili]

# 4. Pulizia dai dati mancanti (GPS)
df_aerei = df_aerei.dropna(subset=["longitudine", "latitudine"])

# 5. FILTRO OSINT: Isoliamo solo i voli sopra l'Italia
lat_min, lat_max = 35.0, 47.0
long_min, long_max = 6.0, 19.0

aerei_italia = df_aerei[
    (df_aerei["latitudine"] >= lat_min)
    & (df_aerei["latitudine"] <= lat_max)
    & (df_aerei["longitudine"] >= long_min)
    & (df_aerei["longitudine"] <= long_max)
].copy()

# 6. Calcoliamo la velocità in km/h
aerei_italia["velocita_kmh"] = aerei_italia["velocita_ms"] * 3.6
# Puliamo gli spazi bianchi nei codici di chiamata (es. 'AZA123  ' -> 'AZA123')
aerei_italia["callsign"] = aerei_italia["callsign"].str.strip()

# 7. SALVATAGGIO: Creiamo il file CSV per Power BI
nome_file = "voli_italia.csv"
aerei_italia.to_csv(nome_file, index=False)

print("\n--------------------------------------------------")
print(f"2. OPERAZIONE COMPLETATA!")
print(f"   Aerei attualmente nello spazio aereo italiano: {len(aerei_italia)}")
print(f"   Il file '{nome_file}' è stato salvato nella cartella.")
print("--------------------------------------------------")