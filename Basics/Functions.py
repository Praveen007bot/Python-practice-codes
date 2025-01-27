# Without input adn without return statement
def add():
    a = 10
    b = 20
    print('Addition is:', a+b)

# With input adn without return statement
def sub(a, b):
    print('Substraction is:', a-b)

# Without input adn with return statement
def mul():
    return 10*20

# With input adn with return statement
def div(a, b):
    return a/b

add()
sub(20, 10)
print(mul())
print(div(20, 10))