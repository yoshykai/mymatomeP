def readL():
    return input()

def readI():
    return int(input())

def readS():
    return input().split(' ')

def readIs():
    a =  readS()
    return [int(a[i]) for i in range(len(a))]

if __name__=='__main__':
    print(readIs())
