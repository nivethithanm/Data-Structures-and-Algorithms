'''
Monk and Rotation Monk loves to preform different operations on arrays, and so being the principal of Hackerearth School, he assigned a task to his new student Mishki. Mishki will be provided with an integer array A of size N and an integer K , where she needs to rotate the array in the right direction by K steps and then print the resultant array. As she is new to the school, please help her to complete the task.

Input: The first line will consists of one integer T denoting the number of test cases. For each test case:

1) The first line consists of two integers N and K, N being the number of elements in the array and K denotes the number of steps of rotation. 2) The next line consists of N space separated integers , denoting the elements of the array A. Output: Print the required array.
'''
def rotate(arr,k):
    bkup = arr[-k:]
    for elem in arr[:-k]:
        bkup.append(elem)
    return bkup

for i in range(int(input())):
    arr = input().split()
    N, K = int(arr[0]), int(arr[1])
    arr_ = input().split()
    for j in range(len(arr_)):
        arr_[i] = int(arr_[i])
    arr_ = rotate(arr_, K%N)    
    strin = ""
    for elem in arr_:
        strin += str(elem) + ' '
    print(strin)
