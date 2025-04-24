def print_note(message):        # message is a parameter
    print("Inside print_note:")
    print(message)              # prints the value passed in

def main():
    message = "This came from inside main"
    return message
    print_note(message) 

main()
print(note(message))