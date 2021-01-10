""""
Link : https://www.codechef.com/problems/KOL15A

Input
The first line of the input contains an integer T denoting the number of test cases. Then T test cases follow.
Each test case is described with a single line containing a string S, the alphanumeric string.
Output
For each test case, output a single line containing the sum of all the digit characters in that string.
Constraints
1 ≤ T ≤ 1000
1 ≤ |S| ≤ 1000, where |S| is the length of the string S.
Example
Input:
1
ab1231da

Output:
7

"""

for _ in range(int(input())):
    print(sum([int(i) for i in list(input()) if i.isnumeric()]))
