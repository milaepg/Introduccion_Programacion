#Entrada
#Variables necesarios y despensa con lista 
necesarios = [["aceite",2],["azúcar",3],["arroz",1]]
despensa = [["aceite",1],["mantequilla",2],["leche",1]]
#Lista vacia para agregar lo necesario
lista_compra = []
#Iterador
i = 0 
#Mientras que el iterador sea menor al largo de la lista de necesarios 
while i < len(necesarios):
        #Iterador
	j = 0
	#Mientras que j sea menor al largo de la lista de despensa 
	while j < len(despensa):
                #Si los valores de las varaibles son iguales, es decir, si los productos se repiten tanto como en necesarios y despensa  
		if necesarios [i][0] == despensa [j][0]:
                        #Se crea la variable diferencia, donde realiza la operacion de resta entre la cantidad de los productos 
			diferencia = necesarios[i][1] - despensa[i][1]
			#Si la diferencia es mayor que 0
			if diferencia > 0:
                                 #Se agrega a lista_compra la diferencia relizada anteriormente 
				lista_compra.append([despensa[i][0],diferencia])
				j = len(despensa)
		elif (j == len(despensa) -1):
			lista_compra.append([necesarios[i][0],necesarios[i][1]])
		#La iteracion j incrementa en 1	
		j = j+1
	#La iteracion i incrementa en 1	
	i = i +1
#Imprime la lista_compra	
print(lista_compra) 	
             
         
            
             
      
            

















































































