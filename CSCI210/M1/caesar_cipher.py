# caesar_cipher.py
# run: python caesar_cipher.py
# Caesar Cipher Program
# This program can encrypt and decrypt messages by shifting letters.

# Number of positions to shift letters
shift = 5

# Alphabet used for encryption/decryption
alphabet = 'abcdefghijklmnopqrstuvwxyz'


def caesar(text, shift_amount, direction):
    """
    Encrypts or decrypts a message using the Caesar Cipher.
    
    Parameters:
        text          : Message to process
        shift_amount  : Number of positions to shift
        direction     : 'encrypt' or 'decrypt'
    """

    # For decryption, reverse the shift
    if direction == "decrypt":
        shift_amount = -shift_amount

    result = ""

    # Process each character in the text
    for char in text:

        # Only encrypt alphabet letters
        if char in alphabet:

            # Find the current position of the letter
            old_index = alphabet.index(char)

            # Calculate the new position
            new_index = (old_index + shift_amount) % 26

            # Get the shifted letter
            new_letter = alphabet[new_index]

            # Add it to the result string
            result += new_letter

        else:
            # Keep spaces, numbers, and punctuation unchanged
            result += char

    return result


# Main Program
print("=== Caesar Cipher ===")

while True:

    # Ask user for operation
    direction = input(
        "\nType 'encrypt' to encrypt or 'decrypt' to decrypt: "
    ).lower()

    # Ask user for message
    message = input("Enter your message: ").lower()

    # Ask user for shift value
    shift = int(input("Enter shift value: "))

    # Large shift values are reduced automatically
    shift = shift % 26

    # Process the message
    output = caesar(message, shift, direction)

    print("\nResult:")
    print(output)

    # Ask if user wants another operation
    again = input("\nDo you want to continue? (yes/no): ").lower()

    if again != "yes":
        print("Goodbye!")
        break