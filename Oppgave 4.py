'''
try:
    n = int(input("Hva vil du ha fakultet til? ")) #spør hva vi skal finne fakultet til
    if n >= 0:
        fakultet = 1 #vi må definere variabelen fakultet, og hvis vi hadde gjort det inni løkken ville det gått galt
        for x in range(1,n+1): #en for-løkke fra 1 til n+1, hvor vi ganger variabelen fakultet med alle tallene mellom 1 og n(inkludert n)
            fakultet = fakultet * x
        print("Fakulteten til " + str(n) + " er " + str(fakultet) + ". ")
    else: #hvis tallet ikke er >= null
        print("Tallet du vil beregne fakulteten til må være over eller lik 0. ")
except ValueError: #hvis det ikke funker å konvertere inputen til et integer
    print("Man kan beregne fakultet til naturlige tall. ")
'''

def fakultet(n):
    if n == 0:
        return 1
    else:
        return n * fakultet(n-1)
try:
    print("Fakulteten er", fakultet(int(input("Hva vil du beregne fakulteten av? "))))
except ValueError:
    print("Man kan kun beregne fakulteten av naturlige tall. ")