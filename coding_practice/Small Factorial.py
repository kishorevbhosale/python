""""

Input
The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

Output
Display the factorial of the given number N .

Constraints
1 ≤ T ≤ 1000
0 ≤ N ≤ 20
Example
Input
3
3
4
5

Output

6
24
120

"""


def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


for _ in range(int(input())):
    n = int(input())
    print(fact(n))
