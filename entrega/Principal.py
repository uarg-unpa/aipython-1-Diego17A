print ("taller AIPython")
print ()
print ("hola","soy","diego")
print ("prueba separador""*""prueba end","\n")
print ("es viernes","y el cuerpo lo sabe",sep="+")
print ("modernizacion","2024",end="*")
print ("2024")
print (type (40))

edad=15
print(f'su edad es: {edad}')
num1=14
num2=2

#print
texto='Es un tiTuLo'
print(texto.title())
print(texto)
texto=texto.title()
print(texto)

#upper lower
print(texto.upper())
print(texto.lower())
#replace
print(texto.replace('',':)'))
print(len(texto))
#sentencia if
edad=int(input('Ingese sus edad:'))
if(edad>=18):
    print('ud. debe votar') 
else:
    print('es menor de edad')
print('indepediente')
#ejemplo
calificacion=int(input('ingrese calificacion'))
if calificacion >=90:
    print('excelente')
else:
    if calificacion >=80:
        print('muy bien')
    else:
        if calificacion >=70:
            print ('bien')
        else:
            print('insuficiente')
#sentencia elif
calificacion=int(input('ingrese calificacion'))
if calificacion >=90:
    print('excelente')
elif calificacion >=80:
    print('muy bien')
elif calificacion >=70:
    print('bien')
else:
    print('insufieciente')
    
# match 
#find  str.find(<caracter>) indice desde donde comienza, -1
    
frase=input("ingrese una frase") 
caracter=input("ingrese un caracter")
#buscar la primera aparicion del caracter
posicion=frase.find(caracter)
if posicion !=-1:
    print(f"el caracter{caracter} se encuentra en la posicion {posicion+1}")
    subcadena=frase{posicion:)
    print(f"subcadena a partir de la posision {posicion+1}: {subcadena}")
else:
    print(f"el caracter {caracter} no se encuentra en la frase")
