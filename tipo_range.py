#tipo range inmutable que sirve
# para generar una secuencia de números para utilizarlo con un iterable

r = range(4,9,2)
print(list(r))

# tabla de multiplicar 

tabla = 5

for i in range(1, 11):
    print(f'{tabla}*{i}={tabla*i}')
