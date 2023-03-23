# Ian DeLano

# Encoder for password
def encode(password):
    EncodedPassword = ""
    for Digit in password:
        NewDigit = int(Digit) + 3
        if NewDigit > 9:
            NewDigit -= 10
        EncodedPassword += str(NewDigit)
    return EncodedPassword


# Decoder for password
def decode(password):
    DecodedPassword = ""
    for Digit in password:
        NewDigit = int(Digit) - 3
        if NewDigit < 0:
            NewDigit += 10
        DecodedPassword += str(NewDigit)
    return DecodedPassword


# Main Body which includes the menu and subsequent options
def main():

    while True:

        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")

        menu_option = int(input("Please enter an option: "))

        if menu_option == 1:  # Encodes the password
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif menu_option == 2:  # Decodes the password
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")
        elif menu_option == 3:  # Exit the program
            break


# Test Cases
if __name__ == "__main__":
    main()
