for _ in range(int(input())):
    string = input()
    N = len(string)
    list = [word for word in string]
    print('..#.'*N + '.')
    print('.#'*2*N + '.')
    print('#.'+'.#.'.join(list)+'.#')
    print('.#' * 2 * N + '.')
    print('..#.' * N + '.')