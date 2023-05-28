names = ['Маша','Даша','Катя','Оля']
for i in names:
    print(f'{i}, приходи на обед')

names[3] = 'Вика'
for i in names:
    print(f'{i}, приходи на обед')

names.insert(0,'Кристина')
names.insert(2,'Нина')
names.append('Алиса')
for i in names:
    print(f'{i}, приходи на обед')

while len(names)>2:
    print(names.pop() + ',сори не приходи')
for i in names:
    print(f'{i}, приходи на обед')

del names[0]
del names[0]
print(names)