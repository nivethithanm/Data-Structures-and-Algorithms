### Problem
#You have been given an undirected graph consisting of N nodes and M edges. This graph can consist of self-loops as well as multiple edges. In addition , you have also been given Q queries. For each query , you shall be given 2 integers A and B. You just need to find if there exists an edge between node A and node B. If yes, print "YES" (without quotes) else , print "NO"(without quotes).

#Input Format:

#The first line consist of 2 integers N and M denoting the number of nodes and edges respectively. Each of the next M lines consist of 2 integers A and B denoting an undirected edge between node A and B. The next line contains a single integer Q denoting the number of queries. The next Line contains 2 integers A and B denoting the details of the query.

#Output Format

#Print Q lines, the answer to each query on a new line.

### Code

arr_ = input().split()

N = int(arr_[0])
M = int(arr_[1])

arr = [[0 for i in range(N)] for j in range(N)] 

for i in range(M):
    arr2 = input().split()
    m = int(arr2[0])
    n = int(arr2[1])
    if (arr[m-1][n-1] == 0):
        arr[m-1][n-1] = 1
        arr[n-1][m-1] = 1

Q = int(input())

for i in range(Q):
    arr2_ = input().split()
    m = int(arr2_[0])
    n = int(arr2_[1])
    if(arr[m-1][n-1] == 1):
        print('YES')
    else:
        print('NO')
