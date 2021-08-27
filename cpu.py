import ALU as alu
import program_counter as pc
import reg_file as reg

class cpu():
    def __init__(self):
        self.data = 0
        self.alu = alu.ALU()
        self.program_counter = pc.program_counter()
        self.reg_file = reg.reg_file()

rd = 5

my_cpu = cpu()

my_cpu.reg_file.write(rd,my_cpu.alu.ADD(6,2))
print(my_cpu.reg_file.read(rd))

##Fetch
##Read instruction for instruction cache


##Decode
##Turn op code into control signals for CPU

##Execute
##perform alu operation/any other operation (e.g. branch/push to stack/etc.)

##Write Back
##Update registers