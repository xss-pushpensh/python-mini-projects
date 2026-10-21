import json
from pathlib import Path

FILE = Path(__file__).with_name("contacts.json")


def load_contacts():
    if FILE.exists():
        try:
            data = json.loads(FILE.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                return data
        except (json.JSONDecodeError, OSError):
            print("Could not read contacts.json.")
            raise SystemExit

    return {}


def save_contacts(contacts):
    FILE.write_text(
        json.dumps(contacts, indent=4),
        encoding="utf-8"
    )


contacts = load_contacts()

while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()

        if not name or not phone:
            print("Name and phone number are required.")
        elif name in contacts:
            print("That contact name already exists.")
        else:
            contacts[name] = phone
            save_contacts(contacts)
            print("Contact saved successfully.")

    elif choice == "2":
        if not contacts:
            print("No contacts saved.")
        else:
            for name, phone in contacts.items():
                print(f"{name}: {phone}")

    elif choice == "3":
        name = input("Enter name to search: ").strip()

        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to delete: ").strip()

        if name in contacts:
            del contacts[name]
            save_contacts(contacts)
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")