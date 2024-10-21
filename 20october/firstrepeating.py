# def repeatingelement():
#     arr=[1, 2, 3, 4]
#     search=0
#     index=0
#     x=arr[search]
#     for i in range(0,len(arr)):
#         if i!=search:
#             if x==arr[search]:
#                 index=i
#                 x=arr[i]
#                 k="found"
#                 return x,index,k
#     search+=1
#     repeatingelement()

# y,z,f=repeatingelement()
# if f=="found":
#     print(f"The repeating Element {y} found at {z} index")

# else:
#     print(-1)

                    #This is actual code

# arr= [1,2,3,4]
# y=1
# search=0
# z=''
# count=0
# while y==1 and count<len(arr):
#     x=arr[search]
#     index=0
#     print(f"this is going to be {search} iteration and value of index is {index}")
#     print(f"search for {x} element")
#     for i in range(0,len(arr)):
#         if i!=search:
#             if x==arr[i]:
#                 index=i
#                 y=2
#                 z='found'
#                 break
#     print(f"{search} iteration end")
#     print(f"the value of y is {y}")
#     print()
#     search=search+1
#     count+=1


# if z=="found":
#     print(f"element {x} found at {index}")
# else:
#     print(-1)



            # this is with 0(n) complexity

def firstRepeated(self, arr):
    # Dictionary to store the frequency of elements
    element_count = {}
    
    # First pass: count occurrences of each element
    for num in arr:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1

    # Second pass: find the first element with a count > 1
    for i, num in enumerate(arr):
        if element_count[num] > 1:
            return i + 1  # Returning 1-based index

    # If no repeated element is found, return -1
    return -1

    

