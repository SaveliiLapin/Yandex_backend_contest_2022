fin = open('input.txt', 'r')
filters = list()
pointer = 0
now_l = 0
now_r = 0
item_l = 0
item_r = 0
ans = '['
s = fin.readline()

for line in fin:
    filters.append(line.split()[1])

filters[1] = int(filters[1])
filters[2] = int(filters[2])
filters[3] = tuple(reversed(list(map(int, filters[3].split('.')))))
filters[4] = tuple(reversed(list(map(int, filters[4].split('.')))))

while pointer < len(s) - 3:
    to_print = 0

    pointer = s.find('{', pointer)
    item_l = pointer

    pointer = s.find('name', pointer)
    pointer += 6

    pointer = s.find('"', pointer)
    now_l = pointer
    pointer = s.find('"', pointer + 1)
    now_r = pointer + 1

    if filters[0] in s[now_l:now_r]:
        to_print += 1

    pointer = s.find('price', pointer) + 7
    now_l = pointer

    pointer = s.find(',', pointer)

    now_r = pointer

    if filters[1] <= int(s[now_l:now_r]) <= filters[2]:
        to_print += 1

    pointer = s.find('date', pointer) + 6
    pointer = s.find('"', pointer)
    now_l = pointer + 1
    pointer = s.find('"', pointer + 1)
    now_r = pointer

    date = s[now_l:now_r].split('.')
    date = tuple(reversed(list(map(int, date))))

    if filters[3] <= date <= filters[4]:
        to_print += 1

    pointer = s.find('}', pointer)

    item_r = pointer + 1

    if to_print == 3:
        ans += s[item_l:item_r] + ', '

    pointer += 1

ans = ans[:-2] + ']'
print(ans)
