def twoSum(nums, target):
    # Create a dictionary to store the complement of each number and its index
    complement_map = {}
    
    # Iterate over the list of numbers
    for index, num in enumerate(nums):
        # Calculate the complement
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in complement_map:
            # Return the indices of the two numbers
            return [complement_map[complement], index]
        
        # Add the number and its index to the dictionary
        complement_map[num] = index
    
    # If no solution is found, return an empty list
    return []

# Example usage
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1]
