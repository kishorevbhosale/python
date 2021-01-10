""""
Input
The first line contains an integer T, total number of testcases. Then follow T lines, each line contains three integers A, B and C.

Output
Display the second largest among A, B and C.
"""

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    print(sorted(arr)[-2])
