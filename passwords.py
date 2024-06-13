import random
def letter_number(message):
    d1 = random.randint(1,26)
    d2 = random.randint(1,26)
    d3 = random.randint(1,26)
    d4 = random.randint(1,26)
    
    s1 = str(d1)
    s2 = str(d2)
    s3 = str(d3)
    s4 = str(d4)
    password = s1 + s2 + s3 + s4
    n_a = {
    1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',
    6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
    11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O',
    16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
    21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
    } 

    print(n_a[d1], n_a[d2], n_a[d3], n_a[d4])
    
    attempt = input(message)
    if attempt == password:
        return True
    else:
        return False

def vigenere(Message):
    
    pass_list = ["beans", "lasagna", "password"]
    pass_choice = random.randint(0,2)
    pass_code = pass_list[pass_choice]
    pass_code = list(pass_code)
    
    key_list = ["words", "interesting","wordpass"]
    key_choice = random.randint(0,2)
    key_code = key_list[key_choice]
    key_code = list(key_code)
    
    
    print(pass_code)

    alphabet_to_number = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25
    }
    number_to_alphabet = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h',
    8: 'i',
    9: 'j',
    10: 'k',
    11: 'l',
    12: 'm',
    13: 'n',
    14: 'o',
    15: 'p',
    16: 'q',
    17: 'r',
    18: 's',
    19: 't',
    20: 'u',
    21: 'v',
    22: 'w',
    23: 'x',
    24: 'y',
    25: 'z'
}
    print(key_code)
    encrypted_pass = []
    key_num = []
    pass_num = []
    for letters in pass_code:
        pass_num.append(alphabet_to_number[letters]) 

    for letters in key_code:
        key_num.append(alphabet_to_number[letters]) 
    print(pass_num)
    print(key_num)
    

vigenere("P")