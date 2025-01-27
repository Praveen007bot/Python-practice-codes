# for i in 'Kodnest':
#     print(i)

# for j in [10,20,30]:
#     print(j)


# for n in range(1, 11):
#     print(n)


# for n in range(1, 11):
#     if(n%2 == 0):
#         print(n, end=" ")

# n = 1
# while(n<10):
#     print(n+100)
#     n = n + 1

for i in range(1, 11):
    if(i == 6):
        continue
    print(i, end=" ")

print()

for i in range(1, 11):
    if(i == 6):
        break
    print(i, end=" ")