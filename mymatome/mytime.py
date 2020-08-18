import time

nowtime=0

def settime():
    global nowtime
    nowtime = time.time()

def laptime():
    global nowtime
    return time.time()-nowtime

def progress():
    global nowtime
    k = time.time()-nowtime
    nowtime = time.time()
    return k
