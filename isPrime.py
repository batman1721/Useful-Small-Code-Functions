#Problem 7
import math

def isPrime(n):
    i=2
    if n==1:
        i=0
    elif n<4:
        i=1
    else:
        if n%2==0:
            i=0
        else:
            if n<9:
                i=1
            elif n%3==0:
                i=0
            else:
                r=math.floor(sqrt(n))
                f=5
                while f<=r:
                    if n%f==0:
                        i=0
                        break
                    elif n%(f+2)==0:
                        i=0
                        break
                    f=f+6
    print i
    
isPrime(71)
