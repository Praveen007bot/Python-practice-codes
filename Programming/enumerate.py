li = [20, 39, 92, 3]

# for idx, el in enumerate(li):
#     print(idx, el)

# write a pyhton program to print all even index elements.

for idx, el in enumerate(li,start=1):
    if idx % 2 == 0:
        print(f'Index of {el} is {idx}')

