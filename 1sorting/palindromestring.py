# string=input("Enter the string: ")
# match=''
# for i in range(len(string)-1,-1,-1):
#     match+=string[i]

# if match==string:
#     print(f"{string} is palindrome as it reverse is {match}")

# else:
#     print(f"{string} is not a palindrome as it reverse is {match}")
string=input("Enter the string: ")
# x=''
low=0
high=len(string)-1

while(low<=high):
    if string[low]!=string[high]:
        high="not palindrome"
        break
    
    # print(low)
    # print(high)
    
    high=high-1
    low+=1

    

if high=="not palindrome":
    print(f"{string}  is not a palindrome")

else:
    print(f"{string}  is  a palindrome")  

