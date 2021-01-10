"""
You're given an integer N. Write a program to calculate the sum of all the digits of N.

Example
Input
3
12345
31203
2123
Output
15
9
8

"""

for t in range(int(input())):
    print(sum([int(i) for i in input()]))
