# py_money
[ER_money.pdf](https://github.com/DavideB98/py_money/files/12079549/ER_money.pdf)

![ER_money](https://github.com/DavideB98/py_money/assets/24292409/bc17ca43-ed1a-4445-9544-743d45b8aa26)

# Coding Rules

## Indentazione e formattazione

Abbiamo scelto di utilizzare il tipo di indentazione con la singola tabulazione. Per mantenere la leggibilità del codice ed evitare lo scorrimento in orizzontale abbiamo deciso di mantenere ogni riga del codice al di sotto dei 79 caratteri.

## Nomenclatura

La scelta della nomenclatura si attiene agli standard di Python. Abbiamo utilizzato dei nomi descrittivi e ci siamo astenuti dall’utilizzo di nomi riservati per definire variabili, funzioni e classi.

Abbiamo utilizzato la convenzione snake case per i nomi delle variabili e il camel case per i nomi delle variabili e dei metodi.

## Commenti

Il codice è provvisto di commenti che forniscono spiegazioni sulle parti più complesse e definiscono la funzione della fase del programma che sta leggendo

## Definizione degli errori

LOGIN/REGISTRAZIONE:  

MENU: Nel caso in cui l’utente non selezionasse nessuna opzione del menù(numero maggiore di 6 o qualunque altro carattere) viene stampato RIPROVA fino a quando in input non viene inserita una scelta valida

## Organizzazione dei files

Prevediamo di dividere il codice in diversi file per aumentarne la leggibilità e di allegare un file csv, che il programma leggerà per il controllo degli registro utenti

## **PYMONEY**

Pymoney è una applicazione che consente di gestire il proprio denaro.

**Funzionalità di Pymoney**
 - Gestione registrazione e accessi
 - Gestione carta e risparmi
 - Previsione investimenti
 
 **Gestione registrazione e accessi**
 
Nella schermata iniziale di Pymoney è possibile accedere o registrarsi nel sistema.
Gli accessi e i login sono gestiti tramite un file CSV in cui sono presenti gli username e le password degli utenti.

**Gestione conto, risparmi e carta**

Nella schermata  home è possibile accedere e svolgere operazioni sul proprio conto corrente , la propria carta e creare diversi salvadanai in cui vengono allocati diverse somme in vista del raggiungimento di un obiettivo  scelto dall'utente.

Dopo aver creato e definito un obiettivo per il proprio salvadanaio è anche possibile monitorare i progressi in funzione dell'obiettivo prestabilito.

# Struttura del Codice
 Il codice è un'applicazione basata su Kivy per la gestione di un'app chiamata *PyMoney* che gestisce i risparmi e fondi personali.

1.  **Import delle librerie**: sono state importate tutte le librerie necessarie per l'applicazione Kivy, insieme ad altre librerie come `random`, `csv` e `pandas` per gestire i dati e i file CSV.
    
2.  **Caricamento dei dati**: Viene letto il file CSV "database.csv" utilizzando pandas e memorizzato in un DataFrame chiamato "dati". Questo DataFrame conterrà le informazioni sugli utenti registrati e i loro dati finanziari.
       
3.  **Definizione delle classi**: Sono state definite diverse classi, alcune di queste rappresentano le schermate dell'applicazione e altre sono servite per la stesura del codice. 
    
	Le classi principali sono:
	-   `Utente`: Rappresenta un utente dell'applicazione con i campi "nome", "cognome", "username" e "password". Ha metodi per la registrazione dell'utente, la creazione dell'username e l'assistenza.
	    
	-   `ContoCorrente`: Rappresenta il conto corrente di un utente, con campi per l'username, l'IBAN e il saldo. Ha metodi per ottenere l'IBAN e il saldo dal file CSV.
	    
	-   `LoginScreen`: Rappresenta la schermata di accesso all'applicazione con campi di input per username e password, oltre ai pulsanti di accesso e registrazione.
	    
	-   `HomeScreen`: Rappresenta la schermata principale dopo il login, con diverse opzioni per il conto corrente, il monitoraggio dei risparmi, la carta, gli investimenti, etc.
	    
	-   `RegistrazioneScreen`: Rappresenta la schermata di registrazione con campi di input per il nome, il cognome e la password.
	    
	-   `ContoScreen`: Rappresenta la schermata del conto corrente con opzioni per depositare denaro.
	    
	-   `DepositoScreen`: Rappresenta la schermata di deposito di denaro sul conto corrente.
	    
	-   `CartaScreen`: Rappresenta la schermata della carta con opzioni per ricaricare la carta prelevando denaro dal conto corrente.
	    
	-   `RisparmiScreen`: Rappresenta la schermata di gestione dei risparmi con opzioni per aggiungere un nuovo risparmio o monitorarne uno esistente.
	    
	-   `InvestimentiScreen`: Rappresenta la schermata di previsione degli investimenti con opzioni per inserire il capitale e il rischio.
	    
	-   `MonitoraggioScreen`: Rappresenta la schermata di monitoraggio dei risparmi con opzioni per inserire la categoria dei risparmi da visualizzare.
	    
	-   `AggiungiRisparmioPopup`: Rappresenta una popup per aggiungere un nuovo risparmio, con campi per la categoria, l'obiettivo e l'importo del risparmio.
    

5.  **Costruzione dell'app:** La classe `PyMoney` eredita da `App` ed è responsabile della costruzione dell'app. Vengono creati oggetti per ogni schermata e aggiunti al `ScreenManager`, che gestirà le transizioni tra le diverse schermate. L'app viene avviata usando la funzione  `run()`.
    

Complessivamente, l'applicazione *PyMoney* è progettata per consentire agli utenti di registrarsi, accedere, gestire il loro conto corrente, visualizzare e monitorare i loro risparmi e fare previsioni sugli investimenti.











**Previsione investimenti**

Nella schermata della home come funzione premium c'è la possibilità di prevedere un investimento.

Dopo aver selezionato un livello di rischio e una somma da investire il programma simula un investimento che può avere un esito negativo o positivo.

