import os
import sys
import reg_file
import ALU
import time


class control_unit:
    def __init__(self,ALU,reg_file):
        self.current_instruction = 0x0
        self.ALU = ALU
        self.reg_file = reg_file
        self.opcode = 0x0
        self.rs1 = 0x0
        self.rs2 = 0x0
        self.rd = 0x0
        self.funct7 = 0x0
        self.funct3 =0x0
        self.imm = 0x0
        self.instr = ""
        self.tmp = 0

    def decode(self,instruction):
        self.current_instruction = instruction
        self.opcode=(instruction&0x7F)

        ##ALU REG-REG function
        if(self.opcode ==0x33):

            ##Take Register Values Now...
            self.rs1 = (self.current_instruction & 0x01F00000) >>20
            self.rs2 = (self.current_instruction & 0x000F8000) >>15
            self.rd = (self.current_instruction  & 0x00000F80) >> 7

            #Check what operation is requested
            self.funct3 =(self.current_instruction & 0x00007000) >>12
            #print(self.funct3)

            if(self.funct3 == 0x0):
                ##30th bit tells you add or subtract
                if((self.current_instruction & 0x40000000) >>30):
                    self.instr="SUB"
                else:
                    ##Decode
                    self.instr = "ADD" ## incorporate global table somehow then just reference entry
                    #print("ADD")

                    ##Execute/WB
                    # print(hex(rd))
                    # print(rs1)
                    # print(rs2)
                    # self.reg_file.write(rd,self.ALU.ADD(rs1,rs2))
                    # print(self.reg_file.read(rd))

            ##Execute cycle not technically "Control Unit" but this logic can live here for now...
    
    
    def execute(self):
        if (self.instr=="ADD"):
            self.tmp = (self.ALU.ADD(self.rs1,self.rs2))
            self.reg_file.write(self.rd,self.tmp)
           #print(self.reg_file.read(self.rd))

    def write_back(self):
        self.reg_file.write(self.rd,self.tmp)





my_alu = ALU.ALU()
my_reg = reg_file.reg_file()
my_cu = control_unit(my_alu,my_reg)


##PC.inc -> that value in instruction memory
##That value --> Decode
##Decode settings -->execute
##Execute --> Write back to memory
start = time.perf_counter()
my_cu.decode(0x00A184B3)
print(time.perf_counter() - start)
##Standard Execute
my_cu.execute()
print(time.perf_counter() - start)
my_cu.write_back()
print(time.perf_counter() - start)

