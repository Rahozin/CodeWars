# # my
# def dirReduc(arr):
#     i = 1
#     while i < len(arr):
#         if len(arr) < 2:
#             return arr
#         if len(arr[i]) == len(arr[i-1]) and arr[i] != arr[i-1]:
#             arr.pop(i)
#             arr.pop(i-1)
#             if i > 1:
#                 i -= 1
#         else:
#             i += 1
#     return arr

# # best and shortest
# def dirReduc(arr):
#     dir = " ".join(arr)
#     dir2 = dir.replace("NORTH SOUTH", '').replace(
#         "SOUTH NORTH", '').replace("EAST WEST", '').replace("WEST EAST", '')
#     dir3 = dir2.split()
#     return dirReduc(dir3) if len(dir3) < len(arr) else dir3


# best
opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}


def dirReduc(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan


if __name__ == '__main__':
    dirReduc(["NORTH", "SOUTH", "SOUTH",
             "EAST", "WEST", "NORTH", "WEST"])
