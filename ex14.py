def generate_password(last_name, first_name, birth_date):
    last_name = last_name.replace(" ", "").lower()
    first_name = first_name.replace(" ", "").upper()

    month = birth_date[3:5]
    year = birth_date[6:10]

    password = last_name[:3] + first_name[:2] + month + year

    return password


last_name = input("Enter your last name: ")
first_name = input("Enter your first name: ")
birth_date = input("Enter your date of birth (dd-mm-yyyy): ")

print(generate_password(last_name, first_name, birth_date))