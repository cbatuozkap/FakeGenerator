import customtkinter
from CTkMessagebox import CTkMessagebox
from faker import Faker

root = customtkinter.CTk()
root.geometry("600x650")

title_label = customtkinter.CTkLabel(root, text="Fake Generator", text_color="SteelBlue3",fg_color="transparent", font=('Bahnschrift', 40 ))
title_label.place(x=180,y=40)

combobox_var = customtkinter.StringVar(value="Fake Options")
fake_combobox = customtkinter.CTkComboBox(root, values=["Name", "Address", "Phone Number", "License Plate", "Job", "Person"], variable=combobox_var)
combobox_var.set("Fake Options")
fake_combobox.place(x=220, y=160)

combobox_var2 = customtkinter.StringVar(value="Languages")
lang_combobox = customtkinter.CTkComboBox(root, values=["English", "Turkish", "German", "Japanese", "All Languages"], variable=combobox_var2)
combobox_var2.set("Languages")
lang_combobox.place(x=220, y=200)

entry = customtkinter.CTkEntry(root, placeholder_text="How many to generate?", width=150)
entry.place(x=220, y=250)

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
                License Plate: {self.licenseplate}\nPlace of Birth:{self.placeofbirth}\n\n"""

def generate_button():
    try:
        output_list = []
        language = 'en_US'
        if combobox_var2.get() == "Turkish":
            language = 'tr_TR'
        elif combobox_var2.get() == "Japanese":
            language = 'jp_JP'
        elif combobox_var2.get() == "German":
            language = 'de_DE'
        elif combobox_var2.get() == "All Languages":
            language = ['en_US', 'ja_JP', 'tr_TR', 'de_DE']
        fake = Faker(language)
        if combobox_var.get() == "Name":
            for _ in range(int(entry.get())):
                output_list.append(fake.name())
            print(output_list)
        elif combobox_var.get() == "Address":
            for _ in range(int(entry.get())):
                output_list.append(fake.address())
            print(output_list)
        elif combobox_var.get() == "Phone Number":
            for _ in range(int(entry.get())):
                output_list.append(fake.phone_number())
            print(output_list)
        elif combobox_var.get() == "License Plate":
            for _ in range(int(entry.get())):
                output_list.append(fake.license_plate())
            print(output_list)
        elif combobox_var.get() == "Job":
            for _ in range(int(entry.get())):
                output_list.append(fake.job())
            print(output_list)
        elif combobox_var.get() == "Person":
            for _ in range(int(entry.get())):
                person = Person()
                person.set_language(language)
                output_list.append(person)
            print(output_list)

        output_window = customtkinter.CTk()
        output_window.geometry("400x450")
        title2_label = customtkinter.CTkLabel(output_window, text="Fake Generator", text_color="medium purple",fg_color="transparent", font=('Bahnschrift', 30 ))
        title2_label.place(x=100,y=30)
        FONT = ('Bahnschrift ', 20, 'bold')
        label10 = customtkinter.CTkLabel(output_window, text="Your fake data :",text_color="medium purple", font=FONT)
        label10.place(x=50, y=100)
        text10 = customtkinter.CTkTextbox(output_window, width=250, height=250)
        text10.place(x=50, y=150)
        if combobox_var.get() != "Person":
            output_list2 = "\n".join(output_list)
            text10.insert("0.0", f"{output_list2}")
        else:
            text10.insert("0.0", f"{output_list}")
        text10.configure(state="disabled")

        output_window.mainloop()
    except:
        CTkMessagebox(title="Error", message="""Something went wrong!
        \n• You may have entered text in the input box. 
        \n• You may not have chosen fake option and language.""", icon="cancel")

generator_button = customtkinter.CTkButton(root, text="Generate!", command=generate_button, font= ('Bahnschrift ', 15,))
generator_button.place(x=220, y=350)

root.mainloop()