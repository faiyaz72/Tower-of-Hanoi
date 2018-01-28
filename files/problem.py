def problems(n):
    i = n//2
    if i == 1:
        return 1
    else:
        return sum([2*problems(n-i) + (2**i)-1])
