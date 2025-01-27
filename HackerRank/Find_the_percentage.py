n = int(input())

li = []
for i in range (n):
    li.append(input().split())

target = input()

for idx,el in enumerate(li):
    name, *scores = li[idx]
    scores = list(map(int, scores))
    if name == target:
        res = sum(scores)/len(scores)

print(f"{res:.2f}")

 