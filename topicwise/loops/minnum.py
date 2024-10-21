tot_num=[5,3,8,-1,-2,0]
for i in tot_num:
    for y in range(0,6):
        # print(y)
        if(i<=tot_num[y]):
            continue
        elif (i>tot_num[y]):
            break
        else:
            print(i,"has the smallest value")
