def Countdown(num):
    newArr = []
    i=num
    k=0
    while (i>=0):
        newArr.insert(k,i)
        i-=1
        k+=1
    print(len(newArr))
    print(newArr)
Countdown(10)
def printReturn(arr):
    print(arr[0])
    return arr[1]
print(printReturn([2,4]))
def fPlusL(arr):
    gkj = arr[0]+len(arr)
    return gkj
print(fPlusL([3,2,4,5]))

def VG_S(arr):
    newArr = []
    k=0
    if(len(arr) < 2):
        return False
    else:
        for i in arr:
            if(arr[1]<arr[i]):
                newArr.insert(k,arr[i])
                k += 1
        print(newArr)
        print("This is",k,"values")
VG_S([1,2,3,8,0,-1,5,7])

def This_That(num1,num2):
    if(num1 == num2):
        print('Jinx')
    else:
        newArr = [num2]*num1
        print(newArr)
This_That(1,1)
This_That(4,3)
