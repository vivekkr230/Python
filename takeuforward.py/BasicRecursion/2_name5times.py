print("with passing the parameter")
def printname(count=1):
    if count==6:
        return
    else:
        print("Suku")
        count=count+1
        printname(count)

printname()

print("without passing the parameter")
x=0
def withoutparameter():
    global x
    if x==6:
        return
    else:
        print("Suku")
        x+=1
        withoutparameter()

withoutparameter()

