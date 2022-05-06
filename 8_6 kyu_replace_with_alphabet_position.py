# my
# def alphabet_position(text):
#     numeric = []
#     for a in text:
#         if a.isalpha():
#             if ord(a) > 90:
#                 numeric.append(str(ord(a) - 96))
#             else:
#                 numeric.append(str(ord(a) - 64))
#     return ' '.join(numeric)


# best and shortest
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


if __name__ == '__main__':
    alphabet_position("AlexMax")
