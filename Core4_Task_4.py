def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Enter a name and a phone number "
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Enter a name and a phone number "
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} has been changed."
    else:
        return f"Contact {name} not found."

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    all_contacts="\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return f"List of contacts:\n{all_contacts}"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts)) 
        elif command == "all":
            print(show_all(contacts))   
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
