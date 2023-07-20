import pandas as pd

def risparmi(username):
    df = pd.read_csv("risparmi.csv")
    print(df[df["username"] == username].to_string(index = False))

def monitoraggio(username):
    # Carica il file CSV in un DataFrame
    try:
        df = pd.read_csv("risparmi.csv")
    except FileNotFoundError:
        print("Errore: il file 'risparmi.csv' non esiste.")
        return

    # Verifica se lo username è presente nella colonna "username"
    if username not in df["username"].values:
        print(f"Errore: lo username '{username}' non è presente nel file.")
        return

    # Filtra il DataFrame per ottenere solo i dati relativi allo username specificato
    user_data = df[df["username"] == username]

    # Ottieni l'elenco dei nomi di salvadanaio associati a quello username
    nomi_salvadanai = user_data["nomeSalvadanaio"] # nel caso possano esistere più salvadanai con lo stesso nome per lo stesso username, bisogna aggiungere un ".unique()" alla fine di questa riga

    # Ciclo per chiedere all'utente di inserire il nome del salvadanaio da monitorare finchè non ne viene inserito uno corretto
    while True:
        nome_scelto = input("Inserisci il nome esatto del salvadanaio che vuoi monitorare tra i seguenti:\n" + "\n".join(nomi_salvadanai) + "\n")
        if nome_scelto in list(nomi_salvadanai):
            break
        else:
            print("Errore: Il nome del salvadanaio inserito non corrisponde a nessun salvadanaio di quello username.")

    # Filtra il DataFrame per ottenere i dati relativi al nome del salvadanaio scelto
    salvadanaio_data = user_data[user_data["nomeSalvadanaio"] == nome_scelto]

    # Calcola la percentuale e arrotondala a 2 decimali
    percentuale = round(float(salvadanaio_data["risparmio"]) / float(salvadanaio_data["obiettivo"]) * 100, 2)

    # Stampa il risultato
    print(f"Percentuale del salvadanaio '{nome_scelto}': {percentuale}%")


def menùRisparmi(username):
    scelta = int(input("Scegli cosa vuoi fare:\n1) I tuoi salvadanai\n2) Monitoraggio\n3) Indietro\n"))
    if scelta == 1:
        risparmi(username)
        menùRisparmi(username)
    elif scelta == 2:
        monitoraggio(username)
        menùRisparmi(username)
    elif scelta == 3:
        return # così dovrebbe semplicemente tornare alla home precedente, cioè quella del file principale
    else:
        print("Scelta non valida. Riprova")
        menùRisparmi(username)