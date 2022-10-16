#This python program generates a random password length 12

import random
import string

def get_random_string(length):
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    print(result_str)

get_random_string(12)
