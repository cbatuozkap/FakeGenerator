from faker import Faker

def after_error():
    print("WARNING :  YOU MUST ENTER A NUMERIC VALUE WITHIN THE SPECIFIED RANGE! ")
    after_error = input(" 'r' to restart , 'q' to  quit : \n ")
    return after_error

class Person:
    def __init__(self):
        self.fake = Faker()
        self.name = self.fake.name()
        self.address = self.fake.address()
        self.age = self.fake.random_int(min=18, max=72)
        self.job = self.fake.job()
        self.licensepalte = self.fake.license_plate()
        self.placeofbirth = self.fake.country()

    def set_language(self, language):
        self.fake = Faker(language)
        self.name = self.fake.name()
        self.address = self.fake.address()
        self.age = self.fake.random_int(min=18, max=72)
        self.job = self.fake.job()
        self.licensepalte = self.fake.license_plate()
        self.placeofbirth = self.fake.country()

    def __repr__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nAge: {self.age}\nJob: {self.job}\nLicense Plate: {self.licensepalte}\nPlace of Birth:{self.placeofbirth}\n\n"


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
    if not 1<=var1<=6:
        print("You must select one of these [1,2,3,4,5,6]")
        continue
    try:
        var2 = int(input("How many do you want to create?\n"))
    except:
        after_error = after_error()
        if after_error.lower() == "r":
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

    except:
        after_error = after_error()
        if after_error.lower() == 'r':
            continue
        else:
            break
    name_list = []
    address_list = []
    phonenum_list = []
    license_plate_list = []
    job_list = []
    person_list = []

    if not 1<=var3<=5:
        print("You have to select one of these [1,2,3,4,5]")
        continue

    if var3 == 1:
        if var1==1:
            fake_name = Faker()
            for _ in range(var2):
                name_list.append(fake_name.name())
            print(name_list)
        elif var1==2:
            fake_address = Faker()
            for _ in range(var2):
                address_list.append(fake_address.address())
            print(address_list)
        elif var1==3:
            fake_phonenum = Faker()
            for _ in range(var2):
                phonenum_list.append(fake_phonenum.phone_number())
            print(phonenum_list)
        elif var1==4:
            fake_plate = Faker()
            for _ in range(var2):
                license_plate_list.append(fake_plate.license_plate())
            print(license_plate_list)
        elif var1==5:
            fake_job = Faker()
            for _ in range(var2):
                job_list.append(fake_job.job())
            print(job_list)
        elif var1 == 6:
            fake = Faker()
            for _ in range(var2):
                person = Person()
                person_list.append(person)
            print(person_list)
        else:
            print("You have to select one of these [1,2,3,4]")
            continue

    elif var3 == 2:
        if var1==1:
            fake_name = Faker('tr_TR')
            for _ in range(var2):
                name_list.append(fake_name.name())
            print(name_list)
        elif var1==2:
            fake_address = Faker('tr_TR')
            for _ in range(var2):
                address_list.append(fake_address.address())
            print(address_list)
        elif var1==3:
            fake_phonenum = Faker('tr_TR')
            for _ in range(var2):
                phonenum_list.append(fake_phonenum.phone_number())
            print(phonenum_list)
        elif var1==4:
            fake_plate = Faker('tr_TR')
            for _ in range(var2):
                license_plate_list.append(fake_plate.license_plate())
            print(license_plate_list)
        elif var1==5:
            fake_job = Faker('tr_TR')
            for _ in range(var2):
                job_list.append(fake_job.job())
            print(job_list)
        elif var1 == 6:
            person = Person()
            person.set_language('tr_TR')
            for _ in range(var2):
                person_list.append(person)
            print(person_list)
        else:
            print("You have to select one of these [1,2,3,4]")
            continue

    elif var3 == 3:
        if var1==1:
            fake_name = Faker('jp_JP')
            for _ in range(var2):
                name_list.append(fake_name.name())
            print(name_list)
        elif var1==2:
            fake_address = Faker('jp_JP')
            for _ in range(var2):
                address_list.append(fake_address.address())
            print(address_list)
        elif var1==3:
            fake_phonenum = Faker('jp_JP')
            for _ in range(var2):
                phonenum_list.append(fake_phonenum.phone_number())
            print(phonenum_list)
        elif var1==4:
            fake_plate = Faker('jp_JP')
            for _ in range(var2):
                license_plate_list.append(fake_plate.license_plate())
            print(license_plate_list)
        elif var1==5:
            fake_job = Faker('jp_JP')
            for _ in range(var2):
                job_list.append(fake_job.job())
            print(job_list)
        elif var1 == 6:
            person = Person()
            person.set_language('jp_JP')
            for _ in range(var2):
                person_list.append(person)
            print(person_list)
        else:
            print("You have to select one of these [1,2,3,4")

    elif var3 == 4:
        if var1==1:
            fake_name = Faker('de_DE')
            for _ in range(var2):
                name_list.append(fake_name.name())
            print(name_list)
        elif var1==2:
            fake_address = Faker('de_DE')
            for _ in range(var2):
                address_list.append(fake_address.address())
            print(address_list)
        elif var1==3:
            fake_phonenum = Faker('de_DE')
            for _ in range(var2):
                phonenum_list.append(fake_phonenum.phone_number())
            print(phonenum_list)
        elif var1==4:
            fake_plate = Faker('de_DE')
            for _ in range(var2):
                license_plate_list.append(fake_plate.license_plate())
            print(license_plate_list)

        elif var1==5:
            fake_job = Faker('de_DE')
            for _ in range(var2):
                job_list.append(fake_job.job())
            print(job_list)
        elif var1 == 6:
            person = Person()
            person.set_language('jp_JP')
            for _ in range(var2):
                person_list.append(person)
            print(person_list)
        else:
            print("You have to select one of these [1,2,3,4")
            continue

    elif var3 == 5:
        if var1==1:
            fake_name = Faker(['en_US', 'ja_JP', 'tr_TR','de_DE'])
            for _ in range(var2):
                name_list.append(fake_name.name())
            print(name_list)
        elif var1==2:
            fake_address = Faker(['en_US', 'ja_JP', 'tr_TR','de_DE'])
            for _ in range(var2):
                address_list.append(fake_address.address())
            print(address_list)
        elif var1==3:
            fake_phonenum = Faker(['en_US', 'ja_JP', 'tr_TR','de_DE'])
            for _ in range(var2):
                phonenum_list.append(fake_phonenum.phone_number())
            print(phonenum_list)
        elif var1==4:
            fake_plate = Faker(['en_US', 'ja_JP', 'tr_TR','de_DE'])
            for _ in range(var2):
                license_plate_list.append(fake_plate.license_plate())
            print(license_plate_list)
        elif var1==5:
            fake_job = Faker(['en_US', 'ja_JP', 'tr_TR','de_DE'])
            for _ in range(var2):
                job_list.append(fake_job.job())
            print(job_list)
        elif var1 == 6:
            person = Person()
            person.set_language('en_US', 'ja_JP', 'tr_TR','de_DE')
            for _ in range(var2):
                person_list.append(person)
            print(person_list)
        else:
            print("You have to select one of these [1,2,3,4")
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