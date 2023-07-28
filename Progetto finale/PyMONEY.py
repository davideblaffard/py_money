from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
import random
import csv
import pandas as pd


dati = pd.read_csv("database.csv")


def accedi(event):
    dati=pd.read_csv('database.csv')
    username_ins = app.root.get_screen('login').children[0].username_input.text
    if username_ins in list(dati["Username"]):
        password_ins = app.root.get_screen('login').children[0].password_input.text
        riga = dati.loc[dati['Username'] == username_ins].index[0]
        if password_ins == list(dati["Password"])[riga]:
            app.root.get_screen('home').children[0].username = username_ins
            app.root.current = 'home'
        else:
            app.root.get_screen('login').children[0].info_label.text = "La password inserita è sbagliata!"
    else:
        app.root.get_screen('login').children[0].info_label.text = "Username inesistente"

def registrazione_utente(event):
    app.root.current = 'registrazione'

def recupera_pass(event):
    dati=pd.read_csv('database.csv')
    username_ins = app.root.get_screen('login').children[0].username_input.text
    if username_ins in list(dati["Username"]):
        riga = dati.loc[dati['Username'] == username_ins].index[0]
        pass_word = (dati["Password"])[riga]
        hint_pass= pass_word[0:3]+"*"*(len(pass_word)-3)
        app.root.get_screen('login').children[0].info_label.text = "La tua password è:"+str(hint_pass)
    else:
        app.root.get_screen('login').children[0].info_label.text = "Username inesistente"
    
def quanti_user(username):
    conta=dati["Username"].str.contains(username).sum()
    if conta==0:
        numero=""
    else:
        numero=conta
    return numero  
 
def aggiorna_database(nome, cognome, userr, passw, ib):
    # Dati da aggiungere alla tabella
    nuova_riga = [len(dati) + 1, nome, cognome, userr, passw, False,ib,0,0,0,0]
    
    # Percorso del file CSV da aggiornare
    percorso_file = 'database.csv'

    # Apro il file in modalità append ("a" per aggiungere alla fine del file)
    with open(percorso_file, 'a', newline='') as file_csv:
        writer = csv.writer(file_csv)

        # Aggiungo la nuova riga alla tabella
        writer.writerow(nuova_riga)

def aggiornamento_database(username,categoria,obiettivo,importo):
    # Dati da aggiungere alla tabella
    nuova_riga = [username, importo, categoria, obiettivo]

    # Percorso del file CSV da aggiornare
    percorso_file = 'risparmi.csv'

    # Apro il file in modalità append ("a" per aggiungere alla fine del file)
    with open(percorso_file, 'a', newline='') as file:
        writer = csv.writer(file)

        # Aggiungo la nuova riga alla tabella
        writer.writerow(nuova_riga)



class Utente:
    def __init__(self):
        self.nome = ""
        self.cognome = ""
        self.username = ""
        self.password = ""

    def registrazione(self, nome, cognome, password, registrazione_screen):
        self.nome = nome
        self.cognome = cognome
        self.password = password
        self.iban = "IT" + str(random.randint(1000000, 99999999))
    
        if registrazione_screen:
            self.create_username(self.nome, self.cognome, registrazione_screen)
        else:
            self.create_username(self.nome, self.cognome)

        aggiorna_database(self.nome, self.cognome, self.username, self.password,self.iban)

    def create_username(self, nome, cognome,registrazione_screen):
        self.username = nome.lower() + "." + cognome.lower() + str(quanti_user(nome.lower() + "." + cognome.lower()))
        registrazione_screen.info_label.text = "Il tuo username è "+ self.username

    def assistenza(self):
        self.info_label.text = "Chiama questo numero e arrangiati: +39 800522522"

class ContoCorrente:
    def __init__(self, username):
        self.username = username
        self.iban = self.get_iban_from_csv()
        self.saldo = self.get_saldo_from_csv()

    def get_iban_from_csv(self):
        # Cerca l'IBAN associato all'utente nel DataFrame 'dati'
        dati= pd.read_csv("database.csv")
        row = dati.loc[dati['Username'] == self.username]
        if not row.empty:
            return row['IBAN'].values[0]  # Prendo il valore dell'IBAN dalla riga trovata
        else:
            return  "Non trovato"
    
    def get_saldo_from_csv(self):
        # Cerca l'IBAN associato all'utente nel DataFrame 'dati'
        dati = pd.read_csv("database.csv")
        row = dati.loc[dati['Username'] == self.username]
        if not row.empty:
            return row['Saldo_ContoCorrente'].values[0]  # Prendi il valore del SaldoContoCorrente dalla riga trovata
        else:
            return "Non trovato"
        
    def funzione_show(self,Conto_screen):
        Conto_screen.info_label.text = "Il tuo IBAN:"+str(self.iban)+"e il suo saldo è "+str(self.saldo)

   
class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.info1_label = Label(text='PYMONEY', font_size=100, bold=True, halign='center', valign='middle')
        self.add_widget(self.info1_label)

        self.info_label = Label(text='')
        self.add_widget(self.info_label)

        self.username_input = TextInput(hint_text='Username')
        self.add_widget(self.username_input)

        self.password_input = TextInput(hint_text='Password', password=True)
        self.add_widget(self.password_input)

        self.login_button = Button(text='Accedi', on_press=accedi)            
        self.add_widget(self.login_button)

        self.registra_button = Button(text='Hai dimenticato la Password?', on_press=recupera_pass)   
        self.add_widget(self.registra_button)

        self.registra_button = Button(text='Registrati', on_press=registrazione_utente)   
        self.add_widget(self.registra_button)



class HomeScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.username = ""

        self.info_label = Label(text='Benvenuto!')
        self.add_widget(self.info_label)

        self.ContoCorrente_button = Button(text='Conto Corrente', on_press=self.contocorrente)
        self.add_widget(self.ContoCorrente_button)

        self.risparmi_button = Button(text='Risparmi', on_press=self.risparmi)
        self.add_widget(self.risparmi_button)

        self.Carta_button = Button(text='Carta', on_press=self.carta)
        self.add_widget(self.Carta_button)

        self.premium_button = Button(text='Passa a Premium', on_press=self.passa_a_premium)
        self.add_widget(self.premium_button)

        self.funzioni_button = Button(text='Funzioni Premium', on_press=self.funzioni_premium)
        self.add_widget(self.funzioni_button)

        self.tornaInLogin_button = Button(text='Torna al Login', on_press=self.torna_al_login)
        self.add_widget(self.tornaInLogin_button)

    def torna_al_login(self, instance):
        app.root.current = 'login'

    def passa_a_premium(self, instance):
        username_ins = app.root.get_screen('login').children[0].username_input.text
        dati=pd.read_csv('database.csv')
        riga = dati.loc[dati['Username'] == username_ins].index[0]
        if dati["Premium"][riga] == True:
            self.info_label.text = "Ma sei già Premium!"
        else:
            dati.at[riga, "Premium"] = True
            dati.at[riga, "Saldo_ContoCorrente"] = dati.at[riga, "Saldo_ContoCorrente"]-50

            dati.to_csv("database.csv", index=False)
            self.info_label.text = "Complimenti sei appena passato a Premium! Ti abbiamo appena scalato 50€ dal tuo conto corrente!"

    def funzioni_premium(self, instance):
        dati=pd.read_csv('database.csv')
        username_ins = app.root.get_screen('login').children[0].username_input.text
        riga = dati.loc[dati['Username'] == username_ins].index[0]
        
        if dati["Premium"][riga] == True:
            app.root.current = 'investimenti_screen'
        
        else:
            self.info_label.text = "Non sei premium: per utilizzare questa funzione devi passare a Premium"
          
    def contocorrente(self, instance):
        # Verifica se l'username è disponibile
        if self.username:
            # Crea un'istanza di ContoCorrente con l'username dell'utente corrente
            conto = ContoCorrente(self.username)
            # Creazione di un'istanza di ContoScreen
            conto_screen = ContoScreen()

            # Popolare ContoScreen con le informazioni dell'account corrente
            conto_screen.info_label.text = "Il tuo IBAN: " + str(conto.iban) + " e il suo saldo è " + str(conto.saldo)

            # Cambiare lo screen attuale a 'conto' screen
            app.root.get_screen('conto').clear_widgets()  # Rimuove eventuali widget precedenti
            app.root.get_screen('conto').add_widget(conto_screen)
            app.root.current = 'conto'
        else:
            self.info_label.text = "Effettua l'accesso per visualizzare il conto corrente."
        
    def carta(self, instance):
        app.root.current = 'carta_screen'
    
    def risparmi(self,instance):
        app.root.current = 'risparmi_screen'

class RegistrazioneScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(RegistrazioneScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.info_label = Label(text='Registrati!')
        self.add_widget(self.info_label)

        self.nome_input = TextInput(hint_text='Nome')
        self.add_widget(self.nome_input)

        self.cognome_input = TextInput(hint_text='Cognome')
        self.add_widget(self.cognome_input)

        self.password_input = TextInput(hint_text='Scegli una Password')
        self.add_widget(self.password_input)

        self.registra_button = Button(text='Registra', on_press=self.registra)
        self.add_widget(self.registra_button)

        self.tornaInLogin_button = Button(text='Torna al Login', on_press=self.torna_al_login)
        self.add_widget(self.tornaInLogin_button)

    def registra(self, instance):
        nome = self.nome_input.text
        cognome = self.cognome_input.text
        password = self.password_input.text
        Utente().registrazione(nome, cognome, password, self)

    def torna_al_login(self, instance):
        app.root.current = 'login'

class ContoScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(ContoScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.info_label = Label(text='')
        self.add_widget(self.info_label)

        self.deposito_button = Button(text='Depositare', on_press=self.deposito)
        self.add_widget(self.deposito_button)

        self.tornaInLogin_button = Button(text='Torna alla Home', on_press=self.torna_al_home)
        self.add_widget(self.tornaInLogin_button)

    def torna_al_home(self, instance):
        app.root.current = 'home'

    def deposito(self, instance):
        app.root.current = 'deposito_screen'

class DepositoScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(DepositoScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.info_label = Label(text='Stai effettuando un deposito')
        self.add_widget(self.info_label)
    
        self.importo_input = TextInput(hint_text='Importo del deposito')
        self.add_widget(self.importo_input)

        self.deposito_button = Button(text='Deposita', on_press=self.deposito) 
        self.add_widget(self.deposito_button)

        self.tornaInLogin_button = Button(text='Indietro', on_press=self.torna_al_conto)
        self.add_widget(self.tornaInLogin_button)

    def deposito(self, instance):
        username=app.root.get_screen('login').children[0].username_input.text
        try:
            importo = float(self.importo_input.text)
            if importo > 0:  
                dati = pd.read_csv("database.csv")
                riga = dati.loc[dati['Username'] == username].index[0]
                dati.at[riga, "Saldo_ContoCorrente"] += importo
                dati.to_csv("database.csv", index=False)

                # Aggiorna l'etichetta della schermata attuale
                self.info_label.text = f"Saldo attuale: {dati.at[riga, 'Saldo_ContoCorrente']} €"

                 # Update the 'conto' screen info_label
                conto_screen = app.root.get_screen('conto').children[0]
                conto_screen.info_label.text = f"Il tuo IBAN: {dati.at[riga, 'IBAN']} e il suo saldo è {dati.at[riga, 'Saldo_ContoCorrente']}"

                # Automaticamente veniamo rimandati alla schermata 'conto'
                app.root.current = 'conto'

            else:
                self.info_label.text = "L'importo del deposito deve essere maggiore di zero."
        except ValueError:
            self.info_label.text = "Input non valido. Inserisci un numero valido."

    def torna_al_conto(self, instance):
        app.root.current = 'conto'

class CartaScreen(BoxLayout):
     def __init__(self, **kwargs):
        super(CartaScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.info_label = Label(text='Ecco la tua carta PYMONEY')
        self.add_widget(self.info_label)

        self.info2_label = Label(text='')
        self.add_widget(self.info2_label)

        self.importo_input = TextInput(hint_text='Importo della Ricarica Carta')
        self.add_widget(self.importo_input)

        self.ricarica_button = Button(text='Ricarica Carta prelevando soldi dal tuo conto', on_press=self.ricarica)
        self.add_widget(self.ricarica_button)  

        self.tornaInLogin_button = Button(text='Indietro', on_press=self.torna_alla_home)
        self.add_widget(self.tornaInLogin_button)

     def torna_alla_home(self, instance):
        app.root.current = 'home'
     
     def ricarica(self, instance):
        username=app.root.get_screen('login').children[0].username_input.text                   
        try:
            importo = float(self.importo_input.text)
            dati = pd.read_csv("database.csv")
            riga = dati.loc[dati['Username'] == username].index[0]
            if 0 < importo and importo<dati.at[riga, "Saldo_ContoCorrente"]:
                dati = pd.read_csv("database.csv")
                riga = dati.loc[dati['Username'] == username].index[0]
                dati.at[riga, "Saldo_ContoCorrente"] -= importo
                dati.at[riga, "Saldo_Carta"] += importo
                dati.to_csv("database.csv", index=False)

                # Aggiorna l'etichetta della schermata attuale
                self.info_label.text = f"Hai effettuato una Ricarica di {importo} €"
                self.info2_label.text= "Il tuo saldo carta attuale è "+ str(dati.at[riga, "Saldo_Carta"])

                # Update the 'conto' screen info_label
                conto_screen = app.root.get_screen('conto').children[0]
                conto_screen.info_label.text = f"Il tuo IBAN: {dati.at[riga, 'IBAN']} e il suo saldo è {dati.at[riga, 'Saldo_ContoCorrente']}"

            else:
                self.info_label.text = "Il tuo saldo è insufficiente, non puoi prelevare questa cifra!"
        except ValueError:
            self.info_label.text = "Input non valido. Inserisci un numero valido."
     
class RisparmiScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(RisparmiScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.info_label = Label(text='Gestione Risparmi')
        self.add_widget(self.info_label)

        self.aggiungi_risparmio_button = Button(text='Aggiungi Risparmio', on_press=self.aggiungi_risparmio)
        self.add_widget(self.aggiungi_risparmio_button)

        self.monitora_risparmio_button = Button(text='Monitoraggio', on_press=self.monitoraggio)
        self.add_widget(self.monitora_risparmio_button)

        self.tornaInHome_button = Button(text='Torna alla Home', on_press=self.torna_alla_home)
        self.add_widget(self.tornaInHome_button)
    
    def aggiungi_risparmio(self, instance):
        # Apri una schermata per aggiungere un nuovo risparmio
        popup = AggiungiRisparmioPopup()
        popup.bind(on_dismiss=self.aggiorna_database_risparmi)  #aggiorna quando la pop up si chiude
        popup.open()

    def aggiorna_database_risparmi(self, instance):
        # Aggiorna la lista dei risparmi quando viene chiusa la popup per aggiungere un nuovo risparmio
        risparmi = pd.read_csv("risparmi.csv")
        username = app.root.get_screen('login').children[0].username_input.text
        riga = risparmi.loc[risparmi['Username'] == username].index[0]

        # Recupera le informazioni sui risparmi dell'utente dal DataFrame
        # Assumiamo che il DataFrame contenga colonne chiamate 'Categoria', 'Obiettivo', e 'Progresso'
        risparmi_df = risparmi.loc[riga, ['Risparmio','Categoria','Obiettivo']]

    def torna_alla_home(self, instance):
        app.root.current = 'home'     
     
    def monitoraggio(self, instance):
        app.root.current = 'monitoraggio' 
    
class AggiungiRisparmioPopup(Popup):
    def __init__(self, **kwargs):
        super(AggiungiRisparmioPopup, self).__init__(**kwargs)
        self.title = 'Aggiungi Risparmio'
        self.size_hint = (0.8, 0.8)

        # Creazione di widget per inserire i dettagli del nuovo risparmio
        self.alert = Label(text='')

        self.importo_input = TextInput(hint_text='Importo Risparmio')
        self.categoria_input = TextInput(hint_text='Categoria')
        self.obiettivo_input = TextInput(hint_text='Obiettivo')
              
        self.salva_button = Button(text='Salva', on_press=self.salva_risparmio)
        self.annulla_button = Button(text='Indietro', on_press=self.dismiss)

        # Creazione di un layout per organizzare i widget
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.categoria_input)
        layout.add_widget(self.importo_input)
        layout.add_widget(self.obiettivo_input)
        layout.add_widget(self.alert)
        layout.add_widget(self.salva_button)
        layout.add_widget(self.annulla_button)

        self.content = layout

    def salva_risparmio(self, instance):
        # Recupera i dati inseriti dall'utente
        categoria = self.categoria_input.text
        obiettivo = self.obiettivo_input.text
        username = app.root.get_screen('login').children[0].username_input.text
        importo = float(self.importo_input.text)
        dati = pd.read_csv("database.csv")
        rigad = dati.loc[dati['Username'] == username].index[0]

        if importo > float(obiettivo): 
            self.alert.text = 'Non puoi inserire un risparmio con obiettivo minore del risparmio'
        elif importo > float(dati.at[rigad, "Saldo_ContoCorrente"]):
            self.alert.text = 'Non puoi inserire questo risparmio perchè non hai abbastanza soldi sul Conto Corrente'
        else:               
            risparmio = pd.read_csv("risparmi.csv")            
            if username in list(risparmio["Username"]):
                riga=risparmio.loc[(risparmio['Username'] == username) & (risparmio['Categoria'] == categoria)]
                if not riga.empty:
                    riga=riga.index[0]
                    risparmio.at[riga, 'Categoria'] = categoria
                    risparmio.at[riga, 'Obiettivo'] = obiettivo
                    risparmio.at[riga, 'Risparmio'] += importo
                    dati.at[rigad, 'Saldo_ContoCorrente'] -= importo
                    dati.at[rigad, 'Saldo_Risparmi'] += importo
                    dati.to_csv("database.csv", index=False)
                    risparmio.to_csv("risparmi.csv", index=False)
                    self.dismiss()

                else:
                    aggiornamento_database(username,categoria,obiettivo,importo)
                    dati.at[rigad, 'Saldo_ContoCorrente'] -= importo
                    dati.at[rigad, 'Saldo_Risparmi'] += importo
                    dati.to_csv("database.csv", index=False)
                    # Chiudi la popup e aggiorna la lista dei risparmi nella schermata principale
                    self.dismiss()
            else:
                aggiornamento_database(username,categoria,obiettivo,importo)
                # Chiudi la popup e aggiorna la lista dei risparmi nella schermata principale
                dati.at[rigad, 'Saldo_ContoCorrente'] -= importo
                dati.at[rigad, 'Saldo_Risparmi'] += importo
                dati.to_csv("database.csv", index=False)
                self.dismiss()
            
class InvestimentiScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(InvestimentiScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.info_label = Label(text='Previsione del tuo prossimo investimento')
        self.add_widget(self.info_label)

        self.info2_label = Label(text='Seleziona correttamente il rischio di investimento: 1-rischio basso, 2-rischio medio, 3-rischio alto')
        self.add_widget(self.info2_label)

        self.info3_label = Label(text='')
        self.add_widget(self.info3_label)

        self.capitale_input = TextInput(hint_text='Quanto capitale vorresti investire?')
        self.add_widget(self.capitale_input)

        self.rischio_input = TextInput(hint_text='Seleziona il rischio di investimento: 1-rischio basso, 2-rischio medio, 3-rischio alto')                                      
        self.add_widget(self.rischio_input)

        self.previsione_button = Button(text='Prevedi rendimento', on_press=self.previsione)
        self.add_widget(self.previsione_button)  

        self.investimento_button = Button(text='Investi', on_press=self.investimento)
        self.add_widget(self.investimento_button)  

        self.indietro_button = Button(text='Indietro', on_press=self.torna_alla_home)
        self.add_widget(self.indietro_button)  

    def torna_alla_home(self, instance):
        app.root.current = 'home'
        
    def previsione(self, instance):
        self.lista_esiti=[-0.01,-0.02,-0.03,-0.04,-0.05,-0.06,-0.07,-0.08,-0.09,-0.10,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.10]
        self.fattore_esito=random.choice(self.lista_esiti)

        self.capitale=float(self.capitale_input.text)
        
        if self.rischio_input.text == "1":
            self.capitale+= self.capitale*float(self.fattore_esito)*1.1
            self.info2_label.text = "Il tuo investimento potrebbe avere un rendimento: "
            self.info3_label.text = str(self.capitale)
        elif self.rischio_input.text == "2":
            self.capitale+= self.capitale*float(self.fattore_esito)*1.2
            self.info2_label.text = "Il tuo investimento potrebbe avere un rendimento: "
            self.info3_label.text = str(self.capitale)
        elif self.rischio_input.text == "3":
            self.capitale+= self.capitale*float(self.fattore_esito)*1.3
            self.info2_label.text = "Il tuo investimento potrebbe avere un rendimento: "
            self.info3_label.text = str(self.capitale)
        else: 
            self.info2_label.text = "Inserisci un valido fattore di rischio"
            self.info3_label.text = ""
    
    def investimento(self,instance):
        dati = pd.read_csv("database.csv")
        capitale = app.root.get_screen('investimenti_screen').children[0].info3_label.text  
        username = app.root.get_screen('login').children[0].username_input.text
        riga=dati.loc[(dati['Username'] == username)]
        riga=riga.index[0]
        if float(capitale) > float(dati.at[riga, 'Saldo_ContoCorrente']):
            app.root.get_screen('investimenti_screen').children[0].info3_label.text  = "NON PUOI PROCEDERE CON L'INVESTIMENTO! Non hai abbastanza capitale nel Conto Corrente"
        else:
            dati.at[riga, 'Saldo_ContoCorrente'] += float(capitale)
            dati.at[riga, 'Saldo_Investimenti'] += float(capitale)
            dati.to_csv("database.csv", index=False)
            app.root.get_screen('investimenti_screen').children[0].info3_label.text  = "INVESTIMENTO ANDATO A BUON FINE! Controlla il tuo Conto Corrente"
    


                     
class MonitoraggioScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MonitoraggioScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.info_label = Label(text='Monitoraggio dei tuoi risparmi')
        self.add_widget(self.info_label)

        self.info2_label = Label(text='')
        self.add_widget(self.info2_label)

        self.categoria_input = TextInput(hint_text='Inserisci la categoria di cui vuoi visualizzare i risparmi')
        self.add_widget(self.categoria_input)

        self.avviamoMonitoraggio_button = Button(text='Avvia monitoraggio', on_press=self.monitoraggio)
        self.add_widget(self.avviamoMonitoraggio_button)

        self.indietro_button = Button(text='Torna alla Home', on_press=self.torna_alla_home)
        self.add_widget(self.indietro_button)

    def torna_alla_home(self, instance):
        app.root.current = 'home'

    def monitoraggio(self, instance):
        df = pd.read_csv("risparmi.csv")
        username = app.root.get_screen('login').children[0].username_input.text

        # Verifica se lo username è presente nella colonna "username"
        if username not in df["Username"].values:
            app.root.get_screen('monitoraggio').children[0].info_label.text = "Non hai nessun risparmio attivo"
        else:             
            # Filtra il DataFrame per ottenere solo i dati relativi allo username specificato
            user_data = df[df["Username"] == username]

            # Ottieni l'elenco dei nomi di salvadanaio associati a quello username
            nomi_salvadanai = user_data["Categoria"] # nel caso possano esistere più salvadanai con lo stesso nome per lo stesso username, bisogna aggiungere un ".unique()" alla fine di questa riga

            self.categoria=self.categoria_input.text

            if self.categoria not in list(nomi_salvadanai):
                 app.root.get_screen('monitoraggio').children[0].info_label.text = "Inserisci il nome esatto del salvadanaio che vuoi monitorare tra i seguenti:\n" + "\n".join(nomi_salvadanai) + "\n"
                 app.root.get_screen('monitoraggio').children[0].info_label.halign = 'center'
            else:
                # Filtra il DataFrame per ottenere i dati relativi al nome del salvadanaio scelto
                salvadanaio_data = user_data[user_data["Categoria"] == self.categoria]

                # Calcola la percentuale e arrotondala a 2 decimali
                self.percentuale = round(float(salvadanaio_data["Risparmio"]) / float(salvadanaio_data["Obiettivo"]) * 100, 2)
                if self.percentuale>100:
                    # Stampa il risultato
                     app.root.get_screen('monitoraggio').children[0].info2_label.text = "Hai raggiunto il tuo obiettivo al " + str(self.percentuale) + "%"
                     popup = EliminaRisparmioPopup()
                     popup.open()
                else:
                    app.root.get_screen('monitoraggio').children[0].info2_label.text = "Percentuale del salvadanaio " +  self.categoria + ": " + str(self.percentuale) + "%" 
    
class EliminaRisparmioPopup(Popup):
    def __init__(self, **kwargs):
        super(EliminaRisparmioPopup, self).__init__(**kwargs)
        self.title = 'Hai raggiunto il tuo obiettivo su questo risparmio, vuoi eliminarlo dalla lista dei tuoi risparmi?'
        self.size_hint = (0.8, 0.8)
              
        self.info_label = Label(text='Hai raggiunto il tuo obiettivo, vuoi eliminare il tuo risparmio?')
        self.add_widget(self.info_label)

        self.salva_button = Button(text='Elimina risparmio', on_press=self.elimina)
        self.annulla_button = Button(text='Indietro', on_press=self.dismiss)

        # Creazione di un layout per organizzare i widget
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.salva_button)
        layout.add_widget(self.annulla_button)

        self.content = layout

    def elimina(self, instance):
        risparmio = pd.read_csv("risparmi.csv")
        # Recupera i dati inseriti dall'utente
        username = app.root.get_screen('login').children[0].username_input.text
        categoria = app.root.get_screen('monitoraggio').children[0].categoria_input.text
        riga=risparmio.loc[(risparmio['Username'] == username) & (risparmio['Categoria'] == categoria)]
        risparmio.drop(riga.index, inplace=True)
        risparmio.to_csv("risparmi.csv", index=False)
        self.dismiss()


    
            



class PyMoney(App):
    def build(self):
        # Creazione del Gestore dello Schermo
        sm = ScreenManager()

        # Creazione degli Schermi
        # Schermata di Login
        login_screen = Screen(name='login')
        login_layout = LoginScreen()
        login_layout.background_color = (1, 0, 0, 1)
        login_screen.add_widget(login_layout)
        sm.add_widget(login_screen)

        # Schermata di Home
        home_screen = Screen(name='home')
        home_layout = HomeScreen()
        home_screen.add_widget(home_layout)
        sm.add_widget(home_screen)

        # Schermata di Registrazione
        registrazione_screen = Screen(name='registrazione')
        registrazione_layout = RegistrazioneScreen()
        registrazione_screen.add_widget(registrazione_layout)
        sm.add_widget(registrazione_screen)

        # Schermata del Conto corrente
        Conto_screen = Screen(name='conto')
        Conto_layout = ContoScreen()
        Conto_screen.add_widget(Conto_layout)
        sm.add_widget(Conto_screen)

        # Schermata di Deposito
        deposito_screen = Screen(name='deposito_screen')
        deposito_layout = DepositoScreen()
        deposito_screen.add_widget(deposito_layout)
        sm.add_widget(deposito_screen)

        # Schermata di Carta
        carta_screen = Screen(name='carta_screen')
        carta_layout = CartaScreen()
        carta_screen.add_widget(carta_layout)
        sm.add_widget(carta_screen)

        # Schermata di Risparmi
        risparmi_screen = Screen(name='risparmi_screen')
        risparmi_layout = RisparmiScreen()
        risparmi_screen.add_widget(risparmi_layout)
        sm.add_widget(risparmi_screen)

        # Schermata di Investimenti
        investimenti_screen = Screen(name='investimenti_screen')
        investimenti_layout = InvestimentiScreen()
        investimenti_screen.add_widget(investimenti_layout)
        sm.add_widget(investimenti_screen)

        # Schermata di Monitoraggio
        monitoraggio_screen = Screen(name='monitoraggio')
        monitoraggio_layout = MonitoraggioScreen()
        monitoraggio_screen.add_widget(monitoraggio_layout)
        sm.add_widget(monitoraggio_screen)

        return sm


if __name__ == '__main__':
    app = PyMoney()
    app.run()