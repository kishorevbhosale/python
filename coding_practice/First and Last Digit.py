""""
Input
The first line contains an integer T, total number of test cases. Then follow T lines, each line contains an integer N.

Output
Display the sum of first and last digit of N.

Constraints
1 ≤ T ≤ 1000
1 ≤ N ≤ 1000000
Example
Input
3
1234
124894
242323

Output
5
5
5
"""

for _ in range(int(input())):
    num = input()
    print(int(list(num)[0]) + int(list(num)[-1]))
