# словари
name = 'max'
age = 20
has_car = True

friend = (name, age, has_car)
friend_inverse = (age, has_car, name)

# Словарь, объявления
friend = {
    'name': 'max',
            'age':20,
                   'has_car': True
}

print(type(friend))

# Индексы? У словаря есть ключи  и мы можем их использовать
print(friend['age'])

# Функция
print(len(friend))

# Оператор вхождения
# Проверяет по ключам
print('name' in friend)
print('max' in friend)

# Методы (Действия) Добавить, удалить, изменить
# Добавить, Изменить
print(friend)
friend['has_wife'] = False
print(friend)
friend['has_wife'] = True
print(friend)

# Удаление
del friend['has_wife']
print(friend)

# Методы, получить значение
# ключи
print(list(friend.keys()))
# Занчения
print(list(friend.values()))
# Пары ключ значение - кортежи
print(list(friend.items()))
print('max' in friend.values())

friend['old'] = '20'
print(list(friend.values()))
print(list(friend.keys()))
print((list(friend.items())))