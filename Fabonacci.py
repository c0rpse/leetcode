def fabonacci_iteration(n):
    f = [0, 1]
    if n < 0:
        return 0
    if n < 2:
        return f[n]
    f_first, f_second, f_sum = 1, 0, 0
    for cur in xrange(2, n + 1):
        f_sum = f_first + f_second
        f_second = f_first
        f_first = f_sum
    return f_sum


def fabonacci_recuisive(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fabonacci_recuisive(n-1) + fabonacci_recuisive(n - 2)

print fabonacci_iteration(5)
print fabonacci_recuisive(5)
