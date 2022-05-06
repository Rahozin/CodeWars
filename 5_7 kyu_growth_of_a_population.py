# # my
# def nb_year(p0, percent, aug, p):
#     percent /= 100
#     n = 0
#     while (p0 < p):
#         p0 = p0 + (p0 * percent)//1 + aug
#         n += 1
#     return n


# best
def nb_year(p0, percent, aug, p, n=0):
    while p > p0:
        p0 += p0*percent/100 + aug
        n += 1
    return n

# # best2
# def nb_year(p0, percent, aug, p, i=0):
#     return i if p0 >= p else nb_year(int(p0+p0*(percent/100)+aug), percent, aug, p, i+1)


if __name__ == '__main__':
    nb_year(300000, 0.5, 1000, 1000000)
