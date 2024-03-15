#15/03/24
#funcion id
num=40
print(id(num))
num=22
print(id(num))

num=2
def multiplicacion (x):
    num=3
    return x*num
print (multiplicacion (8))

def mutables(lista):
    lista[2]=35

mis_numeros=[1,2,3]
print('antes de invocar a la funcion')
print (mis_numeros)
mutables(mis_numeros)
print ('despues de llamar a la funcion mutables')
print (mis_numeros)
