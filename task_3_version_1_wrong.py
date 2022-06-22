fin = open('input.txt', 'r')
items = list()
filters = list()
count = 0

s = fin.readline()

for line in fin:
    filters.append(line.split()[1])

filters[1] = int(filters[1])
filters[2] = int(filters[2])
filters[3] = tuple(reversed(list(map(int, filters[3].split('.')))))
filters[4] = tuple(reversed(list(map(int, filters[4].split('.')))))

data = s.replace(':', ',')
data = data.split(',')

for i in range(0, len(data), 8):
    idd = data[i + 1].strip()
    name = data[i + 3][data[i + 3].find('"') + 1:data[i + 3].rfind('"')]
    price = int(data[i + 5])
    date = data[i + 7][data[i + 7].find('"') + 1:data[i + 7].rfind('"')].split('.')
    items.append([idd, name, price, date])

print('[', end='')

for i in items:
    temp = tuple(reversed(list(map(int, i[3]))))

    if filters[0] in i[1] and filters[1] <= i[2] <= filters[2] and filters[3] <= temp <= filters[4]:
        if count != 0:
            print(', ', end='')
        count += 1

        print('{"id": ', i[0], ', "name": "', i[1], '", "price": ', i[2], ', "date": "', i[3][0], '.', i[3][1], '.', i[3][2], '"}', sep='', end='')

print(']', end='')
