#først må vi få alle verdiene som input
befolkning = int(input("Hva er den nÃ¥vÃ¦rende befolkningen? "))
p = float(input("Hva er den prosentvise endringen? "))
t = int(input("Hvor mange Ã¥r gÃ¥r det? "))

#en løkke som gjentar seg like mange ganger som antall år
for x in range(t):
    befolkning = befolkning * (1 + p / 100)

#printe svaret
print("Etter " + str(t) + " Ã¥r er ligger befolkningen pÃ¥ omtrentlig " + str(befolkning) + " dyr. ")