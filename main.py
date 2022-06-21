edad = int(input('¿Cuantos años tienes?'))

if edad < 18:
    print('Estas chiquito')
elif edad >= 18:
       print('No estas chiquito')

num_ini = int(input('Escribe un numero inicial'))
num_end = int(input('Escribe un numero final'))

for num in range(num_ini, num_end + 1):
    if num % 2 != 0:
        print(num, end = ' ')