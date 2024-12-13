
while True:
    n = int(input())
    dc = []
    if n == 0:
        break

    x = [i for i in range(1, n + 1)]

    while len(x) != 2:
        dc.append(x[0])
        x.pop(0)
        if len(x) == 2: break
        val_base = x[0]
        x.pop(0)
        x.append(val_base)
    
    dc.append(x[1])
    print("Discarded cards: " + ", ".join(str(i) for i in dc))
    print("Remaining card: " + str(x[0]))
