tablero: list[list[str]] = [
    ["","X","","","","","","X","",""],
    ["","","","","","","","","",""],
    ["","","","","","","","","",""],
    ["","","","","X","","","","",""],
    ["","","","","","","","","",""],
    ["","","","","X","","","","",""],
    ["","","","","","","","","X",""],
    ["","X","","","","","X","","",""],
    ["","","","","","","","","",""],
    ["","","","","","","","","",""],
]

fila: int = int(input('Ingrese la fila: '))
columna: int = int(input('Ingrese la columna: '))


maxChances = 0
aciertos = 0
errores = 0

while maxChances < 10:
    fila: int = int(input('Ingrese la fila: '))
    columna: int = int(input('Ingrese la columna: '))
    maxChances +=1
    if(fila ==  0 and columna == 1):
        print('Bien')
        aciertos +=1
    elif(fila == 0 and columna == 7):
        print('Bien')
        aciertos +=1
    elif(fila == 3 and columna == 4):
        print('Bien')
        aciertos +=1
    elif(fila == 5 and columna == 4):
        print('Bien')
        aciertos +=1
    elif(fila == 6 and columna == 8):
        print('Bien')
        aciertos +=1
    elif(fila == 7 and columna == 1):
        print('Bien')
        aciertos +=1
    elif(fila == 7 and columna == 6):
        print('Bien')
        aciertos +=1
    else:
        print ('Error')
        errores +=1


print (aciertos)
print (errores)