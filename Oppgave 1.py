import math #importerer math for å beregne den briggske logaritmen

pH = float(input("Antall H+-ioner oppgitt som mol per liter: ")) #får input
pH = math.log10(pH) * -1 #beregner pH basert på inputet

if pH >= 0 and pH < 7: #
    print("Løsningen har pH " + str(pH) + " og er dermed sur.")
elif pH == 7:
    print("Løsningen har pH 7 og er dermed nøytral.")
elif pH > 7 and pH <= 14:
    print("Løsningen har pH " + str(pH) + " og er dermed basisk.")