""""

Input
Input will begin with an integer T, the number of test cases. Each test case consists of a single line. The line begins with a positive integer N, the number of ingredients. N integers follow, each indicating the quantity of a particular ingredient that is used.

Output
For each test case, output exactly N space-separated integers on a line, giving the quantity of each ingredient that the chef should use in order to make as little food as possible.

Sample Input
3
2 4 4
3 2 3 4
4 3 15 9 6
Sample Output
1 1
2 3 4
1 5 3 2

"""


def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


for _ in range(int(input())):
    a = list(map(int, input().split()))
    arr = a[1:]
    num1 = arr[0]
    num2 = arr[1]
    gcd = find_gcd(num1, num2)

    for i in range(2, len(arr)):
        gcd = find_gcd(gcd, arr[i])

    if gcd == 1:
        for i in arr[:]:
            print(i, end=" ")
        print()
    else:
        for i in arr[:]:
            print(int(i / gcd), end=" ")
        print()
