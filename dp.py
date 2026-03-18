import sys

N = int(sys.argv[1])

min = 1
max = N * 2 + 1
padding = N

for r in range(N):
    # print(f"{' ' * (padding + r)}{'#' * (max - r * 2)}{' ' * (padding + r)}")
    padding -= 1
    draw = r * 2 + 1
    print(f"{' ' * padding}{'#' * draw}{' ' * padding}")
