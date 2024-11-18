class Contact:
    def __init__(self, surname="", name="", age=0, mob_phone="", email=""):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self):
        return f"Contact Info: {self.surname} {self.name}, Age: {self.age}, Phone: {self.mob_phone}, Email: {self.email}"

    def sent_message(self, message: str):
        return f"Message sent to {self.name} at {self.mob_phone}: {message}"


class UpdateContact(Contact):
    def __init__(self, surname="", name="", age=0, mob_phone="", email="", job=""):
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def get_message(self):
        return f"{self.name} works as {self.job}."


contact1 = Contact("Ivanov", "Ivan", 30, "123-456-789", "ivanov@example.com")
contact2 = UpdateContact("Petrov", "Petr", 28, "987-654-321", "petrov@example.com", "Engineer")
update_contact1 = UpdateContact("Sidorov", "Sergii", 35, "555-111-222", "sidorov@example.com", "Developer")
update_contact2 = UpdateContact("Kovalenko", "Olga", 32, "555-333-444", "kovalenko@example.com", "Manager")

# print(contact1.get_contact())
# print(contact2.get_contact())
# print(contact2.get_message())
# print(contact1.__dict__)
# print(contact2.__dict__)
# print(Contact.__base__)
# print(UpdateContact.__base__)
# print(Contact.__bases__)
# print(UpdateContact.__bases__)

# Task 3

# print(hasattr(contact1, "surname"))
# print(hasattr(contact2, "surname"))
# print(hasattr(contact2, "job"))
# print(getattr(contact1, "mob_phone"))
# print(getattr(contact2, "mob_phone"))
# print(getattr(contact1, "age"))
# setattr(contact1, "age", 45)
# setattr(contact2, "mob_phone", "555-000-111")
# print(contact1.get_contact())
# print(contact2.get_contact())
# delattr(contact1, "email")
# delattr(contact2, "job")
# print(hasattr(contact1, "email"))
# print(hasattr(contact2, "job"))

# Task 4

# print(isinstance(contact1, Contact))
# print(isinstance(contact2, UpdateContact))
# print(isinstance(update_contact1, UpdateContact))
# print(isinstance(update_contact2, Contact))
# print(issubclass(UpdateContact, Contact))
# print(issubclass(Contact, UpdateContact))

# Task 5

# delattr(contact2, "job")
# delattr(update_contact1, "job")
# delattr(update_contact2, "job")
#
# print("\nAfter deletion:")
# print(contact1.__dict__)
# print(contact2.__dict__)
# print(update_contact1.__dict__)
# print(update_contact2.__dict__)

# Task 6

# print("Methods in Contact class:")
# print([method for method in dir(Contact) if callable(getattr(Contact, method))])
#
# print("\nMethods in UpdateContact class:")
# print([method for method in dir(UpdateContact) if callable(getattr(UpdateContact, method))])