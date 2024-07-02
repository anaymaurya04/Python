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

def printArr(arr,n):
    print("The reverse array is:")
    for i in range(n):
        print(arr[i], end="")
    print()

def reverseArray(arr,n):
    ans = [0]*n
    for i in range(n-1,-1,-1):
        ans[n-i-1]=arr[i]
    printArr(ans,n)

def checkpalindrome(s):
    for i in range(len(s)):
        ans = [0]*len(s)
        for i in range(len(s)-1,-1,-1):
            ans[len(s)-i-1]=s[i]
            if ans == s:
                return True
            else:
                return False
s="gig"            
print(checkpalindrome(s))
