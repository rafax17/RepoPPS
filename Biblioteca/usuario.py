from excepciones import WrongPasswordException

class Usuario:
    def __init__(self, nombre, apellidos, nombre_usuario, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.nombre_usuario = nombre_usuario
        self.password = password
    
    def login(self, password):
        if self.password == password:
            return True
        else:
            raise WrongPasswordException("")
    

user = Usuario("Rafa", "Sanchez", "rafa1", "rafa123")

lista_usuarios = []
lista_usuarios.append(user)

usr = input("Nombre de usuario: \n")
pas = input("Contraseña: \n")

for usuario_actual in lista_usuarios:
    if usuario_actual.nombre_usuario == usr:
        try:
            if usuario_actual.login(pas):
                print("Usuario logueado con éxito")
        except WrongPasswordException:
                print("La contraseña introducida no es correcta")

        