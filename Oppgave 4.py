try:
    n = int(input("Hva vil du ha fakultet til? "))
    if n >= 0:
        a = 1
        for x in range(1,n+1):
            a = a * x
        print("Fakulteten til " + str(n) + " er " + str(a) + ". ")
    else:
        print("Tallet du vil beregne fakulteten til må være over eller lik 0. ")
except ValueError:
    print("Man kan beregne fakultet til naturlige tall. ")
