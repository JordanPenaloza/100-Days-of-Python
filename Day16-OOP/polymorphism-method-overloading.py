class Operations:

    def add(self, a, b):
        return a + b
    
    def add(self, a, b, c):
        return a + b + c
    
math =  Operations()
print(math.add(1, 1))
print(math.add(1, 1, 1))

#python does not support true method overloading