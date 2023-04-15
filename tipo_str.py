#tipo string mutable


intento = 1
while intento <=3:
    password = input('Introduzca su contraseña > ')
    if len(password) <= 5 or '-' not in password:
        intento += 1
        print('contraseña incorrecta')
    else:
        break
else:
    print('Número de intentos agotados')