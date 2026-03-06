def cantidad_aprobados(v):
    c = 0
    for x in v:
        if x >= 6:
            c += 1
    return c
