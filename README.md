# Password Generator

## Overview

This Python script serves as a simple yet effective tool for generating strong and random passwords. It allows users to specify the desired length and name for the password, and it automatically saves the generated passwords along with their names to a file.

## Features

- **User Input:** Prompt the user to specify the desired length of the password and provide a name for it.
- **Generate Password:** Utilize a combination of random characters to generate a password of the specified length.
- **Save Password:** Save the generated password along with its associated name to a file.
- **File Handling:** If the file for storing passwords does not exist, it is created automatically. If it already exists, new passwords are appended to it.

## Requirements

- Python 3.x
- No external libraries required

## Usage

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/password-generator.git
    cd password-generator
    ```

2. **Run the Script:**
    - Run the script by executing the following command in your terminal:
        ```bash
        python password_generator.py
        ```
    - Follow the prompts to specify the desired length of the password and provide a name for it.

3. **Generated Password:**
    - Once the password is generated, it will be displayed on the screen.
    
4. **Saved Passwords:**
    - The generated passwords along with their names will be saved in a file named `passwords.txt`.

## Example

Suppose you want to generate a password with a length of 12 characters and name it "EmailPassword". You would run the script, specify the length as 12, provide the name "EmailPassword" when prompted, and the generated password would be displayed on the screen. Additionally, the password along with its name would be saved to the `passwords.txt` file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

