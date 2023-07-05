from faker import Faker

language = 'tr_TR'
while True:
    lang = int(input("""
    [1] TR
    [2] EN
    [3] DE
    :"""))

    if lang == 1:
        language = 'tr_TR'
    elif lang == 2:
        language = 'en_US'
    elif lang == 3:
        language = 'de_DE'
    else:
        continue

    fake = Faker(language)

    name_list = []
    for _ in range(3):
        name_list.append(fake.name())
    print(name_list)

    job_list = []
    for _ in range(3):
        job_list.append(fake.job())
    print(job_list)

    rq = input("\n 'r' to restart, 'q' to quit : ")
    if rq.lower() == "r":
        continue
    else:
        break
