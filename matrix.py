import random
import time
def generate_random_binary_string(length):
    return ''.join(random.choice('01    ') for _ in range(length))

def generate_random_with_text(length, letter_number):
    remaining_length = length - letter_number
    row = ''.join(random.choice('01    ') for _ in range(remaining_length //2)) + TEXT_OF_MESSAGE[:letter_number] + ''.join(random.choice('01    ') for _ in range(remaining_length //2))
    return row

def generate_final_string(length, letter_number):
    remaining_length = length - letter_number
    row = ''.join(" "*(remaining_length //2)) + TEXT_OF_MESSAGE[:letter_number] + ''.join(" "*(remaining_length //2))
    return row
N_COLS = 209
START_DURATION = 300000
ANIMATION_DURATION = 300000

TEXT_OF_MESSAGE = """ PRIPOJENI DO SYSTEMU: 0607, 49.20.45.358N, 12.49.1.173E """
print("\033[32m")
for i in range(500000):
    print(" ")

for i in range(START_DURATION):
    print(generate_random_binary_string(N_COLS))
    

letter_to_generate = 0
for i in range(ANIMATION_DURATION):
    if i % 5000 == 0:
        letter_to_generate += 1
    print(generate_random_with_text(N_COLS, letter_to_generate))

for i in range(100000):
    if ((i % 50) - 25) == 0:
        print(generate_final_string(N_COLS, letter_to_generate))
    else:
        print(" "* N_COLS)

time.sleep(4)


for i in range(200000):
    print(" "* N_COLS)