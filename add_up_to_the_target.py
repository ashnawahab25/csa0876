def two_sum(nums, target):
    # Create a dictionary to store the indices of elements
    num_indices = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num

        # If the complement is in the dictionary, return the indices
        if complement in num_indices:
            return [num_indices[complement], i]

        # Otherwise, add the current element's index to the dictionary
        num_indices[num] = i

    # If no solution is found, return an empty list
    return []

# Test Case 1
nums1 = [2, 7, 11, 15]
target1 = 9
print(two_sum(nums1, target1))

# Test Case 2
nums2 = [3, 2, 4]
target2 = 6
print(two_sum(nums2, target2))
