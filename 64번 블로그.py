def continued_fraction(n:int) -> [int]:
    NR = int(n **0.5)
    if NR * NR == n:
        return [NR]
    a = NR
    b = -NR
    c = 1
    cache = [(a, b, c)]
    result = [a]

    def get_next_fraction(b, c):
        cn = (n - b*b) // c
        an = (NR - b) // cn
        bn = -b - an * cn
        return (an, bn, cn)

    while True:
        p = get_next_fraction(b, c)
        if p in cache:
            return result
        cache.append(p)
        a, b, c = p
        result.append(a)

def p64():
    xs = [continued_fraction(i) for i in range(2, 10001)]
    print(sum((1 for x in xs if len(x) % 2 == 0)))
p64()