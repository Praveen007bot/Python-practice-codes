str = input()
sub = input()

count = 0
c = 0
for i in str:
    if str[c:len(sub)+c] == sub:
        count += 1
    c += 1

print(count)