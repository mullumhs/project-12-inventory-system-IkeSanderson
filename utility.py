import random
def get_int(message):
    
    while True:
        try:
            i = input(message)
            i = int(i)
            return i
        except:
            print("Not Digit")
            continue

def print_debug(enabled, message):
    if enabled:
        print(message)

def get_password(message):
   password = random.randint(1000,9999)
   password.split("")
   n_a = {
    1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',
    6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
    11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O',
    16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
    21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}
