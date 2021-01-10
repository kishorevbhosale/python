arr = []
for t in range(int(input())):
    arr.append(int(input()))
print("\n".join([str(i) for i in sorted(arr)]))