
def ratio(x, min_x, max_x, new_min, new_max):
    x = float(x)
    """
    if (x < min_x):
        x = min_x
    if (x > max_x):
        x = max_x
    """
    old_range = max_x - min_x
    new_range = new_max - new_min
    if (old_range == 0):
        old_range = 1
    res = ((x - min_x) / old_range) * new_range + new_min
    return (res)
