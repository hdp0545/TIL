import A

print('top-level B.py')

A.func()

if __name__ == '__main__':
    print('B.py 가 직접 실행')
else:
    print('B.py 가 import 되어 사용됨')