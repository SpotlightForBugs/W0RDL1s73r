#!/usr/bin/env python3

#wordlist generator 
    

from faker import Faker


def clear_file():
    with open("text.txt", 'w') as f:
        f.write('')
    print('Done')
    
    

def fake_name_wordlist_in_file():
    fake = Faker()
    with open("text.txt", 'w') as f:
        for i in range(100):
            f.write(fake.name() + '\n')
    print('Done')
    
    


