
import sys
import time
def stdprint(a):
    for i in a:
        sys.stdout.write(a[:i])
        time.sleep(0.1)
        sys.stdout.flush()
a=input("a string")
stdprint(a)
