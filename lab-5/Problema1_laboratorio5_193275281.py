#Integrantes Camila Prado, Emilio Viñals

from math import sqrt
#Funciones
def separar_archivo_lista(nombre):
    '''
    toma el archivo en nombre, lo abre, lee cada una de las lineas en un for
    le elimina el elemento \n y los separa en una lista por las comas "," y lo
    agrega una nueva lista, cierra el archivo y devuelve una lista de listas
    '''
    nombre = nombre + ".txt"
    archivo = open(nombre,'r')
    lista = []
    for linea in archivo:
        linea = linea.strip("\n").split(",")
        lista.append(linea)
    archivo.close()
    return lista

def calcular_distancia(centros, encomiendas):
    '''
    toma la lista de centros y encomiendas, recorre las encomiendas y busca la distancia más corta entre cada centro
    guarda esa informacioin y la devuelve en una lista con el id, las coordenadas, el centro más cercano y su distancia
    '''
    salida = []
    i = 1
    while i < len(encomiendas):
        j = 1
        x = -1
        centro = ""
        coordenadas = ""
        while j < len(centros):
            d = sqrt((int(centros[j][1]) - int(encomiendas[i][1]))**2 + (int(centros[j][2]) - int(encomiendas[i][2]))**2)
            if x == -1 or d < x:
                x = d
                centro = centros[j][0]
                coordenadas = str(encomiendas[i][1] + "," + encomiendas[i][2])
            if j == len(centros)-1:
                salida.append([encomiendas[i][0],coordenadas,centro, d])
            j+=1
        i+=1
    return salida

def lista_texto(lista):
    '''
    Transforma la lista completa en un string
    '''
    texto = "ID, Cordenada x, Cordenada y, Nombre del Centro, distancia \n"
    for linea in lista:
        texto = texto + str(linea) + "\n"
    return texto

#Entrada
centros = "Centros de despacho"
encomiendas = "Encomiendas"

#Desarrollo
'''
Genera la lista con los centros, las encomiendas y la final con toda la información, luego la transforma en texto
y la escribe en el archivo "Asignacion de encomiendas"
'''
lista_centros = separar_archivo_lista(centros)
lista_encomiendas = separar_archivo_lista(encomiendas)
final = calcular_distancia(lista_centros, lista_encomiendas)
texto_final = lista_texto(final)

salida = open("Asignacion de encomiendas.text", "w")
salida.write(texto_final)
salida.close()
