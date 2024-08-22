import csv
import json

class GestorArchivos:
    def __init__(self, archivo_csv, archivo_json):
        self.archivo_csv = archivo_csv
        self.archivo_json = archivo_json
        
    def simular_base_de_datos(self):
        datos = self.leer_csv()
        base_de_datos_simulada = []
        for fila in datos[1:]:  # Omitimos la primera fila porque es el encabezado
            registro = {
                "nombre": fila[0],
                "edad": int(fila[1]),
                "ciudad": fila[2]
            }
            base_de_datos_simulada.append(registro)
        
        return base_de_datos_simulada

    def validar_datos(self, fila):
        # Asumiendo que la primera fila es el encabezado
        if fila == ['nombre', 'edad', 'ciudad']:
            return True
        
        nombre, edad, ciudad = fila
        
        # Validación de nombre
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError(f"Nombre inválido: '{nombre}' debe ser un texto no vacío.")
        
        # Validación de edad
        try:
            edad = int(edad)  # Convertir edad a entero
            if edad <= 0:
                raise ValueError(f"Edad inválida: '{edad}' debe ser un número positivo.")
        except ValueError:
            raise ValueError(f"Edad inválida: '{edad}' no es un número entero válido.")
        
        # Validación de ciudad
        if not isinstance(ciudad, str) or not ciudad.strip():
            raise ValueError(f"Ciudad inválida: '{ciudad}' debe ser un texto no vacío.")
        
        return True

    def escribir_csv(self):
        try:
            with open(self.archivo_csv, mode='w', newline='') as archivo:
                escritor = csv.writer(archivo)
                filas = [
                    ['nombre', 'edad', 'ciudad'],
                    ['Alfredo', 30, 'Cordoba'],
                    ['Marcos', 20, 'Mendoza'],
                    ['Alvaro', 31, 'Misiones'],
                    ['German', 25, 'Jujuy'],
                    ['Maria', 24, 'Entre Rios'],
                    ['Jimena', 20, 'Rio Gallegos'],
                    ['Sofia', 35, 'Buenos Aires'],
                    ['Alejandra', 19, 'Tucuman'],
                    ['Celestina', 35, 'La Pampa'],
                    ['Oscar', 24, 'Neuquen']
                ]
                for fila in filas:
                    self.validar_datos(fila)  # Validar cada fila antes de escribir
                    escritor.writerow(fila)
        except ValueError as e:
            print(f"Error de validación: {e}")
        except IOError as e:
            print(f"Error al escribir el archivo {self.archivo_csv}: {e}")

    def leer_csv(self):
        datos = []
        try:
            with open(self.archivo_csv, mode='r') as archivo:
                lector = csv.reader(archivo)
                for fila in lector:
                    try:
                        self.validar_datos(fila)
                        datos.append(fila)  # Agregar fila válida a la lista de datos
                    except ValueError as e:
                        print(f"Error en la fila: {fila}. Detalle: {e}")
            return datos
        except FileNotFoundError:
            print(f"El archivo {self.archivo_csv} no existe.")
        except IOError as e:
            print(f"Error al leer el archivo {self.archivo_csv}: {e}.")
            return None  # Retorna None si hay un error en la lectura

    def convertir_csv_a_json(self, datos_csv):
        try:
            with open(self.archivo_json, mode='w') as archivo:
                json.dump(datos_csv, archivo, indent=4)
        except IOError as e:
            print(f"Error al convertir a JSON y escribir el archivo {self.archivo_json}: {e}")

# Uso de la clase
gestor = GestorArchivos('archivo.csv', 'usuarios.json')
base_de_datos = gestor.simular_base_de_datos()
gestor.escribir_csv()
datos_csv = gestor.leer_csv()
print(base_de_datos)
print(datos_csv)
gestor.convertir_csv_a_json(datos_csv)
