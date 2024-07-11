def rotate(nums, k):
        n = len(nums)
        k = k % n
        arr = nums[-k:]+nums[:-k]
        for i in range (n):
                nums[i] = arr[i]
        return arr
a=[1,2,3,4,5,6]
print(rotate(a,43))


def rotate_reverse(nums,k):
        n = len(nums)
        k = k % n
        def reverse(start,end):
                while start < end:
                    nums[start], nums[end] = nums[end], nums[start]
                    start +=1
                    end -=1
                
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k,n-1)
        return nums
a=[1,2,3,4,5,6]
print(rotate_reverse(a,43))