import sys

class Machine:
    clock = 0
    prog_l = ""
    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'i': 0, 's': 0}
    memory = [0 for i in range(100)]
    flags = {'z': 0}

    def __init__(self, text):
        self.prog_l = text.split("\n")        
        self.run()
    
    def run(self):
        while True:
            if self.registers['i'] in range(len(self.prog_l)):
                tokens = self.prog_l[self.registers['i']].split()
                if len(tokens) > 0:
#                    print "Clock %d" % (self.clock)
                    if not "#" in tokens[0]:
                        self.evaluate(tokens)
                        self.clock += 1
                    else: self.__int_step()
                else: break
            else: break


    def evaluate(self, instr_l):
        instr = instr_l[0].lower()
        arg_len, func = self.get_desc(instr)
        func(*instr_l[1:arg_len+1])
        
    def get_desc(self, instr):
        # [arg_len, func]
        descs = {'set': [2, self.__ins_set],
                 'add': [2, self.__ins_add],
                 'sub': [2, self.__ins_sub],
                 'put': [1, self.__ins_put],
                 'cmp': [2, self.__ins_cmp],
                 'movm': [2, self.__ins_movm],
                 'movr': [2, self.__ins_movr],
                 'inc': [1 ,self.__ins_inc],
                 'dec': [1 ,self.__ins_dec],
                 'jmp': [1, self.__ins_jmp],
                 'je': [1, self.__ins_je],
                 'jne': [1, self.__ins_jne],
                 'dump': [0, self.__deb_dump],
                 'dumpm': [0, self.__deb_dumpm],}
        if instr in descs.keys():
            return descs[instr]
        else:
            return (0, self.__no_ins)

    def is_reg(self, reg):
        return reg in self.registers.keys()
    
    def is_mem(self, mem):
        if mem.isdigit():
            mem_loc = int(mem)
            if mem_loc >= 0 and mem_loc < len(self.memory):
                return True
        return False

    def io_write(self, io):
        sys.stdout.write(io)

    def __int_step(self):
        self.registers['i'] += 1

    def __no_ins(self):
        print "no such instruction"
    
    def __ins_jmp(self, addr):
        if addr.isdigit():
            self.registers['i'] = int(addr)

    def __ins_je(self, addr):
        if addr.isdigit() and self.flags['z'] == 0:
            self.registers['i'] = int(addr)
        else:
            self.__int_step()

    def __ins_jne(self, addr):
        if addr.isdigit() and self.flags['z'] != 0:
            self.registers['i'] = int(addr)
        else:
            self.__int_step()

    def __ins_inc(self, dest):
        if self.is_reg(dest):
            self.registers[dest] += 1
        self.__int_step()

    def __ins_dec(self, dest):
        if self.is_reg(dest):
            self.registers[dest] -= 1
        self.__int_step()

    def __ins_add(self, dest, add):
        if self.is_reg(dest) and self.is_reg(add):
            res = self.registers[dest] + self.registers[add]
            self.registers[dest] = res
        self.__int_step()

    def __ins_sub(self, dest, sub):
        if self.is_reg(dest) and self.is_reg(sub):
            res = self.registers[dest] - self.registers[sub]
            self.registers[dest] = res
        self.__int_step()

    def __ins_set(self, dest, val):
        # all instructions fail silently.
        neg = 1
        if "-" in val:
            neg = -1
            val = val[1:]
        if val.isdigit():
            val_i = int(val)*neg
            if self.is_reg(dest):
                self.registers[dest] = val_i
            elif self.is_mem(dest):
                self.memory[int(dest)] = val_i
        self.__int_step()

    def __ins_movm(self, dest, src):
        if src.isdigit():
            val_i = int(src)
            if self.is_mem(src):
                if self.is_reg(dest):
                    self.registers[dest] = self.memory[val_i]
        self.__int_step()

    def __ins_movr(self, dest, src):
        if self.is_reg(src):
            if dest.isdigit():
                val_i = int(dest)
                if self.is_mem(dest):
                    self.memory[val_i] = self.registers[src]
        self.__int_step()

    def __ins_put(self, src):
        io = ""
        if self.is_reg(src):
            io = self.registers[src]
        elif self.is_mem(src):
            io = self.memory[int(src)]
        if io in range(256):
            self.io_write(chr(io))
        self.__int_step()

    def __ins_cmp(self, dest, comp):
        if self.is_reg(dest) and self.is_reg(comp):
            res = 0
            a = self.registers[dest]
            b = self.registers[comp]
            if a > b: res = 1
            if a < b: res = 2
            self.flags['z'] = res
        self.__int_step()

    def __deb_dump(self):
        self.io_write("\nRegisters: %s\nFlags: %s\n" % (self.registers, self.flags))
        self.__int_step()

    def __deb_dumpm(self):
        mem_dump = [" ".join(map("{:04d}".format, i)) for i in list(chunks(self.memory, 10))]
        io = ""
        for i in range(len(mem_dump)):
            io += "%04d: %s\n" % (i*10, mem_dump[i])
        self.io_write("\nMemory:\n%s" % io)
        self.__int_step()

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]
                        
def main():
    machine = Machine(file(sys.argv[1]).read())

if __name__ == "__main__":
    main()
