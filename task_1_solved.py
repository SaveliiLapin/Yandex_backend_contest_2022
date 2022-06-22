s = input()
q = input()

words = dict()

for i in range(len(s)):
    if s[i] != q[i]:
        if words.get(s[i]) is None:
            words[s[i]] = 1
        else:
            words[s[i]] = words[s[i]] + 1

for i in range(len(s)):
    if s[i] == q[i]:
        print('correct')
    elif words.get(q[i]):
        print('present')

        words[q[i]] = words[q[i]] - 1

        if words[q[i]] == 0:
            words.pop(q[i])
    else:
        print('absent')
