def pr(a):
    print(a,end="")

def pl(a):
    print(a)

def pls(*a):
    prA(a)

def prA(a):
    print(a[0],end="")
    for i in a[1:]:
        sp(),print(i,end="")
    ind()

def prAs(a):
    for i in a:
        if type(i) is list or type(i) is tuple:
            prA(i)
        else:
            pl(i)

def ind():
    print("")

def sp():
    print(" ",end="")

if __name__=="__main__":
    pr(3),sp()
    pl("a")
    ind()
    a = [1,2,4]
    pl(a)
    prA("as")
    b=[[1,2,[1,2]],2]
    prAs(b)
    pls(1,2,3)
