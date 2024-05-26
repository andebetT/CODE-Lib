#this program is used to find the prime numbers useing Sieve of Eratosthenes | Fastest way for Prime Number finding
def sieve_algorithm(numbers):
    prime_arr=[1]*(numbers+1)
    prime_arr[0]=0
    prime_arr[1]=0
    for i in range(2,int(numbers**0.5)+1):
        if prime_arr[i]==1:
            j=2
            while i*j<numbers+1:
                prime_arr[i*j]=0
                j+=1
    return prime_arr
print(sieve_algorithm(15))


