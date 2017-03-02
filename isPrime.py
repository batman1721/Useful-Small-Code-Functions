#Problem 7
import math

def isPrime(n):
    if n==1:
        return False
    elif n<4:
        return True
    else:
        if n%2==0:
            return False
        else:
            if n<9:
                return True
            elif n%3==0:
                return False
            else:
                r=math.floor(math.sqrt(n))
                f=5
                while f<=r:
                    if n%f==0:
                        return False
                    elif n%(f+2)==0:
                        return False
                    f=f+6
                return True

