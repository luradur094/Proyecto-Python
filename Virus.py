import random #Importa una libreria para crear texto aleatorio
import time#Importa una libreria que os servira para darnos la fecha y hora
Fecha = time.strftime('%d/%m/%Y') #Creo la variable fecha donde estara guardada la fecha del sistema
Hora = time.strftime('%H:%M:%S') #Creo la variable hora donde estara guardada la hora del sistema
variante_nueva="ccucggcgggca" #Creo una variable con el codigo del virus
numero=32000000 #Creo una variable numerica para la longitud edl ADN 
division=["c","u","g","a"] #Creo una variable que contiene los componentes del virus
ndividido=len(division) #Creo una variable que almacena el numero de letras de la variable
codigo_paciente=input("Introduzca codigo del paciente: ") #Pregunto el codigo del paciente
automatico=[] #Iniciamos una tarea
for i in range(0, numero, 1):
    numero_aleatorio= random.randint(0, ndividido - 1) #Genera una cadena aleatorio
    automatico.append(division[numero_aleatorio]) #Se añade a la cadena de adn
generacion="".join(automatico)
respuesta=""
if variante_nueva in generacion: #Comprobara si el paciente es positivo o negativo buscando el codigo del virus en la cadena generada antes
    respuesta="Positivo: Sí se encuentra restos de la variante COVID."
    resultado="Positivo"
else:
    respuesta="Negativo: No se encuentra restos de la variante COVID."
    resultado="Negativo"

print("Informe de virus COVID:")
print("Fecha:",Fecha) #Mostrara la fecha del sistema
print("Hora:",Hora) #Mostrara la hora del sistema
print("Código del paciente:",codigo_paciente) #Mostrara el codigo del paciente
print("Resultado: ",respuesta) #Mostrara el resultado de la comprobacion

tupla=(Fecha,Hora,codigo_paciente,resultado) #Creara una tupla donde guarda el codigo del paciente la fecha y hora y si dio positivo o negativo
print(tupla)# Muestra la tupla generada