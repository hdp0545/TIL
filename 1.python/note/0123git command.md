## 문제풀이

1. 이 명령어를 통해 내장함수를 읽을 수 있다.

```python
dir(__builtins__)
```

2. 펠린드롬
   - 포인트 : 문자열의 길이
   - 왼쪽 끝과 오른쪽 끝을 비교하면서 인덱스를 이동하면서 비교

```python
#1
def palindrome(word):
    list_word = list(word)
    #0부터 문자열의 길이의 절반만큼 반복
    for i in range(len(list_word) // 2):
        #왼쪽 문자와 오른쪽 문자를 비교
        if list_word[i] != list_word[-i-1]:
            return False # 회문이 아님
        	#return 에는 브레이크의 의미가 있음 값을 반환하고 함수를 끝냄.
    return True

#2
def palindrome(word):
    return word == word[::-1]

#3
word = 'eye'
new_word = reversed(word)
print(new_word) #뒤집혀진 객체라는 뜻의 의미없는 값이 나옴.
print(''.join(new_word))

#3 정답
def palindrome(word):
    return word == ''.join(reversed(word))
```



## 명령어 단축하기(깃배쉬)

- `code ~/.bashrc`

명령어 저장 파일인 bashrc 만들기

- `alias jp="jupyter notebook"` 치기

alias(명령어를 단축하는 함수) 를 사용하여 jupyter notebook을 jp에 저장

- `source ~/.bashrc`

source 라는 명령어를 사용하여 bashrc를 초기화하기.



