result =range(1, 100)
print(result)
print(type(result))
print(list(result))

result =range(4, 56)
print(list(result))

result =range(4, 56, 2)
print(list(result))

result =range(60, 2, -3)
print(list(result))

# Сколько то раз
for i in range(100):
    print(i)

" Индексация списка"
questions = ['a','b','c','d']
answers = [111,222,333,444]

for i in range(len(questions)):
    print('i', i)
    print('q', questions[i])
    print('a', answers[i])


# enumerate
for i,q in enumerate(questions):
    print(i)
    print(q)
    print(answers[i])