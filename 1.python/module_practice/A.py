def func():
    print('function A.py')

print('top-level A.py')

if __name__ == '__main__':
    print('A.py 가 직접 실행')
else:
    print('A.py 가 import 되어 사용됨')