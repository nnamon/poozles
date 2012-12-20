
import watch, sys
while True:
    out = raw_input(">>> ")
    mach = watch.Machine(file(out).read(), None)
    mach.run()
    print mach.out_log


