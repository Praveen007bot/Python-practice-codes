li = []
n = int(input())

for i in range(n):
    cmd, *values = input().split()
    values = list(map(int, values))

    if cmd == "insert":
        li.insert(values[0], values[1])
    elif cmd == "print":
        print(li)
    elif cmd == "remove":
        li.remove(values[0])
    elif cmd == "append":
        li.append(values[0])
    elif cmd == "sort":
        li.sort()
    elif cmd == "pop":
        li.pop()
    elif cmd == "reverse":
        li.reverse()
    

