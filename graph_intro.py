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
