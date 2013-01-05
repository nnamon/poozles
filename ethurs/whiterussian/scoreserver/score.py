#!/usr/bin/python
# Run with socat -T 20 TCP-LISTEN:9999,fork EXEC:./score.py

import sys
from datetime import datetime
from operator import itemgetter

root = "$"

def print_io(to_print, newline=True):
    n = ""
    if newline: n = "\n"
    sys.stdout.write(to_print+n)
    sys.stdout.flush()

def raw_io(to_print):
    print_io(to_print, False)
    return sys.stdin.readline().strip()

def print_welcome():
    welcome = """
%s
Welcome to the Nandy Narwhals score server.
What do you wish to do?
1. Submit flag
2. View scoreboard
3. Get root
4. Exit""" % file("southpark").read()

    print_io(welcome)

def view_scoreboard():
    pass

def parse_scoreboard():
    raw = file("scoreboard").read()
    raw_l = raw.split("\n")
    scores = []
    for i in raw_l:
        if not i == "":
            scores.append(i.split(":::"))
    return scores

def parse_flagfile():
    raw = file("flags").read()
    raw_l = raw.split("\n")
    flags = []
    for i in raw_l:
        if not i == "":
            flags.append(i.split(":"))
    return flags
    
def validate_pid(pid):
    flags = parse_flagfile()
    pids = [i[0] for i in flags]
    return pid in pids

def validate_flag(pid, flag):
    flags = parse_flagfile()
    for i in flags:
        if i[0] == pid:
            if i[1] == flag:
                return int(i[2])
    return -1

def validate_done(name, pid):
    scores = parse_scoreboard()
    for i in scores:
        if i[1] == name:
            if i[2] == pid:
                return False
    return True

def submit_flag():
    name = raw_io("your name/handle: ")
    pid = raw_io("challenge id: ")
    flag = raw_io("flag: ")
    if not validate_pid(pid):
        print_io("Bad challenge id!")
        return
    score = validate_flag(pid, flag)
    if score < 0:
        print_io("Invalid flag for %s!" % pid)
        return
    if ":::" in name:
        print_io("Invalid name!")
        return
    if not validate_done(name, pid):
        print_io("You've already done this one! Try another!")
        return
    print_io("Well done! Flag submitted successfully")
    file("scoreboard", "a").write("%s:::%s:::%s:::%d\n" % (datetime.utcnow(), name, pid, score))

def view_scoreboard():
    print_io("Scoreboard: ")
    scores = parse_scoreboard()
    leaders = {}
    for i in scores:
        if i[1] not in leaders.keys():
            leaders[i[1]] = int(i[3])
        else:
            leaders[i[1]] += int(i[3])
    sort = sorted(leaders.items(), key=itemgetter(1), reverse=True)
    for i in range(len(sort)):
        print_io("%d. %-20s  -  %s" % (i, sort[i][0], sort[i][1]))


def parse_command(command):
    command = command.strip()
    if command == "1":
        submit_flag()
    elif command == "2":
        view_scoreboard()
    elif command == "3":
        global root
        root = "#"
        print_io("Okay, you're root.")
    elif command == "4":
        print_io("Quitting...")
        quit()
    elif command == "1337":
        print_io("Way 1337. Here's your flag: aHR0cDovL3d3dy55b3V0dWJlLmNvbS93YXRjaD92PWRRdzR3OVdnWGNRCg==")
    else:
        print_welcome()

def main():
    print_welcome()
    while True:
        command = raw_io("you@nandy%s " % root)
        parse_command(command)

if __name__ == "__main__":
    try:
        main()
    except:
        print_io("Okay, bye bye.")
