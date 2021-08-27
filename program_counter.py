
class program_counter():
    def __init__(self):
        self.counter=0
        self.size = 128

    def inc(self):
        self.counter +=1
        return self.counter

    def ld(self,val):
        self.counter = val
        return self.counter

# my_pc = program_counter()

# # for i in range(0,18):
# #     my_pc.inc()
# # print(my_pc.counter)
# # print(my_pc.ld(15))
    