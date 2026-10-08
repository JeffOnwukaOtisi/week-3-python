import random
import string

def generate_password_bis(minimum_length, maximum_length):
    length = random.randint(minimum_length, maximum_length)

    password = ""

    for i in range(length):   
        password += random.choice(string.ascii_letters)

    return password


minimum_length = int(input("enter the mininmum length of the password: "))
maximum_length = int(input("enter the maximum length of the password: "))

password = generate_password_bis(minimum_length, maximum_length)

print(f"chosen length: {len(password)}")
print(f"your password is: {password}")