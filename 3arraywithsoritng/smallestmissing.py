# arr=[2,2,-5,2,-2,7,1,-8]
# # arr=[1,2,3,4,5]

# # def missingNumber(arr):
# #         #Your code here
# missing_num=0
# smallest_num=1
# while missing_num==0:
#     x=smallest_num
#     if x==smallest_num:
#         for i in range(0,len(arr)):
#             if arr[i]==smallest_num:
#                 # print(f"smallest number is {smallest_num} element found at {i}")
#                 # print(x)
#                 smallest_num+=1
                
#                 print(smallest_num)
#     else:
#         missing_num=smallest_num  
            
# print(f"missing num is {missing_num}")

# # # return missing_num

# # # y=missingNumber(arr)
# # # print(y)
    


# def missingNumber(arr):
#         #Your code here
#         smallest_num=1
#         for i in range(0,len(arr)):
#             for j in arr:
#                 if smallest_num==j:
#                     smallest_num+=1
#                     break
                
#         return smallest_num

# y=missingNumber([0, -10, 1, 3, -20])
# print(y)

n=5
for i in range(n):
    print(i)