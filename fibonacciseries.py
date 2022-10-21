'''
#fibonacci series (within some range);
a=0
b=1
n=int(input('enter the ending range for the series'))
for i in range(1,n):
    c=a+b
    a=b
    b=c
    print(b)
'''
#largest in the array;
def largest(arr,n):
    max=arr[0]
    for i in range(1,n):
        if arr[i]>max:
            max=arr[i]
    return max

array=[10, 324, 45, 90, 9808]
n=len(array)
print(largest(array,n))

