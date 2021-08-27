
class reg_file():
    def __init__(self):
        self.data = [0]*32
    
    def read(self, reg):
        return self.data[reg]

    def write(self, reg, val):
        self.data[reg] = val
        return 

# my_reg = reg_file()


# my_reg.write(3,15)
# print(my_reg.read(3))






