""""
Help Lost Robot

problem statement link : https://www.codechef.com/problems/ICPC16A

"""

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split(" "))
    ans = (x2, y2)
    if x1 == x2 and y1 > y2:
        print("down")
    elif x1 == x2 and y1 < y2:
        print("up")
    elif y1 == y2 and x1 < x2:
        print("right")
    elif y1 == y2 and x1 > x2:
        print("left")
    else:
        print("sad")
