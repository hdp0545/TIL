for _ in range(3):
    a = list(map(int, input().split(' ')))
    st = a[0]*3600 + a[1]*60 + a[2]
    et = a[3]*3600 + a[4]*60 + a[5]
    total_second = et-st
    second = str(int(total_second % 60))
    total_min = total_second // 60
    minuete = str(int(total_min % 60))
    hour = str(int(total_min // 60))
    print(hour, minuete, second)
