def sortColors(nums):
    #BruteForce(Sorting)
    n=len(nums)
    for i in range (n):
        for j in range(0,n-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums 

def sortColorsHashmaps(nums):
    #Optimised(HashMaps)
    color_count={0:0,1:0,2:0}
    for num in nums:
        color_count[num] += 1
    index = 0
    for color in range(3):
        count = color_count[color]
        for _ in range(count):
            nums[index]=color
            index +=1
