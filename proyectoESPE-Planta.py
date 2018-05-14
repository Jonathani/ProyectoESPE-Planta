import serial
import time

from pymongo import MongoClient

try:
    conn = MongoClient()
    print("Conexion exitosa")
except:  
    print("No se pudo conectar a MongoDB")

db = conn.Experimento
datos = db.datos
while True:
	calidadDelAireYHumedadTierra = serial.Serial("COM3", 9600)
	subCalidadDelAireYHumedadTierra = calidadDelAireYHumedadTierra.readline().decode("utf-8").split(";")
	temperaturaHumedadIndiceCalorYHumedad = serial.Serial("COM4", 9600)
	subTemperaturaHumedadIndiceCalorYHumedad = temperaturaHumedadIndiceCalorYHumedad.readline().decode("utf-8").split(";")
	archivo=open("arduinoAux.txt" , "a")
	archivo.write(time.strftime("%d/%m/%y"))
	archivo.write("\n")
	archivo.write(time.strftime("%H:%M:%S"))
	archivo.write("\n")
	archivo.write(subCalidadDelAireYHumedadTierra[0])
	archivo.write("\n")
	archivo.write(subCalidadDelAireYHumedadTierra[1])
	archivo.write("\n")
	archivo.write(subTemperaturaHumedadIndiceCalorYHumedad[0])
	archivo.write("\n")
	archivo.write(subTemperaturaHumedadIndiceCalorYHumedad[1])
	archivo.write("\n")
	archivo.write(subTemperaturaHumedadIndiceCalorYHumedad[2])
	archivo.write("\n")
	archivo.write(subTemperaturaHumedadIndiceCalorYHumedad[3])
	archivo.write("\n")
	registro = {
        "fecha":time.strftime("%d/%m/%y"),
        "hora":time.strftime("%H:%M:%S"),
        "calidad_aire":subCalidadDelAireYHumedadTierra[0],
	"humedad_tierra1":subCalidadDelAireYHumedadTierra[1],
	"humedad_tierra2":subTemperaturaHumedadIndiceCalorYHumedad[3],
	"humedad_ambiente":subTemperaturaHumedadIndiceCalorYHumedad[0],
	"temperatura_ambiente":subTemperaturaHumedadIndiceCalorYHumedad[1],
	"indice_calor_ambiente":subTemperaturaHumedadIndiceCalorYHumedad[2]
	}
	registros = datos.insert_one(registro)
