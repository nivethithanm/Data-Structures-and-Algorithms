'''
Creatnx now wants to decorate his house by flower pots. He plans to buy exactly  ones. He can only buy them from Triracle's shop. There are only two kind of flower pots available in that shop. The shop is very strange. If you buy  flower pots of kind 1 then you must pay  and  if you buy  flower pots of kind 2. Please help Creatnx buys exactly  flower pots that minimizes money he pays.

Input Format

The first line contains a integer  denoting the number of test cases.

Each of test case is described in a single line containing three space-separated integers .

Output Format

For each test case, print a single line containing the answer.
'''

### Code here

for i in range(int(input())):
    arr = input().split()
    for i in range(3):
        N = int(arr[0])
        A = int(arr[1])
        B = int(arr[2])
    ans = 10**10
    for j in range(N+1):
        X = j
        Y = N-j
        val = A*(X**2)+B*(Y**2)
        if (val < ans):
            ans = val
    print(ans)
