'''
Input
t – the number of numbers in list, then t lines follow [t <= 10^6].
Each line contains one integer: N [0 <= N <= 10^6]

Output
Output given numbers in non decreasing order.
Example
Input:

5
5
3
6
7
1
Output:

1
3
5
6
7
'''

def turbo_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__=="__main__":
    t = int(input())
    arr = []
    while t != 0:
        num = int(input())
        if 0 <= num <= 100000:
            arr.append(num)
        t -= 1
    print("\n".join([str(i)for i in turbo_sort(arr)]))
