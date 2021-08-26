import math

## Class defintion for ALU
## Reg/reg and reg immediate operations defined here

class ALU:
    def __init__(self):
        self.data = []
        self.c_flag = 0
        self.zflag = 0

    def ADD(self,rs1,rs2,rd):
        rd = rs1+ rs2
        return rd

    def SUB(self,rs1,rs2,rd):
        rd = rs1 - rs2
        return rd
    
    def XOR(self,rs1,rs2,rd):
        rd = rs1^rs2
        return rd
    
    def OR(self,rs1,rs2,rd):
        rd = rs1 |rs2
        return rd
    
    def AND(self,rs1,rs2,rd):
        rd = rs1 & rs2
        return
    
    def SLL(self,rs1,rs2,rd):
        rd = rs1 << rs2
        return rd
    
    def SRL(self,rs1,rs2,rd):
        rd = rs1 >> rs2
        return
    
    def SRA(self,rs1,rs2,rd):
        tmp = rs1 & 8
        rd = rs1 >> rs2
        rd  += tmp
        return rd

    def SLT(self,rs1,rs2,rd):
        rd = rs1 < rs2
        return rd

    def SLTU(self,rs1,rs2,rd):
        rd = math.abs(rs1) < math.abs(rs2)
        return rd

    def ADDI(self,rs1,imm,rd):
        rd = imm+ rs1
        return rd

    def SUBI(self,rs1,imm,rd):
        rd = rs1 - imm
        return rd
    
    def XORI(self,rs1,imm,rd):
        rd = imm^rs1
        return rd

    def ORI(self,rs1,imm,rd):
        rd = imm |rs1
        return
    
    def ANDI(self,rs1,imm,rd):
        rd = imm & rs1
        return
    
    def SLLI(self,rs1,imm,rd):
        rd = rs1 << imm
        return rd
    
    def SRLI(self,rs1,imm,rd):
        rd = rs1 >> imm
        return
    
    def SRAI(self,rs1,imm,rd):
        tmp = rs1 & 8
        rd = rs1 >> imm
        rd  +=tmp
        return rd

    def SLTI(self,rs1,imm,rd):
        rd = rs1 < imm
        return rd

    def SLTIU(self,rs1,imm,rd):
       rd = math.abs(rs1) < math.abs(imm)
       return rd


rd = 0;
my_alu = ALU()

print(my_alu.ADD(1,2,rd))
print(my_alu.SUB(1,2,rd))
print(my_alu.SLL(15,2,rd))
print(my_alu.SRA(11,1,rd))