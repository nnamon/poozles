import sys
import traceback

class Machine:

    def __init__(self, text, io_func=sys.stdout.write, run=False, memory_size=100, clock_max=5000):
        self.prog_l = text.split("\n")
        self.memory = [0 for i in range(memory_size)]
        self.io_func = io_func
        self.reset()
        self.clock_max = clock_max
        if run:
            self.run()

    def reset(self):
        self.clock = 0
        max_mem = len(self.memory)-1
        self.registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 
                          'e': 0, 'f': 0, 'g': 0, 'i': 0, 
                          's': max_mem, 'p': max_mem}
        self.flags = {'z': 0}
        self.out_log = ""

    def run(self):
        self.reset()
        while True:
            if self.clock == self.clock_max:
                self.io_write("Clock max iterations reached!")
                return
            if self.registers['i'] in range(len(self.prog_l)):
                tokens = self.prog_l[self.registers['i']].split()
                if len(tokens) > 0:
#                    print "Clock %d" % (self.clock)
                    if not "#" in tokens[0]:
                        try:
                            self.evaluate(tokens)
                        except TypeError:
                            traceback.print_exc()
                            self.io_write("Bad input file! Except on line %d. Terminating.\n" % self.clock)
                            return
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
                 'drf': [2, self.__ins_drf],
                 'lrf': [2, self.__ins_lrf],
                 'push': [1, self.__ins_push],
                 'pop': [1, self.__ins_pop],
                 'mtm': [2, self.__ins_mtm],
                 'rtr': [2, self.__ins_rtr],
                 'nop': [0, self.__ins_nop],
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
        if self.io_func: self.io_func(io)
        self.out_log += io

    def __int_step(self):
        self.registers['i'] += 1

    def __ins_nop(self):
        self.__int_step()

    def __ins_drf(self, dest, src):
        addr = -1
        if src.isdigit():
            val_i = int(src)
            if self.is_mem(src):
                addr = self.memory[val_i]
        elif self.is_reg(src):
            addr = self.registers[src]
        
        if addr in range(len(self.memory)):
            if dest.isdigit():
                val_i = int(dest)
                if self.is_mem(dest):
                    self.memory[val_i] = self.memory[addr]
            elif self.is_reg(dest):
                self.registers[dest] = self.memory[addr]
        self.__int_step()

    def __ins_lrf(self, dest, src):
        addr = -1
        if dest.isdigit():
            val_i = int(dest)
            if self.is_mem(dest):
                addr = self.memory[val_i]
        elif self.is_reg(dest):
            addr = self.registers[dest]

        if addr in range(len(self.memory)):
            if src.isdigit():
                val_i = int(src)
                if self.is_mem(src):
                    self.memory[addr] = self.memory[val_i]
            elif self.is_reg(src):
                self.memory[addr] = self.registers[src]
        self.__int_step()

    def __no_ins(self):
        print "no such instruction"
        self.__int_step()

    def __ins_push(self, reg):
        if self.is_reg(reg):
            val = self.registers[reg]
            self.memory[self.registers['s']] = val
            self.registers['s'] -= 1
        self.__int_step()

    def __ins_pop(self, reg):
        if self.is_reg(reg):
            self.registers['s'] += 1
            self.registers[reg] = self.memory[self.registers['s']]
        self.__int_step()
    
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

    def __ins_rtr(self, dest, src):
        if self.is_reg(dest) and self.is_reg(src):
            self.registers[dest] = self.registers[src]
        self.__int_step()

    def __ins_mtm(self, dest, src):
        if dest.isdigit() and src.isdigit():
            if self.is_mem(dest) and self.is_mem(src):
                self.memory[int(dest)] = self.memory[int(src)]
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
    machine = Machine(file(sys.argv[1]).read(), run=True, memory_size=200)

if __name__ == "__main__":
    main()
