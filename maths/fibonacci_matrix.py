# This relies on the fact that if we n times multiply the matrix M = {{1,1},{1,0}} to itself
# (in other words calculate power(M, n)), then we get the (n+1)th Fibonacci number as
# the element at row and column (0, 0) in the resultant matrix.
# run the debugger and see the working of code ou will ans
def fib(n):
    F = [[1, 1],
         [1, 0]]
    if (n == 0):
        return 0
    power(F, n - 1)

    return F[0][0]
def multiply(F,M):
    # this is manual multiplication of a matrix
    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

def power(F,n):
    if n==0 or n==1:
        return
    M=[[1,1],[1,0]]
    power(F,n//2) # now this will do the job for all multiples of 2
    multiply(F,F)

    if n%2!=0:
        multiply(F,M)

if __name__ == '__main__':
    print(fib(9))
