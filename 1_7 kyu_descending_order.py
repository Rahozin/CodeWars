def descending_order(num):
    # my and the best
    return int(''.join(sorted(str(num), reverse=True)))


if __name__ == '__main__':
    descending_order(int(input("Any non negative integer number: ")))
