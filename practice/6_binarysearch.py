l1=[1,2,5,6,4,12,24,45,67]

key=int(input("Enter the element you are looking for: "))

def binarysearch(l1):

    low=0
    high=len(l1)-1

    while low<=high:
        mid=low+(high-low)//2
        
        if l1[mid]==key:
            return l1[mid]

        elif l1[mid] > key:
            high=mid-1

        elif l1[mid] < key:
            low=mid+1

y=binarysearch(l1)

if y==key:
    print(f"Element {key} has found at ")


else:
    print(f"Element {key} has not found")

# else:
#     print(f"Element {key} has not found and the value of found is {found}")




    # there is limit of integer in every language
    # let suppose the limit is here is 256 so there is way to solve it
    # we can write in this way mid=(low+(high-low)//2)
