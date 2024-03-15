#ejercicio 8
ancho=float(input('ingrese medida correspondiente al ancho: '))
largo=float(input('ingrese medida coorespondiente al largo: '))
radio=float(input('ingrese medida correspondiente al radio: '))
perimetro1=(2*(ancho+largo))
perimetro2=(2*radio*3.1416)
area1=(ancho*largo)
area2=(3.1416*(radio**2))
print('perimetro rectagulo: ',perimetro1)
print('perimetro circunferencia: ',perimetro2)
print(area1)
print(area2)

