def fakultet(n): #f�rst lager vi en funksjon som ganger sammen alle heltallene mellom n og 0 ved � kalle p� seg selv
    if n == 0:
        return 1
    else:
        return n * fakultet(n-1)
try: #her bruker vi en try slik at programmet ikke stopper hvis det kommer en feilmelding
    print("Fakulteten er", fakultet(int(input("Hva vil du beregne fakulteten av? "))))
except ValueError: #hvis en ValueError (f.eks. hvis den pr�ver � gj�re et desimaltall eller en bokstav til et heltall)
    print("Man kan kun beregne fakulteten av naturlige tall. ")