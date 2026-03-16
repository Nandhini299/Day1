# 1. Missing value 
n = len(num)+1
sum_n = n * (n+1) /2
a = sum(num)
print(sum_n - a)
num = list(map(int,input().split()))


# 2. DSA 
# Max Number

def Maxi(arr):
    if not arr:
        return None
    
    max_num = arr[0]
    
    for i in arr:
        if i > max_num:
            max_num = i
    return max_num 
