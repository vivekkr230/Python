

# def nonzero(nums):
#     for i in range(len(nums)):
#         count=0
#         if nums[i] != 0:
#             nums[count],nums[i]=nums[i],nums[count]
#             count +=1


#     print(nums)

# def main():
#     while 1==1:
#         l1=list(input("Enter the list"))
#         if l1 == -1:
#             break
#         else:
#             nonzero(l1)

# main()
def move_zero(nums):
    # Initialize a pointer for the position of non-zero elements
    non_zero_position = 0
    
    # Iterate through the list
    for i in range(len(nums)):
        if nums[i] != 0:
            # Swap the current element with the element at the non-zero position
            nums[non_zero_position], nums[i] = nums[i], nums[non_zero_position]
            # Move the non-zero position pointer to the right
            non_zero_position += 1

# Examples:
nums1 = [0, 1, 0, 0, 0, 2, 0, 3, 0, 4]
move_zero(nums1)
print(nums1)  # Output: [1, 2, 3, 4, 0, 0, 0, 0]

nums2 = [0, 1, 2, 0, 1]
move_zero(nums2)
print(nums2)  # Output: [1, 2, 1, 0, 0]

nums3 = [1, 2, 3, 4, 5, 6, 7, 8]
move_zero(nums3)
print(nums3)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
