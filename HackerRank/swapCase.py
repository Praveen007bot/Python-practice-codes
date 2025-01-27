str = input()
res = ""
for i in str:
    if i.isalnum():
        if i.isupper():
            res = res + i.lower()
        if i.islower():
            res = res + i.upper()
        if i == " ":
            res = res + " "
    else:
        res = res + i

print(res)