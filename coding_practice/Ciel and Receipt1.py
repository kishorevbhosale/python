"""
Problem link : https://www.codechef.com/problems/CIELRCPT
"""

for i in range(int(input())):
    n = int(input())
    div = 2048
    sum = 0
    for j in range(12):
        if n // div:
            sum += n // div
            n = n % div
            if n == 0:
                break
        div //= 2
    print(sum)
