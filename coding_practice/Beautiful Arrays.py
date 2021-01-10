""""

Problem link  : https://www.codechef.com/problems/ICPC16B

An array a is called beautiful if for every pair of numbers ai, aj, (i ≠ j), there exists an ak such that ak = ai * aj. Note that k can be equal to i or j too.

Find out whether the given array a is beautiful or not!

Input
First line of the input contains an integer T denoting the number of test cases. T test cases follow.

First line of each test case contains an integer n denoting number of elements in a.

Next line contains n space separated integers denoting the array

Example
Input
3
2
0 1
2
1 2
2
5 6

Output:
yes
yes
no
Explanation
Test case 1. If you multiply 0 with 1, you get 0, we see that a0 = 0. So, the array is beautiful.

Test case 3. If you multiply 5 with 6, you get 30, there does not exist an k such that ak = 30. So, the array is not beautiful.

"""

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    l = len(arr)
    one = arr.count(1)
    zero = arr.count(0)
    m_one = arr.count(-1)
    other = l - (zero + one + m_one)
    if other > 1:
        print("no")
    elif other >= 1 and m_one >= 1:
        print("no")
    elif m_one > 1 and one == 0:
        print("no")
    elif one == l or zero == l:
        print("yes")
    elif (one + zero) == l:
        print("yes")
    else:
        print("yes")
