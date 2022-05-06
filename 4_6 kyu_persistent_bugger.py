from operator import mul
from functools import reduce


# # my
# def persistence(n):
#     persistence = 0
#     while (len(str(n)) > 1):
#         persistence += 1
#         num = 1
#         for digit in str(n):
#             num = num * int(digit)
#             n = num
#     return persistence


# # best
# def persistence(n):
#     i = 0
#     while n >= 10:
#         n = reduce(mul, [int(x) for x in str(n)], 1)
#         i += 1
#     return i

# best2
def persistence(n):
    return 0 if n < 10 else persistence(reduce(mul, [int(i) for i in str(n)], 1))+1


if __name__ == '__main__':
    persistence(1719)
