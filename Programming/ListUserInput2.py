# li = input('Enter space saperated elements: ')
# print(li)
# li2 = li.split()
# print(li2)
# int_li = list(map(int, li2))
# print(int_li)


# tup = tuple(map(int,input('Enter space saperated elements: ').split()))
# print(tup)


li = list(map(int, input().split()))
print([i for i in li if i%2==0])
