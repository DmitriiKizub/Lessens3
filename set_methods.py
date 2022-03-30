# set
# set набор уникальных данных
# Объявление
office = {'max', 'kate', 'john', 'leo','leo'}
print(type(office))
print(office)

office.add('leo')
office.add('vas')
print(office)

office = ['max', 'kate', 'john', 'leo','leo']
print(set(office))

# 2. Операции с множествами
office= {'max', 'kate', 'john', 'leo','leo'}
freelance = {'max', 'kate','poll'}

print(office-freelance)
print(freelance - office)
print(office&freelance)
print(office|freelance)

for item in office:
    print(item)