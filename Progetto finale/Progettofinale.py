import os
import csv
import pandas as pd

dati = pd.read_csv("database.csv")

class Utente: 
    def init(self, nome, cognome, username, password, premium = False):            
        self.nome=nome
        self.cognome=cognome
        self.username=username
        self.password=password
    
    def registrazione(self):
        self.nome=input("Inserisci nome \n")
        self.cognome=input("Inserisci cognome: \n")

    def create_password(self):
        self.password=input("Inserisci Password: ")

    def create_username(self, nome, cognome):
        self.username = nome.lower() + "." + cognome.lower() + str(quanti_user(nome.lower() + "." + cognome.lower()))

    def premium(self, username):
        riga = dati.loc[dati['Username'] == username].index[0]
        if dati["Premium"][riga] == True:
            print("Ma sei già premium!")
            home(username)
        else:
            dati["Premium"][riga] = True
            #Aggiornare il database alessandro lo ha fatto
            print("Complimenti, sei appena passato a premium!")
            home(username)


    def assistenza(self):
        print("Chiama questo numero e arrangiati: +39 800522522")

    def funzioni_premium(self, username):
        riga = dati.loc[dati['Username'] == username].index[0]
        if dati["Premium"][riga] == True:
            pass
        else:
            print("Devi passare a premium per accedere a questa funzione")


def accedi():
        username_ins=input("Inserisci username: \n")
        if username_ins in list(dati["Username"]):
            password_ins=input("Inserisci password: \n")
            riga = dati.loc[dati['Username'] == username_ins].index[0]
            if password_ins == list(dati["Password"])[riga]:
                home(username_ins)
            else:
                print("La password inserita è sbagliata!")
                accedi()
        else:
            print("Username inesistente")
            accedi()

def quanti_user(username):
    c = 0
    for user in list(dati["Username"]):
        if username in user:
            c += 1
    if c == 0:
        return ""
    else:
        return c + 1

#AGGIORNAMENTO DEL FILE CSV
def aggiorna_database(nome, cognome, userr, passw):

    # Dati da aggiungere alla tabella
    nuova_riga = [len(dati) + 1, nome, cognome, userr, passw, False]
    
    # Percorso del file CSV da aggiornare
    percorso_file = 'database.csv'

    # Apri il file in modalità append
    with open(percorso_file, 'a', newline='') as file_csv:
        writer = csv.writer(file_csv)

        # Aggiungi la nuova riga alla tabella
        writer.writerow(nuova_riga)


#Funzione per mostrare il login
def login():
    os.system('cls')
    registrazione = True
    #Menu
    while(registrazione):
        os.system('cls')
        scelta=int(input("1) Registrati\n2) Accedi \n"))
        if scelta == 1: 
            utente=Utente()
            utente.registrazione()
            utente.create_username(utente.nome,utente.cognome) 
            utente.create_password()       
            aggiorna_database(utente.nome, utente.cognome,utente.username, utente.password)
        elif scelta == 2: 
            accedi()
            registrazione = False
        else:
            print("Riprova")


#Funzione per mostrare il menu
def home(username_inserito):
    os.system('cls')
    registrazione = True
    #Menu
    while(registrazione):
        os.system('cls')
        scelta=int(input("Scegli cosa vuoi fare:\n1) Conto Corrente\n2) Risparmi\
                         \n3) Carta \n5) Passa a premium\n6) Funzioni premium con investimenti\n"))
        if scelta == 1: 
            #Conto Corrente da inizializzare
            pass
        elif scelta == 2: 
            #Risparmi 
            pass
        elif scelta == 3: 
            #Carta
            pass
        elif scelta == 4:
           #Report
           pass
        elif scelta == 5:
           #Investimenti
           pass
        elif scelta == 6:
            #Premium
            Utente().premium(username_inserito)
            registrazione = False
        elif scelta == 7:
            # Funzionalità premium
            Utente().funzioni_premium(username_inserito)
        else:
            print("Riprova")
            pass
    

#Schermata di Login
login()