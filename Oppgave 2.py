import math

variabel = input("Hvilken variabel vil du finne? (E, m, v) ") #spør hvilken variabel som er den ukjente

if variabel == "E": #spør om de to kjente variablene og beregner den ukjente. printer den ukjente
    m = float(input("Hva er massen (m) til objektet oppgitt i kg? "))
    v = float(input("Hva er farten (v) til objektet oppgitt i m/s? "))
    E = m * v**2 / 2
    print("Den kinetiske energien til objektet er " + str(e) + " J. ")
elif variabel == "m":
    v = float(input("Hva er farten (v) til objektet oppgitt i m/s? "))
    E = float(input("Hva er den kinetiske energien til objektet i J? "))
    m = 2 * E / v**2
    print("Massen til objektet er " + str(m) + " kg. ")
elif variabel == "v":
    E = float(input("Hva er den kinetiske energien til objektet i J? "))
    m = float(input("Hva er massen til objektet i kg? "))
    v = math.sqrt(2 * E / m)
    print("Farten til objektet er " + str(v) + " m/s. ")
else: #hvis inputet ikke var E, m eller v
    print("Noe du skrev inn var feil. Husk at Python er case-sensitive! ")