def smallest_multiple(x, y):
    z = y
    for i in range(x, y):
        if not z % i == 0:
            break 
        else return
    