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