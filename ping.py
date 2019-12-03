# Python-Synology-UPS-Shutdown
# Wecent www.wx256.com
# Synology QQ Qun 54123646
import os
import time
import re
import sys


def pingMaster(masterip='127.0.0.1', delay='10', count=10, islog='true'):
    run = True
    loss = 0

    if islog == 'true':
        t = int(time.time())
        fname = "./pinglog_%s.txt" % t
        f = open(fname, "a+")

    while run:
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        ping = os.popen('ping %s -c 1' % (masterip)).read()
        bytesReturn = re.findall(r'(.*?) bytes from', ping)
        if bytesReturn:
            loss = 0
            print('pinging')
            if islog == 'true':
                f.write(now + " " + "pinging")
                f.write("\r\n")
        else:
            loss = loss + 1
        if loss > count:
            run = False
            print('shutdown')
            if islog == 'true':
                f.write(now + " " + "shutdown")
                f.write("\r\n")
                f.close()
            os.popen('init 0')

        if os.path.exists("stop.txt") or os.path.exists("stop"):
            run = False
            print('exit')
            if islog == 'true':
                f.write(now + " " + "exit")
                f.write("\r\n")
                f.close()
            exit()
        time.sleep(delay)


if __name__ == "__main__":
    try:
        ip = str.strip(sys.argv[1])
        delay = float(sys.argv[2])
        count = int(sys.argv[3])
        islog = str.strip(str.lower((sys.argv[4])))

    except:
        print("param is null")
        f = open('./error', "a+")
        f.close()
        exit()
    if os._exists('./error'):
        os.remove('./error')
    pingMaster(ip, delay, count, islog)
