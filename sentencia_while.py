a = 1
# mostrar una cuenta del 1 a 10
# while a <= 10:
#     print(a)
#     a+=1

# mostrar  cuenta de 2 en 2 hast llegar al 10
# while a <= 10:
#     if a % 2 == 0:
#         print(a)
#     a+=1

opcion = 0
var_1 = 3
var_2 = 5
while opcion != -1:
    opcion = int(input('Introduzca una opción: >'))
    if opcion == 1:
        print(f'{var_1} + {var_2} = {var_1+var_2}')
    elif opcion == 2:
        print(f'{var_1} - {var_2} = {var_1-var_2}')
    elif opcion == 3:
        print(f'{var_1} * {var_2} = {var_1*var_2}')
    elif opcion == -1:
        pass
    else:
        print('Opción invalida')