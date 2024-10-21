def concatinate(string):
    if type(string) != list:
        string=list(string)
        name="".join(string)
    
    else:
        name="".join(string)
    print(name)

concatinate("vivek")