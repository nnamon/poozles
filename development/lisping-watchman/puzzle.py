import watch

print "Please calculate 4*5 and leave me the answer in the stack."
prog = file("samples/solve").read()
machine = watch.Machine(prog, io_func=None)
machine.run()
if 20 in machine.memory[-1:]:
    print "Here is flag: flag"
else:
    print "Wrong!"
