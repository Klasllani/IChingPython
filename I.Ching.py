import allFunctions

print ("EL ORÁCULO DEL I CHING - DESCUBRE LO QUE EL FUTURO TE DEPARA\n\t ----------------------------------------")
print ("Escoje una opción para empezar:\n\ta) EXPLICACIÓN: ¿Que es el I Ching? Su historia.\n\tb) ORÁCULO: Ver lo que me depara el futuro.")
opción = str(input(">>>"))

while opción != "a" and opción != "b":
    print("ERROR: La opción escogida no es válida.")
    print ("Escoje una opción para empezar:\n\ta) EXPLICACIÓN: ¿Que es el I Ching? Su historia.\n\tb) ORÁCULO: Ver lo que me depara el futuro.")
    opción = str(input(">>>"))

if opción == "a":
    print("El oráculo del I Ching, también conocido como el Libro de los Cambios, es un texto clásico chino utilizado para la adivinación y la orientación espiritual.\nConsiste en un sistema de 64 hexagramas, cada uno formado por combinaciones de seis líneas (continuas o partidas) que representan diferentes estados de cambio\ny dinámica en la vida. Se consulta lanzando monedas o varillas para construir un hexagrama, el cual se interpreta a través del libro, ofreciendo sabiduría sobre\ncómo enfrentar una situación o tomar decisiones. El I Ching enfatiza la armonía con las leyes del cambio natural y la adaptabilidad.\nMás que predecir el futuro, guía en el presente con enseñanzas filosóficas y éticas.")
    opción = str(input("ORÁCULO: Para ver lo que te depara el futuro pulsa b:"))

if opción == "b":
    print("PROCEDEMOS A LEER TU ORÁCULO...")
    tiradas = [0,0,0,0,0,0]
    for i in range (len(tiradas)):
        tiradas[i] = allFunctions.clasificarTirada(allFunctions.sumarResultados(allFunctions.throwThreeCoins()))
    print (tiradas)
    print ("El hexagrama que ha sacado el oráculo ha de escribirse de atrás hacia adelante:")
    for element in reversed(tiradas):
        if element == "partida":
            print("****************")
        if element == "continua":
            print("******    ******")

f = open("hexagramas.txt", "r")

lineas = f.readlines()

for linea in lineas:
    partes = linea.split(" - ")
    for i in range (0, partes.len(), 1):
        if partes[i] == tiradas:
            print (partes[i+1])


