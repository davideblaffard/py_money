import random
capitale=int(input("Quanto capitale vuoi investire?:\n"))
#metodo che leva il capitale dal conto corrente
scelta_rischio=int(input("Seleziona rischio dell'investimento:\n1)Rischio basso\n2)Rischio medio\n3)Rischio elevato\n"))
while scelta_rischio!=1 and scelta_rischio!=2 and scelta_rischio!=3:
    scelta_rischio=int(input("Seleziona rischio dell'investimento:\n1)Rischio basso\n2)Rischio medio\n3)Rischio elevato"))
#ad un rischio crescente corrispondono guadagni o perdite proporzionate
if scelta_rischio==1:
    fattore_rischio=1.1
if scelta_rischio==2:
    fattore_rischio=1.2
if scelta_rischio==3:
    fattore_rischio=1.3
print(f"Il tuo fattore di rischio è {fattore_rischio}")
#scelgo un esito random dell'investimento
lista_esiti=[-0.01,-0.02,-0.03,-0.04,-0.05,-0.06,-0.07,-0.08,-0.09,-0.10,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.10]
fattore_esito=random.choice(lista_esiti)
if fattore_esito>0:
    print("Il tuo investimento ha avuto un rendimento positivo")
else:
    print("Il tuo investimento ha avuto un rendimento negativo")

capitale+=capitale*fattore_esito*fattore_rischio
print(f"Il tuo capitale adesso è di\n{capitale} euro")
#metodo che aggiunge l'ammontare di capitale al conto corrente


#torna alla home