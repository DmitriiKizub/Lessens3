# Строки

friend = 'Максим Александрович Попов'
friend = 'Максим Александрович \n Попов'
print(friend)

# Индексы - индексы начинаются с 0
friend = 'Максим Александрович Попов'

print(friend[2])
print(friend[5])

# Отрицательные индексы
print(friend[-2])

# Срезы
hello = 'hello world'
# lo wo
print(hello[3:8])

# hello
print(hello[:5])

# word
print(hello[6:])
print(hello[:-1])
print(hello[-1:])

# Функции и методы строки
# 1. Функции
friend = 'Максим Александрович Попов'
friend_fio_length = len(friend)
print(friend_fio_length)

# 2. Метод
friend = 'Максим'
friend_upper = friend.upper()
print(friend_upper)

# 3. Оператор На вхождение подстроки в строку
friend = 'Максим Александрович Попов'
letters = 'андр'

print(letters in friend)
if letters in friend:
    print('Есть')

# Методы строк
friend = 'Максим александрович попов'
# Надо заменить фамилию на Иванов
print(friend[:21]+ 'Иванов')

# Метод для замены подстроки строкой
new_friend = friend.replace('Попов', 'Иванов')
print(new_friend)

#help(str)
#print(dir(str))
# Популярные мотоды
print(friend.upper())
print(friend.lower())
print(friend.title())
print(friend.isdigit())
# Метод split
print(friend.split(' '))

goods = 'стол;;;стул;;;диван'
print(goods.split(';;;'))

bad_data = 'стол;стул,диван кровать'

print(bad_data.replace(';',' ').replace(',',' ').split())

# Форматирование строк
age = 20
name = 'Макс'
# 1. конкатенация +
info = 'Имя: ' + name + ' age: ' + str(age)
print(info)

# 2. format
info = 'Имя: {} age: {}'.format(name, age)
print(info)

# 3. f
info = f'Имя: {name} age: {age}'
print(info)

# Неизменяемость строк (изменияемые и неизменяемые типы)

friend = 'Максим александрович Попов'
upper_friend = friend.upper()
print(upper_friend)

l = ['dsfsf']
l.append(1)
print(l)