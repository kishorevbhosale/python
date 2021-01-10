''''
Input
An integer t, 1<=t<=100, denoting the number of testcases, followed by t lines, each containing a single integer n, 1<=n<=100.

Output
For each integer n given at input, display a line with the value of n!

Example
Sample input:
4
1
2
5
3
Sample output:

1
2
120
6
'''


def fact(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans


for t in range(int(input())):
    num = int(input())
    print(fact(num))
    t -= 1
