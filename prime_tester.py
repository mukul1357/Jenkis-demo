def prime_tester(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                # print(num, "is not a prime number")
                return(False)
                break
        else:
            # print(n, "is a prime number")
            return(True)
    # If the number is less than 1, its also not a prime number.
    else:
        # print(n, "is not a prime number")
        return(False)