n=5
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()
print("\n")


for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print()

print("\n")

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end = " ")
    print()

print("\n")

for i in range(0,n):
    for j in range(i,n):
        print("*",end="")
    print()

print()

for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()

for i in range(n):
    for j in range(i):
        print(" ", end="")
    for j in range(2*(n-i)-1):
        print("*", end="")
    print()

for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    print()
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

print()

count=1
for i in range(n):
    for j in range(i + 1):
        print(count%2,end="")
        count+=1
    print()

for i in range(n):
    for j in range(i + 1):
        if (i + j) % 2 == 0:
            print(1, end="")
        else:
            print(0, end="")
    print()

print()

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end="")
    for j in range(2*(n-i)):
        print(" ",end="")
    for j in range(i,0,-1):
        print(j,end="")
    print()

print()

count=1
for i in range(n):
    for j in range(i+1):
        print(count, end=" ")
        count+=1
    print()

print()

char=65
for i in range(n):
    for j in range(i + 1):
        print(chr(char+j), end="")
    print()

print()
char=65
for i in range(n,0,-1):
    for j in range(0,i):
        print(chr(char+j), end="")
    print()

for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(i+1):
        print(chr(char+j),end="")
    for j in range(i):
        print(chr(char + i - j - 1), end="")
    for j in range(n-i-1):
        print(" ", end="")
    print()

print()

char=65
for i in range(n):
    for j in range(char + n - 1 - i, char + n):
        print(chr(j),end="")
    print()
