def mapping(pos, letter):
    room[pos[0]][pos[1]] = letter

    if room[pos[0]][pos[1] - 1] == '.':
        mapping((pos[0], pos[1] - 1), 'L')
    if room[pos[0] - 1][pos[1]] == '.':
        mapping((pos[0] - 1, pos[1]), 'U')
    if room[pos[0]][pos[1] + 1] == '.':
        mapping((pos[0], pos[1] + 1), 'R')
    if room[pos[0] + 1][pos[1]] == '.':
        mapping((pos[0] + 1, pos[1]), 'D')


fin = open('input.txt', 'r')

i = 0
room = list()
start = tuple()

n, m = map(int, fin.readline().split())

for s in fin:
    if s.find('S') != -1:
        start = (i, s.find('S'))

    room.append(list(s) if s[-1] == '#' else list(s[:-1]))
    i += 1

mapping(start, 'S')

for i in room:
    print(''.join(i))
