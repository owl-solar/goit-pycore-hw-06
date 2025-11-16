from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        self.value = value

class Phone(Field):
    """Class for phone number in record"""
    def __init__(self, value):
        if not isinstance(value, str):
            raise TypeError("Phone must be in a string format")
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone must be 10 digit string format")

        self.value = value

class Record:

    def __init__(self, name):
        self.name = Name(name)      
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone_number):
     
     self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
       
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return

    def edit_phone(self, old_phone, new_phone):
      
        old_exists = any(phone.value == old_phone for phone in self.phones)
        if not old_exists:
            raise ValueError(f"Phone {old_phone} not found.")
    
        new_phone_obj = Phone(new_phone)
        
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone_obj.value
                return

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None  

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
