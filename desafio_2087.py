def v(x):
    x.sort()
    for i in range(1, len(x)):
        if x[i].startswith(x[i - 1]):
            return False
    return True
a = []
while True:
    try:
        n = int(input())
        if n == 0:
            break
        if 1 <= n <= 100000:
            x = [input().strip() for _ in range(n)]
            a.append(x)
    except ValueError:
        pass
for x in a:
    if v(x):
        print("Conjunto Bom")
    else:
        print("Conjunto Ruim")
