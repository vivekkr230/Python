l1=[400,500,6,2,3,400,9,500]
l2=[]
for i in l1:
    if i in l2:
        print(f"{i} is an repetitive element")
        
    else:
        l2.append(i)
print(l2)


# def find_duplicates(nums):
#     duplicates = []
    
#     for num in nums:
#         index = abs(num) - 1  # Use the absolute value to get the correct index
#         if nums[index] < 0:
#             duplicates.append(abs(num))
#         else:
#             nums[index] = -nums[index]  # Mark the number as visited by making it negative
    
#     return duplicates

# # Example usage:
# nums = [100,100,500,100]
# print(find_duplicates(nums))  # Output: [2, 3]

