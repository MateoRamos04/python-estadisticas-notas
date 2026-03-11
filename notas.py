def cantidad_aprobados(v):
    c = 0
    for x in v:
        if x >= 6:
            c += 1
    return c


def cantidad_desaprobados(v):
    c = 0
    for x in v:
        if x < 6:
            c += 1
    return c


def promedio(v):
    total = 0
    for x in v:
        total += x
    prom = round(total / len(v), 2)
    return prom


def nota_maxima(v):
    max_valor = v[0]
    for x in v:
        if x > max_valor:
            max_valor = x
    return max_valor


def nota_minima(v):
    min_valor = v[0]
    for x in v:
        if x < min_valor:
            min_valor = x
    return min_valor


def cargar():
    v = []

    while True:
        try:
            x = int(input('Ingrese una nota del 1 al 10 (0 para finalizar carga): '))

            if x == 0:
                break

            if not 0 < x < 11:
                print('Número inválido.')
            else:
                v.append(x)
        except ValueError:
            print('ERROR. Debe ingresar un número.')
    print('Carga Finalizada...\n')
    return v


def cargar_archivo(v):
    f = open("números.txt", "w")
    for nota in v:
        f.write(str(nota) + "\n")
    f.close()


def principal():
    print('Ejercicio 1 — Estadísticas de números\n'
          '=======================================\n'
          '')
    v = cargar()
    if len(v) == 0:
        print('No se cargaron datos')
        return
    print('Aprobados:', cantidad_aprobados(v))
    print('Desaprobados:', cantidad_desaprobados(v))
    print('Promedio:', promedio(v))
    print('Nota Maxima:', nota_maxima(v))
    print('Nota Minima:', nota_minima(v))
    cargar_archivo(v)


if __name__ == '__main__':
    principal()