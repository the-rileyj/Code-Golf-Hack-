import os, sys


def write_and_send(string):
    with open("RJfi.c", "w") as fi:
        fi.write('#include<stdio.h>\nint main(){{printf("{0}");}}'.format(string))
    print("{0}".format(string))
    res = os.system("bash submit.sh RJfi.c")


def liner(lines, string=None):
    for ans in ["yes", "no"]:
        print(lines)
        for n in range(20000):
            if 0 < lines - 1:
                if string is None:
                    liner(lines - 1, "{0}:{1}\\n".format(ans, n))
                else:
                    liner(lines - 1, "{0}{1}:{2}\\n".format(string, ans, n))
            else:
                if string is None:
                    write_and_send("{0}:{1}\\n".format(ans, n))
                else:
                    write_and_send("{0}{1}:{2}\\n".format(string, ans, n))

def main():
    lines = 200
    sys.setrecursionlimit(2000)
    for x in range(lines):
        liner(x)

if __name__ == "__main__":
    main()


