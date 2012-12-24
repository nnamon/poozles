import watch

def main():
    print "To get the secret, you will have to output the following:"
    print "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print "Please enter exactly 13 lines of valid instructions.\n>>>"
    prog = ""
    for i in range(13):
        prog += raw_input() + "\n"
    machine = watch.Machine(prog, io_func=None)
    machine.run()
    if machine.out_log.strip() == "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print file("secret.txt").read()
    else:
        print "That program did not do what we asked for. Processor shutting down."

if __name__ == "__main__":
    main()
