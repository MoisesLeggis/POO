
import csv
import os
# LEGGIS GOMEZ MOISES ALEJANDRO CODIGO 218423359
class User:
    def __init__(self, user_id, nombre, correo, edad):
        self.user_id = user_id
        self.nombre = nombre
        self.correo = correo
        self.edad = edad

    def __str__(self):
        return f"{self.user_id} - {self.nombre} - {self.correo} - {self.edad} años"


class UserManager:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv

    def leer_usuarios(self):
        with open(self.archivo_csv, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            usuarios = list(reader)  # Convertimos a lista para verificar si está vacía
            
            if not usuarios:  # Si no hay registros (solo el encabezado)
                print("No hay usuarios registrados")
                return []  # Retornamos lista vacía para consistencia
            
            for row in usuarios:
                print(f"{row['id']} - {row['nombre']} - {row['correo']} - {row['edad']} años")
            return usuarios

    def agregar_usuario(self, user: User):
        with open(self.archivo_csv, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'nombre', 'correo', 'edad'])
            writer.writerow({'id': user.user_id, 'nombre': user.nombre, 'correo': user.correo, 'edad': user.edad})

    def actualizar_usuario(self, id_usuario):
        usuarios = []
        actualizado = False

        with open(self.archivo_csv, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['id'] == str(id_usuario):
                    nombre = input(f"Nuevo nombre (actual: {row['nombre']}): ") or row['nombre']
                    correo = input(f"Nuevo correo (actual: {row['correo']}): ") or row['correo']
                    edad = input(f"Nueva edad (actual: {row['edad']}): ") or row['edad']
                    row = {'id': row['id'], 'nombre': nombre, 'correo': correo, 'edad': edad}
                    actualizado = True
                usuarios.append(row)

        if actualizado:
            with open(self.archivo_csv, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['id', 'nombre', 'correo', 'edad'])
                writer.writeheader()
                writer.writerows(usuarios)
            print("Usuario actualizado con éxito.")
        else:
            print("Usuario no encontrado.")

    def eliminar_usuario(self, id_usuario):
        usuarios = []
        eliminado = False

        with open(self.archivo_csv, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['id'] != str(id_usuario):
                    usuarios.append(row)
                else:
                    eliminado = True

        if eliminado:
            with open(self.archivo_csv, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['id', 'nombre', 'correo', 'edad'])
                writer.writeheader()
                writer.writerows(usuarios)
            print("Usuario eliminado con éxito.")
        else:
            print("Usuario no encontrado.")


# Ejemplo de uso:
# Ejemplo de uso:
if __name__ == "__main__":
    archivo = 'usuarios.csv'
    if not os.path.exists(archivo):
        with open(archivo, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'nombre', 'correo', 'edad'])
            writer.writeheader()
    
    user_manager = UserManager(archivo)
    # Opciones del menú
    while True:
        print("\n--- Sistema CRUD con CSV ---")
        print("1. Ver usuarios")
        print("2. Agregar usuario")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            print("\n--- Usuarios registrados ---")
            user_manager.leer_usuarios()  # El método ahora maneja el mensaje de "vacío"
        elif opcion == '2':
            user_id = input("ID del usuario: ")
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            edad = input("Edad: ")
            user = User(user_id, nombre, correo, edad)
            user_manager.agregar_usuario(user)
        elif opcion == '3':
            id_usuario = input("ID del usuario a actualizar: ")
            user_manager.actualizar_usuario(id_usuario)
        elif opcion == '4':
            id_usuario = input("ID del usuario a eliminar: ")
            user_manager.eliminar_usuario(id_usuario)
        elif opcion == '5':
            break
        else:
            print("Opción no válida, inténtalo de nuevo.")