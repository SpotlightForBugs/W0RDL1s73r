#!/usr/bin/env python3

# wordlist generator


from faker import Faker
from faker_wifi_essid import WifiESSID


def clear_file():
    with open("text.txt", "w") as f:
        f.write("")
    print("Done")


def fake_name_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.name() + "\n")
    print("Done")


def fake_free_email_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.free_email() + "\n")
    print("Done")


def fake_net_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.ipv4() + "\n")
    print("Done")


def fake_phone_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.phone_number() + "\n")
    print("Done")


def fake_MAC_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.mac_address() + "\n")
    print("Done")


def fake_essid_wordlist(number):
    clear_file()
    fake = Faker()
    fake.add_provider(WifiESSID)
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.wifi_essid() + "\n")
    print("Done")


def fake_password_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.password() + "\n")
    print("Done")


def fake_address_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.address() + "\n")
    print("Done")


def fake_job_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.job() + "\n")
    print("Done")


def fake_text_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.text() + "\n")
    print("Done")


def fake_sentence_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.sentence() + "\n")
    print("Done")


def fake_paragraph_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.paragraph() + "\n")
    print("Done")


def fake_user_name_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.user_name() + "\n")
    print("Done")


def fake_user_agent_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.user_agent() + "\n")
    print("Done")


def fake_snn_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.ssn() + "\n")
    print("Done")


def fake_credit_card_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.credit_card_full() + "\n")
    print("Done")


def fake_credit_card_provider_wordlist(number):
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.credit_card_provider() + "\n")
    print("Done")


try:
    fake_essid_wordlist(100)

    pass
except UniquenessException:
    print("Error - Duplicate entry, stopping generation")
