# 10. Escribí un programa que lea una cadena y devuelva un diccionario con la cantidad 
#de apariciones de cada carácter en la cadena (considerar que las mayúsculas difieren de las minúsculas, por lo que,
# si el string es "Agua", el carácter "A" tiene 1 aparición y el carácter "a" también tiene 1).


contadores ={}
cadena= input("Ingrese palabra: ")

for caracter in cadena:
    if caracter in contadores:
        contadores[caracter]+=1
    else:
        contadores[caracter]=1

for valor in contadores.keys():
    print(valor,contadores[valor])

