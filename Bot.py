contacts = {}  # Словник для зберігання контактів

# Декоратор для обробки помилок введення користувача
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command format"

    return wrapper

# Додавання нового контакту
@input_error
def add_contact(command):
    _, name, phone = command.split()
    contacts[name] = phone
    return f"Added contact: {name}, {phone}"

# Зміна номеру телефону існуючого контакту
@input_error
def change_phone(command):
    _, name, phone = command.split()
    if name in contacts:
        contacts[name] = phone
        return f"Changed phone for {name} to {phone}"
    else:
        return f"Contact {name} not found"

# Виведення номеру телефону для зазначеного контакту
@input_error
def get_phone(command):
    _, name = command.split()
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        return f"Contact {name} not found"

# Виведення всіх збережених контактів
@input_error
def show_all_contacts(_):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found"

# Головна функція для обробки команд користувача
def main():
    print("How can I help you?")
    
    while True:
        command = input().strip().lower()
        
        if command == "good bye" or command == "close" or command == "exit":
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            result = add_contact(command)
            print(result)
        elif command.startswith("change"):
            result = change_phone(command)
            print(result)
        elif command.startswith("phone"):
            result = get_phone(command)
            print(result)
        elif command == "show all":
            result = show_all_contacts(command)
            print(result)
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()
