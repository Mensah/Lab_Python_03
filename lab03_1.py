n = 50

primes = 0

possible_prime = 2

while primes < n:
    divisors = 0
    for i in range(1,possible_prime+1):
        if possible_prime % i == 0:
            divisors +=1

    if divisors == 2:
        print possible_prime,
        primes +=1

        if primes % 10 == 0:
            print

    possible_prime =+1
