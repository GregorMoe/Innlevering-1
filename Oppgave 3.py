befolkning = int(input("Hva er den nåværende befolkningen? "))
p = float(input("Hva er den prosentvise endringen? "))
t = int(input("Hvor mange år går det? "))

for x in range(t):
    befolkning = befolkning * (1 + p / 100)

print("Etter " + str(t) + " år er ligger befolkningen på omtrentlig " + str(befolkning) + " dyr. ")