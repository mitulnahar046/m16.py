n = int(input("ENter a number (try 4 or 6): "))
guess = input("Is " + str(n) + "a power of 2? (yes/no)")
input("Power of 2: n & (n-1) == 0 means only one bbit is ON. press enter")
if n > 0 and(n & (n-1)) == 0:
    print(" ", n," binary:", bin(n)[2:], " power of 2: yes your guess:", guess)
else:
    print(" ", n," binary:", bin(n)[2:], " power of 2: not your guess:", guess)