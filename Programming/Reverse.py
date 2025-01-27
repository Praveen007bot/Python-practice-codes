# reverse() will
li = [10, 5, 20, 7, 40]
print(li)
li.reverse()
print(li)

# Return interator object
li2 = [11, 6, 8, 22]
rev = list(reversed(li2))
print(rev)

li3 = [1, 5, 2, 9]
new_rev = list(reversed(li3)) # Creating new reverse list
print(new_rev)
li3.reverse() # reversing the acutal list
print(li3)