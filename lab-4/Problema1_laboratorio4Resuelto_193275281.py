import random 
def genera_caminata(n):
    #LISTA DE MOVIMIENTOS ALEATORIOS POSIBLES
    numeros = [[0,1],[0,-1],[1,0],[-1,0]]
    posicion = [0,0]
    caminata = [posicion]
    pasos = (2*n)+1
    i = 1
    while i < pasos:
        existe = False
        aleatorio = random.sample(numeros , 1)
        suma = [posicion[0]+aleatorio[0][0], posicion[1]+aleatorio[0][1]]
        j = 0
        #SI YA NOS MOVIMOS A ESTA POSICION NO CUENTA COMO UN MOVIMIENTO NUEVO
        while j < len(caminata):
            if suma == caminata[j]:
                j = j + 1
                existe = True
            else: 
                j = j + 1 
        if existe == False:
                i = i + 1     
        caminata.append(suma)
        posicion = suma
    return caminata

def grafica_caminata(n, lista):
    #OBTENER EL NUMERO MAYOR GENERADO EN LA CAMINATA
    i = 0
    numMayor = 0
    while i < len(lista):
        x = lista[i][0]
        y = lista[i][1]
        if abs(x) > numMayor:
            numMayor = abs(x)
        if abs(y) > numMayor: 
            numMayor = abs(y)
        i = i + 1
        
    #GENERAR PLANO
    numPlano = -numMayor
    ejeX = numMayor*2+1
    plano = []
    #SE CREA EL EJE X/Y, RELLENANDO EL EJE X CON 0
    while numPlano <= numMayor:
        textoVacio = ''
        ejeY = [numPlano, textoVacio.zfill(ejeX)]
        plano.append(ejeY)
        numPlano = numPlano + 1

    #GENERAR LAS X EN EL PLANO
    j = 0
    while j < len(lista):
        n=0
        #BUSCAMOS COINCIDENCIAS CON EL EJE Y, LUEGO MODIFICAMOS CON UNA X MEDIANTE LA POSICION DEL EJE X
        while n < len(plano):
            yLista = lista[j][1]
            yPlano = plano[n][0]
            if  yLista == yPlano:
                pos = 0
                s = list(plano[n][1])
                pos = lista[j][0]
                pos = pos + numMayor
                s[pos] = 'X'
                plano[n][1] = "".join(s)
            n = n +1
        j = j + 1
        
    #IMPRIMIR PLANO CARTECIANO DESDE EL +Y HASTA EL -Y
    p = numMayor
    cadenaTexto = ''
    while p >= -len(plano):
        z = 0
        #LLAMAMOS AL PLANO CARTECIANO, CONCATENANDO CADA EJE X CON UN SALTO DE LINEA AL FINAL DE CADA UNO
        while z < len(plano): 
            yPlano = plano[z][0]
            if  p == yPlano:
                cadenaTexto = cadenaTexto + str(plano[z][1]) + '\n'
            z = z +1
        p = p -1 
    return cadenaTexto

#ENTRADA
numero = int(input("Ingrese un número entero positivo: "))
#PROCESO
caminata = genera_caminata(numero)
grafico = grafica_caminata(numero, caminata)
#SALIDA
print("La lista de puntos visitados en la caminata es:")
print(caminata)
print("La representación gráfica de la caminata es:")
print(grafico)
