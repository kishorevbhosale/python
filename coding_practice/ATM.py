"""
Input
Positive integer 0 < X <= 2000 - the amount of cash which Pooja wishes to withdraw.

Nonnegative number 0<= Y <= 2000 with two digits of precision - Pooja's initial account balance.

Output
Output the account balance after the attempted transaction, given as a number with two digits of precision. If there is not enough money in the account to complete the transaction, output the current bank balance.

Example - Successful Transaction
Input:
30 120.00

Output:
89.50
Example - Incorrect Withdrawal Amount (not multiple of 5)
Input:
42 120.00

Output:
120.00
Example - Insufficient Funds
Input:
300 120.00

Output:
120.00
"""

withdraw, balance = [float(i) for i in input().split()]

if 0 < withdraw <= 2000 and 0 < balance <= 2000:
    if withdraw <= (balance - 0.50) and withdraw % 5 == 0:
        print("%.2f" % (float(balance - withdraw - 0.5)))
    else:
        print(balance)
