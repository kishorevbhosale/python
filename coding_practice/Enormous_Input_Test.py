""""

Input
The input begins with two positive integers n k (n, k<=107).
The next n lines of input contain one positive integer ti, not greater than 109, each.

Output
Write a single integer to output, denoting how many integers ti are divisible by k.

Example
Input:
7 3
1
51
966369
7
9
999996
11

Output:
4 """


t,k = [int(i) for i in input().split()]

count = 0
if(k<=10^7):
    while(t!=0):
        num = int(input())
        if(num%k==0):
            count += 1
        t -= 1
print(count)