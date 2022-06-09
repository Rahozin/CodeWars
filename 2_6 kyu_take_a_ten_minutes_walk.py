def is_valid_walk(walk):
    # the best
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

    # # my
    # if len(walk) != 10:
    #     return False
    # vert_position = 0
    # hor_position = 0
    # for char in walk:
    #     if char == 'n':
    #         vert_position = vert_position + 1
    #     if char == 's':
    #         vert_position = vert_position - 1
    #     if char == 'e':
    #         hor_position = hor_position + 1
    #     if char == 'w':
    #         hor_position = hor_position - 1
    # if vert_position == 0 and hor_position == 0:
    #     return True
    # else:
    #     return False


if __name__ == '__main__':
    is_valid_walk('nsnsnsnsns')
