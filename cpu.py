import ALU as alu
import program_counter as pc
import reg_file as reg

class cpu():
    def __init__(self):
        self.data = 0
        self.alu = alu.ALU()
        self.program_counter = pc.program_counter()
        self.reg_file = reg.reg_file()

rd = 0

my_cpu = cpu()

rd = my_cpu.alu.ADD(6,2,rd)
my_cpu.reg_file.write(3,my_cpu.alu.ADD(6,2,rd))
print(rd)
#my_cpu.reg_file.write(3,rd)
print(my_cpu.reg_file.read(3))    