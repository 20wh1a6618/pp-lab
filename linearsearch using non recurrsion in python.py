def linearsearch(arr,n,x):
    for i in range(0,n):
        if(arr[i] == x):
            return i+1
        return -1
    n=int(input("enter the total number of element"))
    arr = []
    for i in range(o,n):
        ele = int(input("enter the array elements"))
        arr.append(ele)
        print(arr)
        x = int(input("enter the serach element"))
        answer = linearsearch(arr,n,x)
        if(answer == -1):
            print("enter not found")
        else:
            print("element found at position:",answer)    
//input :
Enter Size : 2
Enter 2 elements : 5 6
Element to be searched : 3
 //output :
 Element is not found   
