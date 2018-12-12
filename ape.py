import faker
from faker import Faker
import random
import selenium
from selenium import webdriver
import string

link = 'https://janegoodall.ca/our-work/roots-and-shoots/ape-fund/vote/st-thomas-aquinas-sustainable-garden-initiative/'
domains = ['@hotmail.com', '@hotmail.ca', '@gmail.com', '@yahoo.ca', '@outlook.com', '@icloud.com']

fake = Faker()


# browser = webdriver.Firefox()
# browser.get(link)

def generate_address_1():
    mail = fake.first_name() + fake.last_name() + random.choice(domains)
    return mail

def generate_address_2():
    min_char = 1
    max_char = 5

    words = ['xx_', '_xx', 'superstar', 'malicka', 'josh', 'glados', 'indie', 'pewie', 'penguin', 'sith', 'ragnarok', 'af', '123', '01']

    allchar = string.ascii_letters + string.digits
    rand = ''.join(random.choice(allchar) for x in range(random.randint(min_char, max_char)))

    mail = random.choice([fake.first_name(),fake.last_name(), fake.word(ext_word_list=words)]) + random.choice([rand, fake.first_name(),fake.last_name(), rand]) + random.choice(domains)
    return mail.lower()


print(generate_address_2())


