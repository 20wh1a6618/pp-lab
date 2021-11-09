def binarysearch(arr,n,low,high,x):
    mid = (low+high)//2
    if (low > high):
        return 0
    elif(arr[mid] == x):
        return mid
    elif(arr[mid] < x):
        low = mid+1
    elif(arr[mid] > x):
        high = mid-1
    else:
        return binarysearch(arr,n,low,high,x)
    n=int(input("enter the size of an array"))
    print("enter the array elements")
    arr = []
    for i in range(0,n):
        ele = int(input())
        arr.append(ele)
    arr.sort()
    print(arr)
    x = int(input("enter the search elements"))
    answer = binarysearch(arr,n,0,n-1,x)
    if(answer != 0):
        print("elements found at position:",answer)
    else:
        print("element not found in the array")
//input:
Enter the size of an array : 7
Enter the array elements : 3 4 5 6 7 8 9
Enter the search element : 5
//output :
Element found at 3 position    
    
