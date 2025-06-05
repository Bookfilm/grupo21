import re

class Usuario:
    def __init__(self, nombre, contraseña, rol):
        self.nombre = nombre
        self.contraseña = contraseña
        self.rol = rol

    def verificar_contraseña(self, contraseña):
        return self.contraseña == contraseña

class Menu:
    def __init__(self, sistema):
        self.sistema = sistema

    def mostrar_menu_principal(self):
        while True:
            print("\nMenú Principal")
            print("1. Registrar Usuario")
            print("2. Iniciar Sesión")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                self.sistema.registrar_usuario()
            elif opcion == '2':
                nombre_usuario, rol_usuario = self.sistema.iniciar_sesion()
                if nombre_usuario:
                    if rol_usuario == 1:
                        self.mostrar_menu_administrador()
                    elif rol_usuario == 2:
                        self.mostrar_menu_usuario(nombre_usuario)
            elif opcion == '3':
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

    def mostrar_menu_administrador(self):
        while True:
            print("\nMenú Administrador")
            print("1. Ver lista de usuarios")
            print("2. Cambiar rol de un usuario")
            print("3. Eliminar usuario")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                self.sistema.ver_lista_usuarios()
            elif opcion == '2':
                self.sistema.cambiar_rol_usuario()
            elif opcion == '3':
                self.sistema.eliminar_usuario()
            elif opcion == '4':
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

    def mostrar_menu_usuario(self, nombre_usuario):
        while True:
            print("\nMenú Usuario Estándar")
            print("1. Ver mis datos")
            print("2. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                self.sistema.ver_datos_usuario(nombre_usuario)
            elif opcion == '2':
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

class Sistema:
    def __init__(self): # Base de datos de usuarios (solo para fines de demostración)
        self.usuarios = {
            'admin': Usuario('admin', 'admin123', 1),
            'user1': Usuario('user1', 'user123', 2)
        }

    def obtener_rol(self):
        while True:
            rol_input = input("Ingrese el rol (1 para administrador, 2 para usuario): ")
            if rol_input not in ['1', '2']:
                print("Rol inválido. Por favor, ingrese 1 para administrador o 2 para usuario.")
                continue
            rol = int(rol_input)
            if rol == 1:
                contraseña_admin = input("Ingrese la contraseña de administrador: ")
                if contraseña_admin != '123':
                    print("Contraseña de administrador incorrecta. No se puede registrar como administrador.")
                    continue
            return rol

    def registrar_usuario(self):
        while True:
            nombre = input("Ingrese el nombre de usuario: ")
            if nombre in self.usuarios:
                print("El usuario ya existe. Por favor, elija otro nombre de usuario.")
                continue
            break
        while True:
            contraseña = input("Ingrese la contraseña (mínimo 6 caracteres, debe contener letras y números): ")
            contraseña2 = input("Ingrese su contraseña otra vez para verificar: ")
            if contraseña == contraseña2:
                if len(contraseña) < 6:
                    print("La contraseña debe tener al menos 6 caracteres.")
                    continue
                if not re.search(r'[a-zA-Z]', contraseña):
                    print("La contraseña debe contener al menos una letra.")
                    continue
                if not re.search(r'[0-9]', contraseña):
                    print("La contraseña debe contener al menos un número.")
                    continue
            else:
                print("Su contraseña no es igual")
                continue
            break
        rol = self.obtener_rol()
        self.usuarios[nombre] = Usuario(nombre, contraseña, rol)
        print("Usuario registrado con éxito.")

    def iniciar_sesion(self):
        while True:
            nombre = input("Ingrese el nombre de usuario: ")
            contraseña = input("Ingrese la contraseña: ")
            if nombre in self.usuarios and self.usuarios[nombre].verificar_contraseña(contraseña):
                print("inicio de sesion exitoso")
                return nombre, self.usuarios[nombre].rol
            else:
                print("Credenciales incorrectas. Por favor, inténtelo de nuevo.")
                continue

    def ver_lista_usuarios(self):
        print("\nLista de Usuarios:")
        for usuario, datos in self.usuarios.items():
            rol = "administrador" if datos.rol == 1 else "usuario"
            print(f"Usuario: {usuario}, Rol: {rol}")

    def cambiar_rol_usuario(self):
        nombre = input("Ingrese el nombre de usuario: ")
        if nombre not in self.usuarios:
            print("Usuario no encontrado.")
            return
        nuevo_rol = self.obtener_rol()
        self.usuarios[nombre].rol = nuevo_rol
        print("Rol actualizado con éxito.")

    def eliminar_usuario(self):
        nombre = input("Ingrese el nombre de usuario a eliminar: ")
        if nombre not in self.usuarios:
            print("Usuario no encontrado.")
            return
        del self.usuarios[nombre]
        print("Usuario eliminado con éxito.")

    def ver_datos_usuario(self, nombre_usuario):
        print("\nMis Datos:")
        print(f"Nombre de Usuario: {nombre_usuario}")
        rol = "administrador" if self.usuarios[nombre_usuario].rol == 1 else "usuario"
        print(f"Rol: {rol}")


if __name__ == "__main__":
    sistema = Sistema()
    menu = Menu(sistema)
    menu.mostrar_menu_principal()