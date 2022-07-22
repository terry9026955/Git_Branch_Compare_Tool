import sys
import time

sys.setrecursionlimit(100000000)



def main(depth):
    depth += 1
    print("Depth: ", depth)
    #time.sleep(1)
    main(depth)






if __name__ == '__main__':
    #sys.setrecursionlimit(15)
    print(sys.getrecursionlimit())

    main(0)
    