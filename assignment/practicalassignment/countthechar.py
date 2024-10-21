# Write a program that counts the frequency of each character in a string and stores it in a dictionary.


name="Shubhankar Kumar"
dict_of_string={}

for i in name:
   
    if i in dict_of_string:
        dict_of_string[i]+=1
    else:
        dict_of_string[i]=1
print(dict_of_string)

# correct program here
