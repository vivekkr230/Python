arr=[3,7,6,7,1,8,8,1,8]
num1=7
num2=7
start=0
end=0
for i in range(0,len(arr)):
    if arr[i]==num1:
        start=i
        
for i in range(len(arr)-1,0,-1):
    if arr[i]==num2:
        end=i

print(f"start:{start} end:{end}")
# if start>end:
#     x=start
#     start=end
#     end=x
# else:
#     x=end

print(f"start:{start} end:{end}")

# count=0            
# for j in range(start+1,x):
#     count=count+1

# print(count)