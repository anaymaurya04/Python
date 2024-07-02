'''
n=5
count = 0
original_n = n
while n > 0:
    x = n % 10
    if x != 0 and original_n % x == 0:  
        count += 1
    n = n // 10 
print(count)
'''
def reverse(x):
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        rev=0
        sign=1
        if x<0:
            sign=-1
            x=-x
        while x>0:
            if rev>MAX_INT/10 or rev<MIN_INT/10:
                return 0
            ld= x%10
            x=x//10
            rev=(rev*10)+ld
        rev=rev*sign
        return rev


def divisor(x):
    sum = 0
    for i in range(1, x + 1):
        if x % i == 0:
            sum += i
    return sum


def print_numbers(n, current=1):
    if current > n:
        return
    print(current)
    print_numbers(n, current + 1)


n=10
def Nto1(n):
    print(n)
    if n>0:
        n=n-1
        Nto1(n)


# class Solution:
#     def printNos(self, n):
#         print(n)
#         if n>0:
#             n=n-1
#             printNos(self,n)

def factorialNumbers( n):
    result = []
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        if (factorial > n):
            break
        else:
            result.append(factorial)
    return result

