def _sqrt(x):
    l, r = 0, x
    while l <= r:
        mid = (r - l) // 2
        if mid*mid <= x <= (mid + 1)*(mid + 1):
            return mid
        elif x < mid*mid:
            r = mid
        else:
            l = mid

    
