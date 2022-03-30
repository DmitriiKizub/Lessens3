friends = []
friends = [1, True, 'max', 1.2]
friends = ['max', 'kate', 'john', 'leo']

# Индексы

print(friends[1])
print(friends[-1])

# срезы
print(friends[1:3])

# функции
# Длина
print(len(friends))

# Оператор вхождения
print('max' in friends)
print('poll' in friends)

# Основные методы (действия)
# Добавление, Изменение, Удаление
# Добавление в конец
friends.append('poll')
print(len(friends))
print(friends)

friends.insert(2, 'maria')
print(friends)

# Изменения
friends[3] = 'leonid'
print(friends)

# Удаление
# 1. remove
friends.remove('maria')
print(friends)

# 2. Удаление по индексу
del friends[1]
print(friends)

friends.sort()
friends.reverse()
print(friends)