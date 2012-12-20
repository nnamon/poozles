import watch

print "Enter program (# to end):"
prog = ""
while True:
    line = raw_input()
    if line == "#":
        break
    prog += line + "\n"
machine = watch.Machine(prog, io_func=None)
machine.run()
print machine.out_log
