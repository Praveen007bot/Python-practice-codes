# map is an build-in method  map(function, iterable_object)  returns->Iterator object

def double(x):
    return x*2

li = [1, 2, 3, 4]

li2 = list(map(double, li))
print(li2)


tup = ('10' ,'20', '30')

# def toInt(x):
#     return int(x)

int_tup = tuple(map(int, tup))
print(int_tup)


li2 = [1, 5, 66]
print(li2)
float_li2 = list(map(float, li2))
print(float_li2)