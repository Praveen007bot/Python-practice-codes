def mutate_string(string, position, character):
    li = list(string)
    li[position] = character
    return ''.join(li)

s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)