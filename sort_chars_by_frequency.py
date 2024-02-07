from typing import Counter

input = "tree"

# beats 28%
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

# beats 28%
def sort_by_freq(input: str) -> str:
    f = Counter(input)
    sor = sorted(f.items(), key=lambda item: item[1], reverse=True)
    result = []
    for k,v in sor:
        for _ in range(v):
            result.append(k)
    return ''.join(result)

# beats 60%
def sort_by_freq2(input:str) -> str:
    c = Counter(input)
    r = sorted(c.items(), key=lambda i: i[1], reverse=True)
    return "".join([char * freq for char, freq in r])
print(sort_by_freq2(input))
