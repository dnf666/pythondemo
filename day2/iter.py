import sys

list = [1, 2, 3, 4, 5, 6, 7]
ite = iter(list)

while True:
    try:
        print(next(ite))
    except StopIteration:
        sys.exit()

