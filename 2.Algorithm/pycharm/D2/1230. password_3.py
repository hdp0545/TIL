for test_case in range(1, 11):
    N = int(input())
    password = list(map(int, input().split()))
    N_command = int(input())
    command = list(map(int, input().split()))
    for i in range(N_command):
        if command[i] == 'I':
            temp = command.pop([i+1:i+3+command[i+2]])
            del command
