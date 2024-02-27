#!/usr/bin/env python3
"""
simple implementation of a password generator
"""
import random
import string

def generate_password(length):
    """Generate a random password of specified length."""
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def save_password(name, password):
    """Save the password and its associated name to a file."""
    # Open the file in append mode and write the name and password
    with open("passwords.txt", "a") as file:
        file.write(f"{name}: {password}\n")

def main():
    """Main function to generate and save passwords."""
    try:
        # Prompt the user to enter a name for the password
        name = input("Enter a name for the password: ")

        # Prompt the user to specify the desired length of the password
        length = int(input("Enter the desired length of the password: "))

        # Generate the password
        password = generate_password(length)

        # Display the generated password
        print("Generated Password:", password)

        # Save the password with its associated name
        save_password(name, password)

        # Display a success message
        print("Password saved successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for the length.")

if __name__ == "__main__":
    main()
