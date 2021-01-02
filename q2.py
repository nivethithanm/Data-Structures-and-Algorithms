'''
Monk visits the land of Islands. There are a total of N islands numbered from 1 to N. Some pairs of islands are connected to each other by Bidirectional bridges running over water. Monk hates to cross these bridges as they require a lot of efforts. He is standing at Island #1 and wants to reach the Island #N. Find the minimum the number of bridges that he shall have to cross, if he takes the optimal route.

Input: First line contains T. T testcases follow. First line of each test case contains two space-separated integers N, M. Each of the next M lines contains two space-separated integers X and Y , denoting that there is a bridge between Island X and Island Y.

Output: Print the answer to each test case in a new line.
'''

for i in range(int(input())):
    arr = input().split()
    N, M = int(arr[0]), int(arr[1])
    arr_main = []
    arr_ = []
    for j in range(M):
        arr2 = input().split()
        arr2 = [int(elem) for elem in arr2]
        for elem in arr2:
            if(elem not in arr_main):
                arr_main.append(elem)
        arr_.append((arr2[0],arr2[1]))
    arr_main.sort()
    
