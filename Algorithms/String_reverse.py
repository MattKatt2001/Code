def order(x):

    y = []
    i = len(x[0])
    i = i - 1

    while i >= 0:
        y.append(x[0][i])
        i -= 1

    for i in y:
        print(i, end = '')

order(["123456789"])#enter a string returns reversed
