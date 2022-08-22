#!/usr/bin/env python3

# wordlist generator


from faker import Faker
from faker_wifi_essid import WifiESSID


def clear_file():
    """
    The clear_file function clears the text.txt file.

    :return: A string 'done'

    """
    with open("text.txt", "w") as f:
        f.write("")
    print("Done")


def fake_name_wordlist(number):
    """
    The fake_name_wordlist function creates a text file with fake names.
       The number of names is determined by the user.

    :param number: Determine how many fake names to generate
    :return: A list of names that have been generated using the faker library

    """
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.name() + "\n")
    print("Done")


def fake_free_email_wordlist(number):
    """
    The fake_free_email_wordlist function creates a wordlist of fake free email addresses.
    The function takes one argument, number, which specifies the number of emails to be created.

    :param number: Determine how many fake emails are generated
    :return: A list of unique free email domains

    """
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.free_email() + "\n")
    print("Done")


def fake_net_wordlist(number):
    """
    The fake_net_wordlist function creates a text file with fake IP addresses.
    The function takes one argument, number, which is the number of lines to be created in the text file.

    :param number: Determine how many fake ip addresses to generate
    :return: A list of fake ip addresses

    """
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.ipv4() + "\n")
    print("Done")


def fake_phone_wordlist(number):
    """
    The fake_phone_wordlist function creates a text file with fake phone numbers.
    The function takes one argument, number, which is the number of fake phone numbers to be created.

    :param number: Determine how many fake phone numbers to generate
    :return: A list of phone numbers

    """
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.phone_number() + "\n")
    print("Done")


def fake_MAC_wordlist(number):
    """
    The fake_MAC_wordlist function creates a text file with fake MAC addresses.
    The function takes one argument, number, which is the number of lines to be written in the text file.

    :param number: Determine how many fake mac addresses to generate
    :return: A list of mac addresses

    """
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.mac_address() + "\n")
    print("Done")


def fake_essid_wordlist(number):
    """
    The fake_essid_wordlist function creates a wordlist of fake wifi essid's.
    The function takes one argument, number, which is the number of fake essid's to create.

    :param number: Specify the number of fake essids to be generated
    :return: A wordlist with the specified number of fake wifi names

    """
    clear_file()
    fake = Faker()
    fake.add_provider(WifiESSID)
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.wifi_essid() + "\n")
    print("Done")


def fake_password_wordlist(number):
    """
    The fake_password_wordlist function creates a text file with a number of fake passwords.
    The function takes one argument, the number of passwords to be created.

    :param number: Determine how many passwords to generate
    :return: A list of passwords

    """
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.password() + "\n")
    print("Done")


def fake_address_wordlist(number):
    """
    The fake_address_wordlist function creates a text file with fake addresses.
        The function takes one argument, number, which is the number of fake addresses to create.

    :param number: Determine the number of fake addresses to generate
    :return: A list of unique addresses

    """
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.address() + "\n")
    print("Done")


def fake_job_wordlist(number):
    """
    The fake_job_wordlist function creates a text file with the number of lines specified by the user.
    The function also creates a unique job title for each line in the text file.

    :param number: Determine the number of fake job titles to be generated
    :return: A list of randomly generated job titles

    """
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.job() + "\n")
    print("Done")


def fake_text_wordlist(number):
    """
    The fake_text_wordlist function creates a text file with fake words.
       It takes one argument, number, which is the number of lines to be created.

    :param number: Determine how many lines of fake text to generate
    :return: A list of strings with a random amount of words

    """
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.text() + "\n")
    print("Done")


def fake_sentence_wordlist(number):
    """
    The fake_sentence_wordlist function creates a text file with a number of sentences.
    The function takes one argument, the number of sentences to be written in the file.

    :param number: Determine how many sentences to generate
    :return: A list of strings, each string being a sentence

    """
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.sentence() + "\n")
    print("Done")


def fake_paragraph_wordlist(number):
    """
    The fake_paragraph_wordlist function creates a text file with paragraphs of fake text.
    The number of paragraphs is determined by the user.

    :param number: Determine how many fake paragraphs to generate
    :return: A list of paragraphs

    """
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.paragraph() + "\n")
    print("Done")


def fake_user_name_wordlist(number):
    """
    The fake_user_name_wordlist function creates a text file with fake user names.
    The function takes one argument, number, which is the number of fake user names to create.

    :param number: Determine how many fake user names to generate
    :return: A list of fake user names

    """
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.user_name() + "\n")
    print("Done")


def fake_user_agent_wordlist(number):
    """
    The fake_user_agent_wordlist function creates a text file containing fake user agent strings.
    The function takes one argument, number, which is the number of fake user agents to create.

    :param number: Determine how many fake user agents to generate
    :return: A list of unique user agents

    """
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.user_agent() + "\n")
    print("Done")


def fake_snn_wordlist(number):
    """
    The fake_snn_wordlist function creates a text file with the specified number of fake SSNs.
    The function also prints 'Done' when it is finished.

    :param number: Determine how many fake ssns to generate
    :return: A list of unique ssns

    """
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.ssn() + "\n")
    print("Done")


def fake_credit_card_wordlist(number):
    """
    The fake_credit_card_wordlist function creates a text file containing fake credit card numbers.
    The function takes one argument, number, which is the number of fake credit card numbers to be generated.

    :param number: Determine how many fake credit card numbers to generate
    :return: A list of strings

    """
    clear_file()
    fake = Faker()
    with open("text.txt", "w") as f:
        for i in range(number):
            f.write(fake.unique.credit_card_full() + "\n")
    print("Done")


def fake_credit_card_provider_wordlist(number):
    """
    The fake_credit_card_provider_wordlist function creates a wordlist of credit card providers.
    The function takes one argument, number, which is the number of lines to be written in the text file.

    :param number: Determine how many fake credit card providers to generate
    :return: A list of credit card providers

    """
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
