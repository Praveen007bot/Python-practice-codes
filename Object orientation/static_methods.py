class MathOperations:

    @staticmethod
    def add(a, b):
        return a + b
    
    def sub(self):
        print("sub")

print(MathOperations.add(5, 10))
m = MathOperations()
m.sub()
print(m.add(2, 3))