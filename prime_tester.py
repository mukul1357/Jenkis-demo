#!/usr/bin/python3
def prime_tester(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                return(False)
        else:
            return(True)
    else:
        return(False)