# Create a dictionary that represents a phone book, with names as keys and another dictionary as values (containing phone numbers and addresses).
# Access a nested value in the dictionary.
# Add a new entry to the nested dictionary.


phone_book={
    "Vivek":{
        "p_no":985984958,
        "Address":"JP Nagar"
        },
    "Satyam":{
        "p_no":9999999958,
        "Address":"Odisha"
        },
    "Suku":{
        "p_no":980000008,
        "Address":"Vijay Nagar"}
}

# v=phone_book.get("Vivek")
# print(v.get("Address"))
# print(phone_book.get("Suku").get("Address"))
# phone_book.get("Suku")["Age"]=22
# print(phone_book.get("Suku"))

#else we could have done in this way
v=phone_book["Vivek"]["Address"]
print(f"{v}")
s=phone_book["Satyam"]["p_no"]
print(f"{s}")

phone_book["Suku"]["Address"]="Near Vijay Nagar"
print(f"updated address for suku {phone_book}")

phone_book["Surya"]={
    "p_no":938746473893,
    "Address":"Assam"
}
print(phone_book)