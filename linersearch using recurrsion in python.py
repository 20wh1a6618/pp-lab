def linearsearch(arr,n,x,i):
    if(i>=n):
        return 0
    elif(arr[i]==x):
        return i+1
    else:
        return linearsearch(arr,n,x,i+1)
    n=int(input("enter the size of an array"))
    print("enter the array elements")
    arr=[]
    for i in range(0,n):
        ele=int(input())
        arr.append(ele)
        x=int(input("enter the search element"))
        answer = linearsearch(arr,n,x,0)
        if(answer!=0):
            print("element found at%d position."%answer)
        else:
            print("enter not found")
