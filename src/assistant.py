from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

    def __repr__(self):
        return f"Name: {self.value}"

class Phone(Field):
    @staticmethod
    def process_phone(phone: str):
        if len(phone) == 10 and phone.isdigit():
            return phone
        raise ValueError(f"Phone number {phone} is invalid")

    def __init__(self, phone: str):
        super().__init__(phone)
        self.value = Phone.process_phone(phone)

    def __repr__(self):
        return self.value

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def get_phone_index(self, phone: str):
        return [phone.value for phone in self.phones].index(phone)

    def edit_phone(self, old_phone: str, new_phone: str):
        index = self.get_phone_index(old_phone)
        if index != -1:
            self.phones[index] = Phone(new_phone)
        else:
            raise ValueError(f"Phone number {old_phone} not found")

    def remove_phone(self, phone: str):
        index = self.get_phone_index(phone)
        self.phones.pop(index)

    def find_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __repr__(self):
        return f"Contact name: {self.name.value}, phones: [{', '.join(p.value for p in self.phones)}]"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        if name in self.data:
            return self.data[name]
        return None

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]
            return "Record deleted"
        return "Record not found"

    def __repr__(self):
        return str(self.data)

book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)

# Пошук конкретного телефону в записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
john.remove_phone("1112223333")

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

