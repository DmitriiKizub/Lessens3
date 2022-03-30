# Лист
friends = ('max', 'kate', 'john', 'leo')

for friend in friends:
    hello = f'Hello, {friend}'
    print(hello)

# Строке
friend = 'Максим Александрович Попов'

for letter in friend:
    print(letter)

# Словарь
friend = {
    'name': 'max',
            'age':20,
                   'has_car': True
}

# По ключам
for key in friend:
    print(key)
    print(friend[key])

# Только значение
for val in friend.values():
    print(val)

# По парам. ключа значения
for item in friend.items():
    print(item)

for key, val in friend.items():
    print(key)
    print(val)

name, age, has_car = ('max', 23, True)
print(name, age, has_car)