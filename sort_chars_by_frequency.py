def sort_by_freq(input: str) -> str:
    f = {}
    for s in input:
        if s in f:
            f[s] += 1
        else:
            f[s] = 1
    sor = sorted(f.items(), key=lambda item: item[1], reverse=True)
    result = []
    for k,v in sor:
        for _ in range(v):
            result.append(k)
    return ''.join(result)

input = "tree"
print(sort_by_freq(input))
