""""

Input
The first line of the input contains an integer T, the number of test cases. T lines follow. Each T contains an integer N whose square root needs to be computed.

Output
For each line of input output the square root of the input integer.

Constraints
1<=T<=20
1<=N<=10000
Input:
3
10
5
10000

Output:
3
2
100

"""
for _ in range(int(input())):
    n = int(input())
    print(int(n ** (1 / 2)))
