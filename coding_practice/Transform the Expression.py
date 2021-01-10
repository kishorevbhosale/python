""""
Input:
3
(a+(b*c))
((a+b)*(z+x))
((a+t)*((b+(a+c))^(c+d)))

Output:
abc*+
ab+zx+*
at+bac++cd+^*

"""

for _ in range(int(input())):
    expression = input()
    postfix = []
    symbols = []
    for i in expression:
        if i == "(":
            symbols += [i]
        elif i.isalpha():
            postfix += [i]
        elif i == ")":
            postfix += symbols[-1]
            symbols = symbols[:-2]
        else:
            symbols += [i]
    print("".join(postfix))
