import time #Importa una libreria que os servira para darnos la fecha y hora
Fecha = time.strftime('%d/%m/%Y') #Creo la variable fecha donde estara guardada la fecha del sistema
Hora = time.strftime('%H:%M:%S') #Creo la variable hora donde estara guardada la hora del sistema
import os #Importa la libreria os donde podremos poner los comandos del sistema 
grado = [] #Iniciamos una tarea
while True: 
    temperatura = float(input("Introduzca la temperaturas: "))
    if temperatura == 100:
        break;
    grado.append(temperatura)
    #Este bucle ira recogiendo las temperaturas y guardandola en una lista asta que se pulse 100 que es cuando se para 
os.system ("clear") #este comando importado de la libreria os limpiara la pantalla
print("Informe de temperaturas del Parque Natural de Doñana:")
print("Fecha:",Fecha) #Mostrara la fecha del sistema
print("Hora:",Hora) #Mostrara la hora del sistema 
print("Número de muestras:", len(grado)) #Mostrara el numero total de elementos introducidos
print("Temperaturas tomadas:", grado) #Muestra la lista con las temperaturas recogidas
print("Temperatura máxima:", max(grado)) #Muestra la temperatura mas alta
print("Temperatura mínima:", min(grado)) #Muestra la temperatura mas baja
media = sum(grado) / len(grado) #Realiza la media de todas las temperaturas
print("Temperatura media:", round(media,1)) #Muestra la temperatura redondeada a un decimal
tupla = (Fecha,Hora,grado) #Guarda la fecha, hora y las temperaturas en una tupla
listar = list(tupla) #Convierte la tupla en una lista para que se pueda escribir e un txt
file = open("temperaturas.txt", "a") #Creara o abrira si existe un fichero con el modo append que hace es escribir sin borrar el contenido que tenia
file.write('grado = %s' % listar + '\n') #Escribe la informacion de una tupla y la convierte en cadena
file.close() #Cierra el fichero