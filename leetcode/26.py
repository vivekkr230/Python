# pahle ek aaray lena hai usme iterate karwana hai phir output ko
# naye aaray m push kar dena hai
nums=[1,1,2]
newarr=[]
newarr2=[]

print(nums)

for i in range(len(nums)-1):
    if nums[i]==nums[i+1]:
        newarr.append(nums[i+1])
    else:
        newarr2.append(nums[i])
        newarr2.append(nums[i+1])
while len(arr)!=len(newarr2):
    newarr2.append('_')
print(newarr)
print(newarr2)
    

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         ans=nums.copy()

#         for i in range(1,len(ans)):
#             if ans[i]==ans[i-1]:
#                 nums.remove(ans[i])

#         return len(nums)