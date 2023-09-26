input_words = input()

answer = ''

for w in input_words:
    if w.isupper():
        answer += w.lower()
    else:
        answer += w.upper()
        
print(answer)