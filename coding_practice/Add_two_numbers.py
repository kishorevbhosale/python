"""
Input
The first line contains an integer T, total number of test cases. Then follow T lines, each line contains two Integers A and B.

Output
Add A and B and display it.

Constraints
1 ≤ T ≤ 1000
1 ≤ A,B ≤ 10000
Example
Input
3
1 2
100 200
10 40

Output
3
300
50

"""

for t in range(int(input())):
   a,b= [int(i) for i in input().split()]
   print(a+b)