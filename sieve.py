
def sieve_of_eratosthenes(n:int) :
    prime = [True for i in range(n + 1)]
    p = 2
    while ( p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] =  False

        p += 1
    # prime[0] = False
    # prime[1] = False 

    for p in range(n + 1):
        if prime[p]:
            print(p)

if __name__ == '__main__':
    n = 30
    n = int(input("Enter a number to calculate up to: "))
    print(f'All prime numbers up to {n}',)
    sieve_of_eratosthenes(n)