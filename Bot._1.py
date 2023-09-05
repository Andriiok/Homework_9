contacts = {}  # Словник для зберігання контактів

# Додавання нового контакту
def add_contact(name, phone):
    contacts[name] = phone
    return f"Added contact: {name}, {phone}"

# Зміна номеру телефону існуючого контакту
def change_phone(name, phone):
    if name in contacts:
        contacts[name] = phone
        return f"Changed phone for {name} to {phone}"
    else:
        return f"Contact {name} not found"

# Виведення номеру телефону для зазначеного контакту
def get_phone(name):
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        return f"Contact {name} not found"

# Виведення всіх збережених контактів
def show_all_contacts():
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found"

# Головна функція для обробки команд користувача
def main():
    commands = {
        "hello": lambda: "How can I help you?",
        "add": add_contact,
        "change": change_phone,
        "phone": get_phone,
        "show all": show_all_contacts,
    }

    print("How can I help you?")

    while True:
        command = input().strip().lower()
        
        if command in {"good bye", "close", "exit"}:
            print("Good bye!")
            break
        elif command in commands:
            if command == "hello":
                print(commands[command]())
            else:
                try:
                    name, *args = input("Enter name and phone: ").split()
                    result = commands[command](name, *args)
                    print(result)
                except ValueError:
                    print("Invalid command format")
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()

