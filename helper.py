from faker import Faker

faker = Faker()

def generate_email_data():
    email = faker.email()
    return email

def generate_password_data():
    password = faker.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return password