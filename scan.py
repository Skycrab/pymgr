import time

with open('scan.log','w') as f:
    for x in range(1000):
        f.write("%s\n" % x)
        sleep(1)
