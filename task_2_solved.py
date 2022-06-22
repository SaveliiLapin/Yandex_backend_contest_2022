jobs = dict()
people = list()
passed = list()

n = int(input())

for i in range(n):
    temp = input().split(',')

    jobs[temp[0]] = int(temp[1])

k = int(input())

for i in range(k):
    people.append(input().split(','))
    people[i][2] = int(people[i][2])
    people[i][3] = int(people[i][3])

people = sorted(people, key=lambda x: (x[1], -x[2], x[3]))

for i in people:
    if jobs.get(i[1]) and jobs.get(i[1]) > 0:
        passed.append(i[0])

        jobs[i[1]] = jobs[i[1]] - 1

print(*sorted(passed), sep='\n')
