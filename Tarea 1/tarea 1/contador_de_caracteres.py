frase = input('digite una palabra o frase ')
busqueda = input('digite la letra que le gustaria buscar ')
largo = len(frase)
print(f'en la frase o palabra digitada con una cantidad de {largo} caraccteres, la letra "{busqueda}" aparece un total de {frase.count(busqueda)} cantidad de vecas')