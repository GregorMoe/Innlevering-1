#f�rst m� vi f� alle verdiene som input
befolkning = int(input("Hva er den nåværende befolkningen? "))
p = float(input("Hva er den prosentvise endringen? "))
t = int(input("Hvor mange år går det? "))

#en l�kke som gjentar seg like mange ganger som antall �r
for x in range(t):
    befolkning = befolkning * (1 + p / 100)

#printe svaret
print("Etter " + str(t) + " år er ligger befolkningen på omtrentlig " + str(befolkning) + " dyr. ")