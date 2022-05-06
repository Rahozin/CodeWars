def find_outlier(integers):
    # # the best
    # odds = [x for x in integers if x % 2 != 0]
    # evens = [x for x in integers if x % 2 == 0]
    # return odds[0] if len(odds) < len(evens) else evens[0]

    # second and I think it is the best
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]

    # # my
    # odds = []
    # evens = []
    # for i in integers:
    #     if i % 2 == 0:
    #         odds.append(i)
    #     else:
    #         evens.append(i)
    # if len(odds) == 1:
    #     N = odds[0]
    # else:
    #     N = evens[0]
    # return N


if __name__ == '__main__':
    find_outlier([3, 1719, 19, 11, 160, 13, -21])
