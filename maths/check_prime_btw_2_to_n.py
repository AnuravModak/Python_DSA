def check_prime_in_range(n):# time-complexity:O(nlogn)
    sieve=[0]*(n+2)
    sieve[0]=-1
    sieve[1]=-1
    for i in range(2,n+1):
        if sieve[i]==0:
            for j in range(2*i,n+1,i):
                sieve[j]=1
                j+=i
    # print(sieve)
    for i in range(len(sieve)-1):
        if sieve[i]==0:
            print(i)
def return_smallest_factor(n):
    sieve=[0]*(n+2)
    sieve[0]=-1
    sieve[1]=-1
    for i in range(len(sieve)-1):
        if sieve[i]==0:
            for j in range(2*i,n+1,i):
                if sieve[j]==0:
                    sieve[j] = i
    for i in range(len(sieve)-1):
        if sieve[i]>0:
            print("Smallest factor of {} is {}".format(i,sieve[i]))








if __name__ == '__main__':
    check_prime_in_range(20)
    print()
    return_smallest_factor(20)
