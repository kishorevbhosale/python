""""
Input
The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

Output
Display the reverse of the given number N.

Constraints
1 ≤ T ≤ 1000
1 ≤ N ≤ 100000
Example
Input
4
12345
31203
2123
2300
Output
54321
30213
3212
32
"""

for _ in range(int(input())):
    num = input()
    print(int(num[::-1]))
