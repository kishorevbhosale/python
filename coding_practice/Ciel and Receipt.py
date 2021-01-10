"""
Problem link : https://www.codechef.com/problems/CIELRCPT
"""

pricelist = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]

for t in range(int(input())):
    arr = []
    price = int(input())
    arr = [i for i in pricelist if i <= price]
    arr = arr[::-1]
    ans = 0
    count = 0

    for i in range(len(arr)):
        ans += arr[i]
        count += 1
        if price == (arr[i] + arr[i]):
            print(2)
            break
        elif ans == price:
            print(count)
            break
        elif ans > price:
            ans -= arr[i]
            count -= 1
