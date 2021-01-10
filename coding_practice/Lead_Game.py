"""
Consider the following score sheet for a game with 5 rounds:

Round	Player 1	Player 2
1	    140	        82
2	    89      	134
3	    90      	110
4	    112     	106
5	    88      	90
The total scores of both players, the leader and the lead after each round for this game is given below:

Round	Player 1	Player 2	Leader	    Lead
1	    140     	82      	Player 1	58
2	    229     	216     	Player 1    13
3	    319 	    326     	Player 2   	7
4	    431 	    432     	Player 2	1
5	    519     	522     	Player 2	3
Note that the above table contains the cumulative scores.

The winner of this game is Player 1 as he had the maximum lead (58 at the end of round 1) during the game.

Your task is to help the Manager find the winner and the winning lead.
You may assume that the scores will be such that there will always be a single winner. That is, there are no ties.

Input

The first line of the input will contain a single integer N (N ≤ 10000) indicating the number of rounds in the game.
Lines 2,3,...,N+1 describe the scores of the two players in the N rounds.
Line i+1 contains two integer Si and Ti, the scores of the Player 1 and 2 respectively, in round i.
You may assume that 1 ≤ Si ≤ 1000 and 1 ≤ Ti ≤ 1000.

Output

Your output must consist of a single line containing two integers W and L, where W is 1 or 2 and indicates the winner
and L is the maximum lead attained by the winner.

Example

Input:

5
140 82
89 134
90 110
112 106
88 90
Output:

1 58

"""


from functools import reduce
p1,p2=0,0
ans_list = []
for t in range(int(input())):
    a,b = [int(x) for x in input().split()]
    p1 += a
    p2 += b
    lead = lambda p1, p2: ((p1 - p2),"1") if (p1 > p2) else ((p2 - p1),"2")
    ans_list.append(reduce(lead,[p1,p2]))
ans = (sorted(ans_list)[-1])
print(str(ans[1])+" "+str(ans[0]))
