#Lista con abecesario con respectivo codigo morse
morse = [['A','·−'],['B','−···'],['C','-·-·'],['D','-··'],['E','·'],['F','··-·'],['G','--·'],['H','····'],['I','··'],['J','·---'],['K','-·-'],['L','·-··'],['M','--'],['N','-·'],['O','---'],['P','·--·'],['Q','--·-'],['R','·-·'],['S','···'],['T','-'],['U','··-'],['V','···-'],['W','·--'],['X','-··-'],['Y','-·--'],['Z','--··']]
#Entrada
#Solicita ingreso de mensaje 
mensaje= input('Ingrese mensaje:')
#Crea una nueva variable donde todo el mensaje pasa a mayúscula 
lista_mensaje = list(mensaje.upper())
#Se crea un string para agregar código 
mensaje_morse=[]
i =0
#mientras el iterador sea menor al largo del mensaje a cifrar 
while i< len(lista_mensaje):
    #recorre el mensaje para agregar "/" para separar las letras de las palabras, además agrega "\" para separar las palabras  
    if lista_mensaje[i] != ' ' and i !=0 and lista_mensaje[i-1] != (' '):
        mensaje_morse.append('/')
    if lista_mensaje[i] == ' ':
        mensaje_morse.append("\\")
    else:
        j = 0
     #mientras el iterador sea menor al largo de lo que contiene "morse"  
    while j < len(morse):
            #se agrega a la lista de mensaje_morse cifrado
            if lista_mensaje[i] == morse[j][0]:
                print('prin',morse[j][0])
                letra = morse[j][1]
                mensaje_morse.append(letra)
             #el iterador se incrementa en 1    
           j = j+1
    #el iterador se incrementa en 1       
    i = i+1
#Salida
#imprime el mensaje en morse     
print(str(mensaje_morse))

