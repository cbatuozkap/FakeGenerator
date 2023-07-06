from faker import Faker

def after_error():
    print("WARNING:  YOU MUST ENTER A NUMERIC VALUE WITHIN THE SPECIFIED RANGE! ")
    input_error = input(" 'r' to restart , 'q' to  quit : \n ")
    return input_error

class Person:
    def __init__(self):
        self.fake = Faker()
        self.name = self.fake.name()
        self.address = self.fake.address()
        self.age = self.fake.random_int(min=22, max=72)
        self.job = self.fake.job()
        self.licenseplate = self.fake.license_plate()
        self.placeofbirth = self.fake.country()

    def set_language(self, language):
        self.fake = Faker(language)
        self.name = self.fake.name()
        self.address = self.fake.address()
        self.age = self.fake.random_int(min=18, max=72)
        self.job = self.fake.job()
        self.licenseplate = self.fake.license_plate()
        self.placeofbirth = self.fake.country()

    def __repr__(self):
        return f"""Name: {self.name}\nAddress: {self.address}\nAge: {self.age}\nJob: {self.job}
                License Plate: {self.licenseplate}\nPlace of Birth:{self.placeofbirth}"""

print("-"*35)
print("\t\t Fake Generator")
print("-"*35)

while True:
    try:
        var1 = int(input("""        Which one do you want to create?
        [1] Fake Name
        [2] Fake Address
        [3] Fake Phone Number
        [4] Fake License Plate
        [5] Fake Job
        [6] Fake Person
        Your select is :          
            """))
    except:
        print("WARNING : YOU MUST ENTER THE A NUMERIC VALUE!    ")
        continue
    if not 1 <= var1 <= 6:
        print("You must select one of these [1,2,3,4,5,6]")
        continue
    try:
        var2 = int(input("How many do you want to create?\n"))
    except (ValueError, TypeError):
        input_error = after_error()
        if input_error.lower() == "r":
            continue
        else:
            break

    try:
        var3 = int(input("""Which language do you wanna use to create it?
        [1] English
        [2] Turkish
        [3] Japanese
        [4] German
        [5] All Languages (mixed)
        Your select is :\n  """))

    except (ValueError, TypeError):
        input_error = after_error()
        if input_error.lower() == 'r':
            continue
        else:
            break

    if not 1 <= var3 <= 5:
        print("You have to select one of these [1,2,3,4,5]")
        continue

    language = 'en_US'
    if var3 == 2:
        language = 'tr_TR'
    elif var3 == 3:
        language = 'jp_JP'
    elif var3 == 4:
        language = 'de_DE'
    elif var3 == 5:
        language = ['en_US', 'ja_JP', 'tr_TR', 'de_DE']

    output_list = []
    fake = Faker(language)

    if var1 == 1:
        for _ in range(var2):
            output_list.append(fake.name())
        print(output_list)
    elif var1 == 2:
        for _ in range(var2):
            output_list.append(fake.address())
        print(output_list)
    elif var1 == 3:
        for _ in range(var2):
            output_list.append(fake.phone_number())
        print(output_list)
    elif var1 == 4:
        for _ in range(var2):
            output_list.append(fake.license_plate())
        print(output_list)
    elif var1 == 5:
        for _ in range(var2):
            output_list.append(fake.job())
        print(output_list)
    elif var1 == 6:
        person = Person()
        person.set_language(language)
        for _ in range(var2):
            person = Person()
            output_list.append(person)
        print(output_list)
    else:
        continue

    print("""\nDo you want to continue or quit ?
        [c] Press "c" to create a new one.
        [q] Press "q" to quit.\n""")

    cq = input("[ c, q ] : ")
    if cq.lower() == "c":
        continue
    elif cq.lower() == "q":
        break
    else:
        print("You have to choose one of these [c, q]")
        break