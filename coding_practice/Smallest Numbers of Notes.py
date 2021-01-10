""""
Consider a currency system in which there are notes of seven denominations, namely, Rs. 1, Rs. 2, Rs. 5, Rs. 10, Rs. 50, Rs. 100.
If the sum of Rs. N is input, write a program to computer smallest number of notes that will combine to give Rs. N.

Input
The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

Output
Display the smallest number of notes that will combine to give N.

Constraints
1 ≤ T ≤ 1000
1 ≤ N ≤ 1000000
Example
Input
3
1200
500
242

Output
12
5
7

"""

for _ in range(int(input())):
    num = int(input())
    count = 0
    if num >= 100:
        a = int(num / 100)
        count += a
        num = num % 100

    if num >= 50:
        a = int(num / 50)
        count += a
        num = num % 50

    if num >= 10:
        a = int(num / 10)
        count += a
        num = num % 10

    if num >= 5:
        a = int(num / 5)
        count += a
        num = num % 5

    if num >= 2:
        a = int(num / 2)
        count += a
        num = num % 2

    if num >= 1:
        a = int(num / 1)
        count += a
        num = num % 1

    print(int(count))
