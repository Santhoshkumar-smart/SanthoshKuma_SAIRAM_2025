def solve(c):
    words = c.split(' ')
    b = (((i.capitalize() for i in words)))
    return ' '.join(b)
