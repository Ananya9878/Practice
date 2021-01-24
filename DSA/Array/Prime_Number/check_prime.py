prime = [2,3]
def isPrime(n):
    i = 0
    while prime[i]<= n**0.5:
        if n%prime[i] == 0:
            return False
        i+=1
    return True

def allPrime(n):
    for i in range(prime[-1]+1,n):
        if isPrime(i):
            prime.append(i)

def sieve(n):
    p = [True]*(n+1)
    for i in range(2,n):
        if p[i]:
            t = i+i
            while t < n:
                p[t] = False
                t+=i
    print(p)



# n = 100
# allPrime(n)
# print(prime)
# print(len(prime))
(sieve(100))








