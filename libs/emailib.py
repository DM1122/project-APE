import faker
from faker import Faker
import random
import string

domains = ['@hotmail.com', '@hotmail.ca', '@gmail.com', '@yahoo.ca', '@outlook.com', '@icloud.com']

fake = Faker()

def generate_address():
    char_rand_min = 1
    char_rand_max = 5

    allchar = string.ascii_letters + string.digits
    char = ''.join(random.choice(allchar) for x in range(random.randint(char_rand_min, char_rand_max)))

    address = random.choice([fake.first_name(), fake.last_name()]) + random.choice([fake.first_name(), fake.last_name(), char]) + random.choice(domains)

    return address.lower()


if __name__ == '__main__':
    print(generate_address())