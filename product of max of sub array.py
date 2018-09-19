def maxsubarrayproduct(arr):
 
    n = len(arr)
    max_ending_here = 1
    min_ending_here = 1
    max_so_far = 1
    for i in range(0,n):
        if(arr[i] > 0):
            max_ending_here = max_ending_here*arr[i]
            min_ending_here = min (min_ending_here * arr[i], 1)
        elif(arr[i] == 0):
            max_ending_here = 1
            min_ending_here = 1
        else:
            temp = max_ending_here
            max_ending_here = max (min_ending_here * arr[i], 1)
            min_ending_here = temp * arr[i]
        if (max_so_far <  max_ending_here):
            max_so_far  =  max_ending_here
    print(max_so_far)
a=int(input())
c=input().split()
arr=[]
for i in range(0,a):
    arr.append(int(c[i]))
maxsubarrayproduct(arr)
