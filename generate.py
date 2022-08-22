#!/usr/bin/env python3

# wordlist generator


from faker import Faker
from faker.providers import internet


def clear_file():
    with open("text.txt", 'w') as f:
        f.write('')
    print('Done')


def fake_name_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", 'w') as f:
        for i in range(number):
            f.write(fake.name() + '\n')
    print('Done')


def fake_free_email_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", 'w') as f:
        for i in range(number):
            f.write(fake.free_email() + '\n')
    print('Done')


def fake_net_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", 'w') as f:
        for i in range(number):
            f.write(fake.ipv4() + '\n')
    print('Done')


def fake_phone_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", 'w') as f:
        for i in range(number):
            f.write(fake.phone_number() + '\n')
    print('Done')


def fake_MAC_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", 'w') as f:
        for i in range(number):
            f.write(fake.mac_address() + '\n')
    print('Done')


def fake_password_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", 'w') as f:
        for i in range(number):
            f.write(fake.password() + '\n')
    print('Done')


def fake_address_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", 'w') as f:
        for i in range(number):
            f.write(fake.address() + '\n')
    print('Done')


def fake_job_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", 'w') as f:
        for i in range(number):
            f.write(fake.job() + '\n')
    print('Done')


def fake_text_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", 'w') as f:
        for i in range(number):
            f.write(fake.text() + '\n')
    print('Done')


def fake_sentence_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", 'w') as f:
        for i in range(number):
            f.write(fake.sentence() + '\n')
    print('Done')


def fake_paragraph_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", 'w') as f:
        for i in range(number):
            f.write(fake.paragraph() + '\n')
    print('Done')

