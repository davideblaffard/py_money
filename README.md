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

**Previsione investimenti**

Nella schermata della home come funzione premium c'è la possibilità di prevedere un investimento.

Dopo aver selezionato un livello di rischio e una somma da investire il programma simula un investimento che può avere un esito negativo o positivo.

