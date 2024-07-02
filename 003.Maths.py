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


