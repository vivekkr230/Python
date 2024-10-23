# nums=[1,3,5,6]

# low=0
# high=len(nums)
# target=3
# mid=0
# while low<=high:
#     mid=low+((high-low)//2)
#     if nums[mid]==target:
#         break

#     if nums[mid]<target:
#         low=mid+1
#         # high=mid-1

#     if nums[mid]>target:
#         # low=low+1
#         high=mid-1 

# print(mid)


                #Actual Code

class Solution:
    def searchInsert():
        low=0
        high=len(nums)-1
        mid=0
        while low<=high:
            mid=low+((high-low)//2)
            if nums[mid]==target:
                return mid

            if nums[mid]<target:
                low=mid+1
                

            if nums[mid]>target:
                
                high=mid-1 

        if nums[mid]>target:
            return mid
        else:
            return mid+1

num=Solution()
y=num
print(y)