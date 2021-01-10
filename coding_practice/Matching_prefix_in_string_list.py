"""
Find out the longest prefix in given list of strings
ex. Input = ['Apple', 'App', 'Apostrophy']
    Output = 'Ap'
"""


def min_str(ip):
    for i in ip:
        lcount.append(len(i))
    min_index = lcount.index(min(lcount))
    mystr = ip[min_index]
    return mystr


if __name__ == "__main__":
    ip = [x for x in input().split()]
    lcount = []
    min_index = 0
    tmp_list = []

    mystr = min_str(ip)
    del ip[min_index]

    new_str = ""
    for item in ip:
        for j in range(len(mystr)):
            if (item[j]) == (mystr[j]):
                new_str = new_str + item[j]
        tmp_list.append(new_str)
        new_str = ""

    lcount = []
    result_str = min_str(tmp_list)
    print(result_str)
