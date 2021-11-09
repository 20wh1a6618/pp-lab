def binarysearch(arr,n,low,high,x):
    while(low <= high):
        mid = (low+high)//2
        if(arr[mid] ==x):
            return mid
        elif(arr[mid] < x):
            low = mid+1
        else:
            high = mid-1
        return -1
    n=int(input("enter the size of an array"))
    print("enter the array elements")
    arr = []
    for i in range(0,n):
        ele = int(input())
        arr.append(ele)
    arr.sort()
    print(arr)
    x = int(input("enter the search element"))
    answer = binarysearch(arr,n,0,n-1,x)
    if(answer ==-1):
      print("enter not found in the array")
    else:
      print("element found at position:",answer)
//input:
Enter the size of an array : 4
Enter the array elements : 2 3 4 5
Enter the search element : 3
//output:
Element found at 2 position    
