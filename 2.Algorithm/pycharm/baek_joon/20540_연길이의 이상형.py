words = input()
mbti1 = ['E', 'S', 'T', 'J']
mbti2 = ['I', 'N', 'F', 'P']
answer = [mbti2[idx] if word == mbti1[idx] else mbti1[idx] for idx, word in enumerate(words)]
print(''.join(answer))