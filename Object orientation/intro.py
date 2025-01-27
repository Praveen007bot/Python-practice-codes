class student:
    def learn(self):
        print(self.name,"Inside Learn Method")

    def play(self):
        print("Inside Play method")

s1 = student()
s1.play()
s1.name = 'Muzaffar'
print(s1.name)
s1.learn()