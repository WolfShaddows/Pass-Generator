import random
import string

def generate_password(length, uppercase=True, lowercase=True, numbers=True, specials=True):
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if specials:
        characters += string.punctuation

    if not characters:
        print("Error: Debes seleccionar al menos un tipo de caracteres.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password_to_file(name, password):
    with open("passwords.txt", "a") as file:
        file.write(f"{name}: {password}\n")

def main():
    name = input("Ingrese un nombre o identificación para la contraseña: ")
    length = int(input("Ingrese la longitud de la contraseña: "))
    uppercase = input("¿Incluir mayúsculas? (si/no): ").lower() == 'si'
    lowercase = input("¿Incluir minúsculas? (si/no): ").lower() == 'si'
    numbers = input("¿Incluir números? (si/no): ").lower() == 'si'
    specials = input("¿Incluir caracteres especiales? (si/no): ").lower() == 'si'

    password = generate_password(length, uppercase, lowercase, numbers, specials)
    if password:
        print(f"Contraseña generada: {password}")
        save_password_to_file(name, password)
        print("Contraseña guardada en el archivo passwords.txt")

if __name__ == "__main__":
    main()
