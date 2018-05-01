def Biggie(arr):
    for i in range(len(arr)):
        if(arr[i]>=0):
            arr[i]='big'
Biggie([1,4,-3,-2,5,0])
array =[1,4,-3,-2,5,0]
def Count_Pos(arr):
    k=0
    for num in arr:
        if (num >=0):
            k+=1
    arr[len(arr)-1] = k
    return arr
Count_Pos([-1,1,1,1,1])
def SumTotal(arr):
    sum1 = 0
    for num in arr:
        sum1 +=num
    return sum1
SumTotal(array)
def Avg_Me(arr):
    avg = 0
    size = len(arr)
    for num in arr:
        avg += num/size
    return avg
print(Avg_Me(array))
def Length(arr):
    k=0
    for num in arr:
        k+=1
    print(k)
    return k
Length(array)
def Minimum(arr):
    if not arr:
       return False  
    min = arr[0]
    for num in arr:
        if (num < min):
            min = num
    return min
print(Minimum(array))
def Maximum(arr):
    if not arr:
       return False 
    max = arr[0]
    for num in arr:
        if num >max:
            max = num
    return max
print(Maximum(array))
def ultimate(arr):
    sum_t = SumTotal(arr)
    avg = Avg_Me(arr)
    min= Minimum(arr)
    max = Maximum(arr)
    length = Length(arr)
    analyze = dict([("Sum",sum_t),("Average",avg),("Minimum",min),("Maximum",max),("Length",length)])
    print(analyze)
    return analyze
ultimate(array)
def reverseList(arr):
    k=len(arr)
    rng = int(len(arr)/2)
    i=0
    if not arr:
        return False
    while i < rng:
        temp = arr[i]
        arr[i] = arr[k]
        arr[k] =temp
        k-=1
        i+=1
    return arr
print(reverseList(array))



