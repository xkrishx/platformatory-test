def process_data():
    n=int(input("enter length of data list "))
    data = []
    for i in range(n):
        sublist=[int(input("enter first integer of the sublist: \n")), int(input("enter second integer of the sublist: "))]
        data.append(sublist)
    print("the list obtained is: ", data)
    for i in range(len(data)):
        data[i]=data[i][0]-data[i][1]
    print("the new list after subtraction is: ", data)
    res=1
    for x in data:
        res=res*x
    
    print("the final product is", res)

process_data()