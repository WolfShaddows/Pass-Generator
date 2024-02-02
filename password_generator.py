import random
import string

def generate_password(length, uppercase=True, lowercase=True, numbers=True, specials=True):
    # Inicializa una cadena vacía para contener los caracteres de la contraseña
    characters = ""
    
    # Añade los conjuntos de caracteres según las opciones del usuario
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if specials:
        characters += string.punctuation

    # Verifica si se ha seleccionado al menos un tipo de caracteres
    if not characters:
        print("Error: Debes seleccionar al menos un tipo de caracteres.")
        return None

    # Genera la contraseña seleccionando caracteres aleatorios del conjunto
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password_to_file(name, password):
    # Abre el archivo "passwords.txt" en modo de anexar y escribe la contraseña junto con el nombre
    with open("passwords.txt", "a") as file:
        file.write(f"{name}: {password}\n")

def main():
    # Solicita información al usuario para generar la contraseña
    name = input("Ingrese un nombre o identificación para la contraseña: ")
    length = int(input("Ingrese la longitud de la contraseña: "))
    uppercase = input("¿Incluir mayúsculas? (si/no): ").lower() == 'si'
    lowercase = input("¿Incluir minúsculas? (si/no): ").lower() == 'si'
    numbers = input("¿Incluir números? (si/no): ").lower() == 'si'
    specials = input("¿Incluir caracteres especiales? (si/no): ").lower() == 'si'

    # Genera la contraseña y la guarda en el archivo
    password = generate_password(length, uppercase, lowercase, numbers, specials)
    if password:
        print(f"Contraseña generada: {password}")
        save_password_to_file(name, password)
        print("Contraseña guardada en el archivo passwords.txt")

if __name__ == "__main__":
    # Si el script se ejecuta directamente, llama a la función principal
    main()

        print("Contraseña guardada en el archivo passwords.txt")

if __name__ == "__main__":
    main()
