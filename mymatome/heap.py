import heapq
from mycopy import *

class Heap:
    def __init__(self,mm=False):
        self.h = []
        self.sign = 1
        if mm:
            self.sign = -1

    def push(self,n):
        heapq.heappush(self.h,n*self.sign)
        print(self.h)

    def pop(self):
        k = heapq.heappop(self.h)*self.sign
        return k

def heapsort(h):
    k = copyC(h)
    ran = len(k.h)
    return [k.pop() for i in range(ran)]



if __name__=='__main__':
    import rand
    heap = Heap(True)
    h = rand.randIs(1,20,10)
    print(h)
    for i in h:
        heap.push(i)
    print(heapsort(heap))
