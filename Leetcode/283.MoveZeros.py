def moveZeros(nums):
    zero_arr = []
    i=0
    while i<len(nums):
        if nums[i] == 0:
            nums.pop(i)
            zero_arr.append(0)
        else:
            i+=1
    arr= zero_arr + nums
    return arr

def Movezeros(nums):
    j=-1

a=[0,1,3,5,1,0,0,1,0]
print(moveZeros(a))