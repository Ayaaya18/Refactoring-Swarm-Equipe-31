def f(x):
    y = []
    for i in x:
        if i % 2 == 0:
            y.append(i*2)
        else:
            y.append(i)
    return y