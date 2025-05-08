s = n
for i in range(6):
    n.append(int(input()))

s = n
for i in range(5):
    if s[j] > s[j+1]:
        a = s[j]
        s[j] = s[j+1]
        s[j+1] = a
print(s)

s = n
for i in range(len(n)-2):
    for j in range(len(n)-1):
        if s[j] > s[j+1]:
            a = s[j]
            s[j] = s[j+1]
            s[j +1] = a
print(s)
