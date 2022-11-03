#Entrada
#Define ADN como constante
ADN = "TYHMCQFHCRYVNNHSGEKLYECNERSKAFSCPSHLQCHKRRQIGEKTIIEHNQCGKAFPT"
#Define ARN como constante
ARN = "RTMIGTCTPQNHYECNERSKAFSCPSHLQCHKRRQIGEKTRTMIGMTRCKTPQNHSGIYMP"
#Procesamiento
#Guarda la mayor secuencia encontrada
cadena_max = ""
i = 0
#Mientras i sea menor al largo de la variable ADN
while i < len(ADN):
    j = 0
    index = i
    cadena_tem = ""
    #Mientras j sea menor al largo de la variable ARN
    while j < len(ARN):
        #Recoorre la lista buscando el mayor numero de coincidencia entre ADN y ARN
        if ADN[index] == ARN[j] and index < len(ADN)-1:
            cadena_tem = cadena_tem + ADN[index]
            index = index + 1
            #La iteracion j incrementa en 1
            j = j + 1
        else:
            #La iteracion j incrementa 1 
            j = j + 1
            if len(cadena_max) < len(cadena_tem):
                cadena_max = cadena_tem
            cadena_tem = ""
    #La iteracion i incrementa en 1
    i = i + 1
#Salida
#Imprime lo que contiene la variable cadena_max y el largo de la variable cadena_max
print(cadena_max, "-----Final", len(cadena_max))
