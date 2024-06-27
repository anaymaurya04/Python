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
x=123
rev=0
while x>0:
    ld=x%10
    x=x//10
    rev= (rev*10)+ld
print(rev)
    