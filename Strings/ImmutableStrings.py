# Python Internally uses String interning.
# String interning is the proccess of checking string intern pool before creating any new object.
# Whenever we want to create new object, python first check string intern poll weather that object is already exist or not.
# when object already exist in the string interning records then address of existing object will be reused. 

s1 = 'Hello'
s2 = 'World'
print(s2)
print(s1, id(s1))
print(s2, id(s2))

print('Id of K:', id(s1[0]))
print(s1[-1])

print('s2 id of o:',id(s2[1]))
print('s1 id of o:', id(s1[-1]))

print('s1 id of l:',id(s1[2]))
print('s1 id of l:', id(s1[3]))
print('s2 id of l:',id(s2[3]))