n = int(input())

li = []

for i in range (n):
    name = input()
    score = float(input())
    li.append([name, score])

score = []
for i in li:
    score.append(i[1]) 

score = list(set(score))
score.sort()
res = score[1]
li.sort()
for i in li:
    if i[1] == res:
        print(i[0])


