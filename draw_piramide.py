N = 10
final_size = 1 + (N-1) * 2
mid_point = final_size // 2

for i in range(N):
    left_pad = mid_point - i
    stars = (i * 2) + 1
    print(f"{' '*left_pad}{'*'*stars}")
